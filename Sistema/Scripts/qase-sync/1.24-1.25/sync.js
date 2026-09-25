// Sincroniza os 39 casos do TR 1.24-1.25 na Qase (projeto SGV) com o conteúdo já
// validado no vault (Obsidian/.../Termo de Referência 1.24-1.25/1.24-1.25 - Casos de
// Teste (Dado-Quando-Então).md), que passou a ser a fonte única em 31/08.
//
// Uso:
//   node sync.js --inspect=1      -> SÓ LEITURA: busca o case 1 na Qase e imprime o JSON cru.
//   node sync.js                  -> dry-run (default): só imprime o que faria, não chama a API
//   node sync.js --apply          -> aplica de verdade contra a Qase (updates + deletes + create)
//   node sync.js --apply --only=4 -> aplica de verdade só no case id 4
//
// Requer QASE_TESTOPS_API_TOKEN no .env do repo (mesmo token já usado pelo
// cypress-qase-reporter — ver docs/integrations/qase.md). --inspect também precisa do
// token (é uma leitura autenticada), mas não escreve nada.
//
// CAMPOS severity/type/automation são INTEIROS na API real (confirmado em 31/08 via
// `node sync.js --inspect=1` contra o case 1 de verdade — devolveu severity:4, type:7,
// automation:0 — batendo com os rótulos "normal"/"acceptance"/"is-not-automated" do
// export). O corrections.json continua com rótulos legíveis; a tradução pro inteiro
// certo acontece no mapa ENUMS abaixo, na hora de montar cada chamada.
//
// `priority` foi deliberadamente removido de todo o payload (updates e create) —
// decisão do Rafael em 31/08: é campo fácil de preencher manualmente na Qase depois,
// e não dava pra confirmar o mapeamento 1/2/3 (low/medium/high) empiricamente, já
// que nenhum dos 39 casos originais tinha prioridade definida (todos undefined/0).
//
// `behavior` também nunca é enviado — o valor observado no case 1 não bateu com o
// padrão esperado pro rótulo "undefined" do export, e não vale o risco.
//
// Os antigos ids 13 e 33 (órfãos, absorvidos por outros 4 casos desde 19/08) não são
// mais "depreciados" — decisão do Rafael em 31/08: excluir de vez (DELETE
// /v1/case/{code}/{id}), mais simples que mexer no campo status. A explicação de por
// que eles não existem mais fica registrada na seção "G. Fora de execução" do vault.
// ATENÇÃO: a doc da Qase descreve esse endpoint como "completely deletes a test case
// from repository" — sem menção a lixeira/recuperação. Tratar como IRREVERSÍVEL.
//
// A API da Qase faz update PARCIAL de verdade (confirmado na doc do endpoint PATCH
// /v1/case/{code}/{id}: "only fields present in the payload are validated;
// required fields not included are not enforced" — campo omitido não é tocado).
//
// Por caso, faz: PATCH nos casos existentes com conteúdo a corrigir, DELETE nos 2
// casos órfãos, e POST no único caso novo (equivalente ao CT-017, desbloqueio manual)
// — deletes e create pulados quando --only é usado.

const fs = require("fs");
const path = require("path");
require("dotenv").config({ path: path.join(__dirname, "..", ".env") });

const APPLY = process.argv.includes("--apply");
const onlyArg = process.argv.find((a) => a.startsWith("--only="));
const ONLY_ID = onlyArg ? parseInt(onlyArg.split("=")[1], 10) : null;
const inspectArg = process.argv.find((a) => a.startsWith("--inspect="));
const INSPECT_ID = inspectArg ? parseInt(inspectArg.split("=")[1], 10) : null;

// Mapa rótulo (usado no corrections.json, legível) -> inteiro (o que a API espera de
// verdade). Confirmado em 31/08 via --inspect=1 contra o case 1 real.
const ENUMS = {
  severity: { normal: 4 },
  type: { acceptance: 7 },
  automation: { "is-not-automated": 0 },
};

function toEnum(field, label) {
  const value = ENUMS[field][label];
  if (value === undefined) {
    throw new Error(`Valor "${label}" sem mapeamento conhecido pro campo "${field}"`);
  }
  return value;
}

const TOKEN = process.env.QASE_TESTOPS_API_TOKEN;
const corrections = JSON.parse(
  fs.readFileSync(path.join(__dirname, "corrections.json"), "utf-8")
);

const BASE_URL = "https://api.qase.io/v1";
const PROJECT = corrections.project_code;

function authHeaders() {
  return {
    Token: TOKEN,
    "Content-Type": "application/json",
  };
}

