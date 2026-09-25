// Sincroniza os casos de teste da epic SGV-9296 (Departamentos — Cadastrar
// Contato/Departamento sem CPF/CNPJ) na Qase (projeto SGV, suite 220), a partir do
// conteúdo validado no vault (Obsidian/.../QA Workspace/02 Demandas/DEV/11083...md e
// 11184...md, mais os defeitos filhos quando entrarem no lote).
//
// Versão de referência pra copiar em próximas sincronizações (04/09/2026) — tem
// suporte a shared steps e escreve de volta id/hash no corrections.json depois de
// aplicar, o que a versão anterior (qase-sync-1.24-1.25/sync.js) não tem.
//
// Uso:
//   node sync.js --inspect=<id>   -> SÓ LEITURA: busca o case <id> na Qase e imprime o JSON cru.
//   node sync.js                  -> dry-run (default): só imprime o que faria, não chama a API
//   node sync.js --apply          -> aplica de verdade (shared_steps -> updates -> delete -> creates)
//   node sync.js --apply --only=<id> -> aplica de verdade só o update do case <id>
//
// Requer QASE_TESTOPS_API_TOKEN no .env do repo (mesmo token já usado pelo
// cypress-qase-reporter — ver docs/integrations/qase.md). --inspect também precisa do
// token (é uma leitura autenticada), mas não escreve nada.
//
// CAMPOS severity/type/automation são INTEIROS na API real (confirmado em 31/08, na
// sincronização do TR 1.24-1.25, via --inspect=1 contra um case real). O
// corrections.json continua com rótulos legíveis; a tradução pro inteiro certo
// acontece no mapa ENUMS abaixo. Se um rótulo novo aparecer, adicionar a entrada no
// mapa ANTES de rodar --apply — o script recusa (`toEnum` lança erro) em vez de
// adivinhar.
//
// `priority` fica de fora do payload por padrão (decisão de longa data: mais simples
// preencher/confirmar manualmente na Qase do que arriscar mapeamento não confirmado).
// `behavior` também nunca é enviado.
//
// A API da Qase faz update PARCIAL de verdade (PATCH /v1/case/{code}/{id}: campo
// omitido não é tocado) e o DELETE é IRREVERSÍVEL (sem lixeira documentada).
//
// SHARED STEPS (confirmado contra a doc oficial da API em 04/09/2026):
// - Criar: POST /v1/shared_step/{code}, body { title, steps: [{action, data,
//   expected_result}] }.
// - Listar/checar duplicata: GET /v1/shared_step/{code}?search=<título> — a API NÃO
//   faz dedup automático por título, o script confere antes de criar.
// - Assimetria real entre escrita e leitura, não é bug nosso: pra REFERENCIAR um
//   shared step ao criar/atualizar um caso, o step usa o campo `shared` = hash. Ao
//   LER (GET) um caso já salvo, a API devolve esse mesmo step com
//   `shared_step_hash`/`shared_step_nested_hash` no lugar.
// - DELETE de shared step via API: comportamento não documentado — não implementado
//   aqui de propósito.
//
// IDEMPOTÊNCIA: depois de um --apply bem-sucedido, o script reescreve
// corrections.json com o `id` de cada case criado e o `hash` de cada shared step
// criado. Uma entrada de `creates`/`shared_steps` que já tenha esse campo é PULADA
// (aviso, não erro) — rodar --apply de novo não duplica nada. Só os `updates` são
// seguros de rerodar por natureza (PATCH sobrescreve); ainda assim, tratamos o
// arquivo como o estado atual de verdade, não só um log do que foi feito uma vez.

const fs = require("fs");
const path = require("path");
require("dotenv").config({ path: path.join(__dirname, "..", ".env") });

const APPLY = process.argv.includes("--apply");
const onlyArg = process.argv.find((a) => a.startsWith("--only="));
const ONLY_ID = onlyArg ? parseInt(onlyArg.split("=")[1], 10) : null;
const inspectArg = process.argv.find((a) => a.startsWith("--inspect="));
const INSPECT_ID = inspectArg ? parseInt(inspectArg.split("=")[1], 10) : null;

// Mapa rótulo (usado no corrections.json, legível) -> inteiro (o que a API espera de
// verdade). Confirmado em 31/08 (sincronização do TR 1.24-1.25) via --inspect=1 contra
// um case real. Adicionar entradas novas aqui se algum CT usar rótulo diferente.
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
const CORRECTIONS_PATH = path.join(__dirname, "corrections.json");
const corrections = JSON.parse(fs.readFileSync(CORRECTIONS_PATH, "utf-8"));

const BASE_URL = "https://api.qase.io/v1";
const PROJECT = corrections.project_code;

function authHeaders() {
  return {
    Token: TOKEN,
    "Content-Type": "application/json",
  };
}

function persistCorrections() {
  fs.writeFileSync(CORRECTIONS_PATH, JSON.stringify(corrections, null, 2) + "\n", "utf-8");
  console.log(`corrections.json atualizado com os ids/hashes resultantes.`);
}