async function patchCase(id, body) {
  const url = `${BASE_URL}/case/${PROJECT}/${id}`;
  if (!APPLY) {
    console.log(`[dry-run] PATCH ${url}`);
    console.log(JSON.stringify(body, null, 2));
    return;
  }
  const res = await fetch(url, {
    method: "PATCH",
    headers: authHeaders(),
    body: JSON.stringify(body),
  });
  const json = await res.json();
  if (!res.ok || json.status === false) {
    throw new Error(`Falha ao atualizar case ${id}: ${JSON.stringify(json)}`);
  }
  console.log(`OK  PATCH case ${id}`);
}

async function deleteCase(id) {
  const url = `${BASE_URL}/case/${PROJECT}/${id}`;
  if (!APPLY) {
    console.log(`[dry-run] DELETE ${url} (IRREVERSÍVEL quando aplicado de verdade)`);
    return;
  }
  const res = await fetch(url, {
    method: "DELETE",
    headers: authHeaders(),
  });
  const json = await res.json();
  if (!res.ok || json.status === false) {
    throw new Error(`Falha ao excluir case ${id}: ${JSON.stringify(json)}`);
  }
  console.log(`OK  DELETE case ${id}`);
}

async function createCase(body) {
  const url = `${BASE_URL}/case/${PROJECT}`;
  if (!APPLY) {
    console.log(`[dry-run] POST ${url}`);
    console.log(JSON.stringify(body, null, 2));
    return;
  }
  const res = await fetch(url, {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify(body),
  });
  const json = await res.json();
  if (!res.ok || json.status === false) {
    throw new Error(`Falha ao criar case: ${JSON.stringify(json)}`);
  }
  console.log(`OK  POST novo case -> id ${json.result.id}`);
}

function buildUpdateBody(entry) {
  const body = {};
  for (const key of ["title", "description", "preconditions", "postconditions"]) {
    if (entry[key] !== undefined) body[key] = entry[key];
  }
  if (entry.steps !== undefined) {
    body.steps_type = "classic";
    body.steps = entry.steps.map((s, i) => ({
      position: i + 1,
      action: s.action,
      data: s.data,
      expected_result: s.expected_result,
    }));
  }
  return body;
}

async function inspectCase(id) {
  if (!TOKEN) {
    console.error(
      "QASE_TESTOPS_API_TOKEN não encontrado no .env — necessário mesmo pra leitura."
    );
    process.exit(1);
  }
  const url = `${BASE_URL}/case/${PROJECT}/${id}`;
  const res = await fetch(url, { headers: authHeaders() });
  const json = await res.json();
  if (!res.ok || json.status === false) {
    throw new Error(`Falha ao buscar case ${id}: ${JSON.stringify(json)}`);
  }
  console.log(`=== GET ${url} (só leitura, nada foi escrito) ===\n`);
  console.log(JSON.stringify(json.result, null, 2));
}

async function main() {
  if (INSPECT_ID !== null) {
    await inspectCase(INSPECT_ID);
    return;
  }

  if (APPLY && !TOKEN) {
    console.error(
      "QASE_TESTOPS_API_TOKEN não encontrado no .env — configure antes de rodar (mesmo token do cypress-qase-reporter)."
    );
    process.exit(1);
  }
  if (!APPLY) {
    console.log(
      "=== DRY-RUN — nenhuma chamada real será feita. Rode com --apply para aplicar de verdade. ===\n"
    );
  }
  if (ONLY_ID !== null) {
    console.log(`=== --only=${ONLY_ID} — processando só esse case (deletes/creates pulados). ===\n`);
  }

  const updates = ONLY_ID === null
    ? corrections.updates
    : corrections.updates.filter((u) => u.id === ONLY_ID);
  const toDelete = ONLY_ID === null ? corrections.delete : [];
  const creates = ONLY_ID === null ? corrections.creates : [];

  for (const entry of updates) {
    const body = buildUpdateBody(entry);
    await patchCase(entry.id, body);
  }

  for (const entry of toDelete) {
    await deleteCase(entry.id);
  }

  for (const entry of creates) {
    const { _note, steps, severity, type, behavior, automation, ...rest } = entry;
    // behavior e priority ficam de fora de propósito — ver aviso no topo do arquivo.
    const body = {
      ...rest,
      suite_id: corrections.suite_id,
      severity: toEnum("severity", severity),
      type: toEnum("type", type),
      automation: toEnum("automation", automation),
      steps: (steps || []).map((s, i) => ({
        position: i + 1,
        action: s.action,
        data: s.data,
        expected_result: s.expected_result,
      })),
    };
    await createCase(body);
  }

  console.log(
    APPLY
      ? "\nConcluído — mudanças aplicadas na Qase."
      : "\nDry-run concluído. Revise a saída acima e rode com --apply quando estiver pronto."
  );
}

main().catch((err) => {
  console.error(err);
  process.exit(1);
});