// Resolve o array de steps do corrections.json pro formato que a API espera. Um step
// pode ser inline ({action, data, expected_result}) ou referenciar um shared step
// já resolvido nesta execução ({shared_step_key: "..."}) — sharedHashByKey é o mapa
// key -> hash montado a partir de corrections.shared_steps antes de chegar aqui.
function buildSteps(steps, sharedHashByKey) {
  return (steps || []).map((s, i) => {
    if (s.shared_step_key) {
      const hash = sharedHashByKey.get(s.shared_step_key);
      if (!hash) {
        throw new Error(
          `Step referencia shared_step_key "${s.shared_step_key}" sem hash resolvido — confira corrections.shared_steps.`
        );
      }
      return { position: i + 1, shared: hash };
    }
    return {
      position: i + 1,
      action: s.action,
      data: s.data,
      expected_result: s.expected_result,
    };
  });
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
    return null;
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
  return json.result.id;
}

async function listSharedSteps(search) {
  const url = `${BASE_URL}/shared_step/${PROJECT}?search=${encodeURIComponent(search)}`;
  const res = await fetch(url, { headers: authHeaders() });
  const json = await res.json();
  if (!res.ok || json.status === false) {
    throw new Error(`Falha ao listar shared steps: ${JSON.stringify(json)}`);
  }
  return json.result.entities || [];
}

async function createSharedStep(body) {
  const url = `${BASE_URL}/shared_step/${PROJECT}`;
  if (!APPLY) {
    console.log(`[dry-run] POST ${url}`);
    console.log(JSON.stringify(body, null, 2));
    return null;
  }
  const res = await fetch(url, {
    method: "POST",
    headers: authHeaders(),
    body: JSON.stringify(body),
  });
  const json = await res.json();
  if (!res.ok || json.status === false) {
    throw new Error(`Falha ao criar shared step: ${JSON.stringify(json)}`);
  }
  console.log(`OK  POST novo shared step -> hash ${json.result.hash}`);
  return json.result.hash;
}

function buildUpdateBody(entry, sharedHashByKey) {
  const body = {};
  for (const key of ["title", "description", "preconditions", "postconditions"]) {
    if (entry[key] !== undefined) body[key] = entry[key];
  }
  if (entry.steps !== undefined) {
    body.steps_type = "classic";
    body.steps = buildSteps(entry.steps, sharedHashByKey);
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

async function resolveSharedSteps() {
  const sharedHashByKey = new Map();
  const sharedSteps = corrections.shared_steps || [];

  for (const entry of sharedSteps) {
    if (entry.hash) {
      console.log(`shared step "${entry.key}" já tem hash (${entry.hash}) — pulando.`);
      sharedHashByKey.set(entry.key, entry.hash);
      continue;
    }

    if (TOKEN) {
      const existing = await listSharedSteps(entry.title);
      const exact = existing.find((s) => s.title === entry.title);
      if (exact) {
        console.log(
          `shared step "${entry.title}" já existe na Qase (hash ${exact.hash}) — reaproveitando, não criando de novo.`
        );
        entry.hash = exact.hash;
        sharedHashByKey.set(entry.key, exact.hash);
        continue;
      }
    }

    const body = {
      title: entry.title,
      steps: entry.steps.map((s, i) => ({
        position: i + 1,
        action: s.action,
        data: s.data,
        expected_result: s.expected_result,
      })),
    };
    const hash = await createSharedStep(body);
    if (hash) {
      entry.hash = hash;
      sharedHashByKey.set(entry.key, hash);
    } else {
      // dry-run: sem hash real ainda, usa um placeholder só pra não quebrar a
      // montagem do restante do dry-run (updates/creates que referenciam a chave).
      sharedHashByKey.set(entry.key, `<dry-run-hash-${entry.key}>`);
    }
  }

  return sharedHashByKey;
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

  // Shared steps sempre resolvem primeiro (mesmo com --only), pra qualquer update
  // ou create que os referencie ter o hash disponível.
  const sharedHashByKey = await resolveSharedSteps();

  const updates = ONLY_ID === null
    ? corrections.updates
    : corrections.updates.filter((u) => u.id === ONLY_ID);
  const toDelete = ONLY_ID === null ? corrections.delete : [];
  const creates = ONLY_ID === null ? corrections.creates : [];

  for (const entry of updates) {
    const body = buildUpdateBody(entry, sharedHashByKey);
    await patchCase(entry.id, body);
  }

  for (const entry of toDelete) {
    await deleteCase(entry.id);
  }

  for (const entry of creates) {
    if (entry.id) {
      console.log(`create "${entry.title}" já tem id (${entry.id}) — pulando, não recriando.`);
      continue;
    }
    const { _note, steps, severity, type, behavior, automation, ...rest } = entry;
    // behavior e priority ficam de fora de propósito — ver aviso no topo do arquivo.
    const body = {
      ...rest,
      suite_id: corrections.suite_id,
      severity: toEnum("severity", severity),
      type: toEnum("type", type),
      automation: toEnum("automation", automation),
      steps: buildSteps(steps, sharedHashByKey),
    };
    const id = await createCase(body);
    if (id) entry.id = id;
  }

  if (APPLY) {
    persistCorrections();
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
