---
demanda: "[[01 - Demanda]]"
execucao: ""
ambiente: dev
versao: ""
status: execucao
responsavel: ""
resultado: aguardando
pontos: 0
ct_resultados:
  ct_001: ⏳ Aguardando
  ct_002: ⏳ Aguardando
  ct_003: ⏳ Aguardando
  ct_004: ⏳ Aguardando
  ct_005: ⏳ Aguardando
  ct_006: ⏳ Aguardando
  ct_007: ⏳ Aguardando
  ct_008: ⏳ Aguardando
  ct_009: ⏳ Aguardando
  ct_010: ⏳ Aguardando
  ct_011: ⏳ Aguardando
  ct_012: ⏳ Aguardando
  ct_013: ⏳ Aguardando
  ct_014: ⏳ Aguardando
  ct_015: ⏳ Aguardando
  ct_016: ⏳ Aguardando
  ct_017: ⏳ Aguardando
  ct_018: ⏳ Aguardando
  ct_019: ⏳ Aguardando
  ct_020: ⏳ Aguardando
data_inicio: ""
data_fim: ""
---

# Validação — SGV-12272

> [!info]- Navegação QA
> **README do card:** [[00 README|Abrir README do card]]
> **Demanda:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]

> [!settings]- Controle da validação
> **Status:** `INPUT[inlineSelect(option(execucao),option(concluido)):status]`
> **Resultado:** `INPUT[inlineSelect(option(aguardando),option(aprovado),option(reprovado),option(aprovado_com_ressalvas)):resultado]`
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`

> Registro da validação dos 20 CTs (CT-001 a CT-020, redigidos em `03 - Casos de teste.md`). Fluxo real: execução em ambiente DEV pelo Rafael, com evidência gravada e gate de doc do módulo (ver "Pré-requisitos de execução" abaixo) — decisão de 20/10/2026. **Esta nota está preparada; nenhum resultado foi registrado ainda.**

---

## Contexto

- Ambiente:
- Versão/build:

---

## Resumo da execução

```dataviewjs
const paginaResumo = dv.current() ?? {};
const resultadosResumo = paginaResumo.ct_resultados ?? {};
const pontosEtapaResumo = Number(paginaResumo.pontos) || 0;
const totalCTsResumo = Object.keys(resultadosResumo).length;
const aprovadosResumo = Object.values(resultadosResumo).filter((resultado) => String(resultado).includes("Aprovado")).length;
const pesoResumo = (resultado) => {
  const status = String(resultado);
  if (status.includes("Aprovado") || status.includes("Falhou")) return 1;
  if (status.includes("Em andamento")) return 0.25;
  if (status.includes("Bloqueado")) return 0.5;
  return 0;
};
const executadosResumo = Object.values(resultadosResumo).filter((resultado) => pesoResumo(resultado) > 0).length;
const pontosEntreguesResumo = totalCTsResumo
  ? Math.round(Object.values(resultadosResumo).reduce((total, resultado) => total + (pontosEtapaResumo / totalCTsResumo) * pesoResumo(resultado), 0) * 100) / 100
  : 0;

dv.list([
  `CTs aprovados: ${aprovadosResumo}/${totalCTsResumo}`,
  `CTs executados: ${executadosResumo}/${totalCTsResumo}`,
  `Pontos da etapa: ${pontosEtapaResumo}`,
  `Pontos entregues: ${pontosEntreguesResumo} de ${pontosEtapaResumo}`,
]);
```

---

## Resultado dos casos de teste

| CT | Resultado | Evidência | Observação | Defeito/Bug | Pontos entregues |
|---|---|---|---|---|---:|
| [[03 - Casos de teste#^ct-001\|CT-001]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_001]` |  |  |  | `= choice(this.ct_resultados.ct_001 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-002\|CT-002]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_002]` |  |  |  | `= choice(this.ct_resultados.ct_002 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-003\|CT-003]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_003]` |  |  |  | `= choice(this.ct_resultados.ct_003 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-004\|CT-004]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_004]` |  |  |  | `= choice(this.ct_resultados.ct_004 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-005\|CT-005]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_005]` |  |  |  | `= choice(this.ct_resultados.ct_005 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-006\|CT-006]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_006]` |  |  |  | `= choice(this.ct_resultados.ct_006 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-007\|CT-007]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_007]` |  |  |  | `= choice(this.ct_resultados.ct_007 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-008\|CT-008]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_008]` |  |  |  | `= choice(this.ct_resultados.ct_008 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-009\|CT-009]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_009]` |  |  |  | `= choice(this.ct_resultados.ct_009 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-010\|CT-010]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_010]` |  |  |  | `= choice(this.ct_resultados.ct_010 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-011\|CT-011]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_011]` |  |  |  | `= choice(this.ct_resultados.ct_011 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-012\|CT-012]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_012]` |  |  |  | `= choice(this.ct_resultados.ct_012 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-013\|CT-013]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_013]` |  |  |  | `= choice(this.ct_resultados.ct_013 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-014\|CT-014]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_014]` |  |  |  | `= choice(this.ct_resultados.ct_014 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-015\|CT-015]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_015]` |  |  |  | `= choice(this.ct_resultados.ct_015 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-016\|CT-016]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_016]` |  |  |  | `= choice(this.ct_resultados.ct_016 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-017\|CT-017]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_017]` |  |  |  | `= choice(this.ct_resultados.ct_017 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-018\|CT-018]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_018]` |  |  |  | `= choice(this.ct_resultados.ct_018 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-019\|CT-019]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_019]` |  |  |  | `= choice(this.ct_resultados.ct_019 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |
| [[03 - Casos de teste#^ct-020\|CT-020]] | `INPUT[inlineSelect(option(⏳ Aguardando),option(🔵 Em andamento),option(✅ Aprovado),option(❌ Falhou),option(🚫 Bloqueado),option(⚪ Não executado)):ct_resultados.ct_020]` |  |  |  | `= choice(this.ct_resultados.ct_020 = "✅ Aprovado", round(number(this.pontos) / length(this.ct_resultados), 2), 0)` |

> **Regra de esforço:** aprovado e falhou = 100% da parcela; em andamento = 25%; bloqueado = 50%; aguardando e não executado = 0%.

> **Pontos entregues:** a coluna é calculada automaticamente conforme o status de cada CT.

```dataviewjs
const pagina = dv.current() ?? {};
const resultados = pagina.ct_resultados ?? {};
const pontosEtapa = Number(pagina.pontos) || 0;
const totalCTs = Object.keys(resultados).length;
const pesoDoStatus = (resultado) => {
  const status = String(resultado);
  if (status.includes("Aprovado") || status.includes("Falhou")) return 1;
  if (status.includes("Em andamento")) return 0.25;
  if (status.includes("Bloqueado")) return 0.5;
  return 0;
};
const raiz = dv.container.closest(".markdown-preview-view") ?? document;
const tabela = Array.from(raiz.querySelectorAll("table")).find((item) => item.innerText.includes("Pontos entregues"));
if (tabela) {
  const pontosPorCT = totalCTs ? pontosEtapa / totalCTs : 0;
  Array.from(tabela.querySelectorAll("tbody tr")).forEach((linha, indice) => {
    const chave = `ct_${String(indice + 1).padStart(3, "0")}`;
    const celula = linha.lastElementChild;
    if (celula) {
      const pontos = pontosPorCT * pesoDoStatus(resultados[chave]);
      celula.textContent = pontos ? (Math.round(pontos * 100) / 100).toString() : "0";
    }
  });
}
```

> A prévia do CT é exibida pelo Obsidian ao passar o mouse sobre cada link. A tabela é o registro da execução; o conteúdo do cenário permanece em `03 - Casos de teste.md`.

---

## Pré-requisitos de execução

Por CT: ator/conta necessária, massa de dados de que depende (extraída das Pré-condições em `03 - Casos de teste.md`) e o doc do módulo pra rodar o gate de verificação (SKILL_VERIFICACAO_DOC) antes de marcar ✅. **Confirmado?** marca se a massa de dados/configuração já existe no ambiente ou se ainda precisa ser confirmada/montada antes da gravação.

| CT | Ator/conta necessária | Massa de dados | Doc do módulo (gate) | Confirmado? |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-001\|CT-001]] | Servidor Público cadastrado e ativo | CPF e senha conhecidos, conta sem bloqueio | [[QA Workspace/04 Conhecimento/Módulos/Login\|Login]] | A informar |
| [[03 - Casos de teste#^ct-002\|CT-002]] | Uma conta ativa (Servidor, Cidadão ou Empresa), sacrificável — vai ficar bloqueada | Conta sem bloqueio nem tentativa malsucedida recente; não reaproveitar a conta do CT-001 | [[QA Workspace/04 Conhecimento/Módulos/Login\|Login]] | A informar |
| [[03 - Casos de teste#^ct-003\|CT-003]] | Servidor com permissão para alterar status funcional de outro Servidor + o Servidor-alvo (status inicial "Ativo") | Servidor-alvo com permissões completas, disponível pra mudar entre Ativo/Licença/Férias/Inativo(ou "Suspenso") | [[QA Workspace/04 Conhecimento/Módulos/Usuário Servidor\|Usuário Servidor]] | A informar |
| [[03 - Casos de teste#^ct-004\|CT-004]] | Servidor vinculado (N:N) a 2 Setores no mesmo Módulo | Setor A marcado "Setor criador", Setor B não, e o Serviço/Assunto do teste com a lista herdada de "Setores que criam" mantendo A — **não confirmado como já existente** | [[QA Workspace/04 Conhecimento/Módulos/Tramitação\|Tramitação]] | **Não confirmado** |
| [[03 - Casos de teste#^ct-005\|CT-005]] | Servidor com permissão de criar Assunto/Serviço | Módulo já cadastrado com categoria-base definida (DO/CO/PA) | [[QA Workspace/04 Conhecimento/Módulos/Serviços e Assuntos\|Serviços e Assuntos]] | A informar |
| [[03 - Casos de teste#^ct-006\|CT-006]] | Acesso de configuração de Tramitação (provável Administrador) | Módulo com 3 Setores (X, Y, Z) e ≥2 Assuntos/Serviços; Setor Z removido de "recebem e tramitam" só num deles — **não confirmado como já existente** | [[QA Workspace/04 Conhecimento/Módulos/Tramitação\|Tramitação]] | **Não confirmado** |
| [[03 - Casos de teste#^ct-007\|CT-007]] | Cidadão/Empresa (acesso público, sem login) + alguém que publique a Zona antes (Servidor/Administrador) | Zona publicada com ao menos uma Categoria de uso associada — **não confirmado como já existente** | [[QA Workspace/04 Conhecimento/Módulos/Processos Urbanísticos\|Processos Urbanísticos]] | **Não confirmado** |
| [[03 - Casos de teste#^ct-008\|CT-008]] | Cidadão/Empresa (inicia processo) + Servidor com permissão de revisão de Anexo | Mesma Zona publicada do CT-007 (reaproveitável); Processo com ao menos um Anexo | [[QA Workspace/04 Conhecimento/Módulos/Processos Urbanísticos\|Processos Urbanísticos]] | **Não confirmado** |
| [[03 - Casos de teste#^ct-009\|CT-009]] | Servidor tramitando um documento | Dois Modelos simples compatíveis com o mesmo serviço/assunto (um com herança de dados, outro sem) + um formulário preenchido com dados herdáveis — **não confirmado como já existente** | [[QA Workspace/04 Conhecimento/Módulos/Gerar Documento\|Gerar Documento]] | **Não confirmado** |
| [[03 - Casos de teste#^ct-010\|CT-010]] | Servidor tramitando documento | Módulo "Fluxo de trabalho" contratado/habilitado no Ambiente Cliente (funcionalidade opcional, não padrão) + Fluxo com Etapa configurada com despacho customizado e assinatura obrigatórios + Documento parado nessa Etapa — **não confirmado como já existente/habilitado** | [[QA Workspace/04 Conhecimento/Módulos/Fluxo de trabalho (Workflow)\|Fluxo de trabalho (Workflow)]] | **Não confirmado** |
| [[03 - Casos de teste#^ct-011\|CT-011]] | Servidor vinculado a mais de um Setor | Documentos do Servidor/Setor em "Em aberto", "Em tramitação", "Concluído" e com assinatura pendente ou prazo vencendo/vencido | [[QA Workspace/04 Conhecimento/Módulos/Mesa de trabalho\|Mesa de trabalho]] | A informar |
| [[03 - Casos de teste#^ct-012\|CT-012]] | Servidor A (cria etiquetas) + Servidor B (outro Setor, verifica visibilidade) | 2 Documentos para aplicar etiquetas; etiquetas específicas do teste — não usar a etiqueta padrão "Urgente" | [[QA Workspace/04 Conhecimento/Módulos/Etiquetas\|Etiquetas]] | A informar |
| [[03 - Casos de teste#^ct-013\|CT-013]] | Cidadão (PF) ou Empresa (PJ) se cadastrando como Contato externo | CPF/CNPJ ainda sem Contato externo associado (cadastro único); acesso à caixa de e-mail usada no cadastro | [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão\|Usuário Cidadão]] | A informar |
| [[03 - Casos de teste#^ct-014\|CT-014]] | Cidadão/Empresa/Ente externo acessando a Central de atendimento | Serviço já disponibilizado pelo órgão e acessível pela Central | [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão\|Usuário Cidadão]] | A informar |
| [[03 - Casos de teste#^ct-015\|CT-015]] | Usuário externo cadastrado, com acesso ao próprio ambiente virtual | Nenhuma massa adicional além do cadastro | [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão\|Usuário Cidadão]] *(doc cobre o ambiente do cidadão de forma geral — confirmar se trata "ambiente virtual"/Demanda como o CT descreve)* | A informar |
| [[03 - Casos de teste#^ct-016\|CT-016]] | Servidor (vê mural interno) + Cidadão (acessa Jornal Oficial, sem login) | Documento configurado para divulgação (mural interno e/ou canal externo) | [[QA Workspace/04 Conhecimento/Módulos/Divulgar Documento\|Divulgar Documento]] | A informar |
| [[03 - Casos de teste#^ct-017\|CT-017]] | Ao menos 1 signatário interno (Servidor) e 1 externo | Solicitação de assinatura sequencial já criada, com ordem definida, pronta para a tentativa fora da vez — **não confirmado como já existente/montável** | [[QA Workspace/04 Conhecimento/Módulos/Assinaturas\|Assinaturas]] | **Não confirmado** |
| [[03 - Casos de teste#^ct-018\|CT-018]] | Servidor concedente + Servidor convenente | Chave de acesso já concedida, com limite de uso definido — **não confirmado como já existente** | [[QA Workspace/04 Conhecimento/Módulos/Chaves de Acesso\|Chaves de Acesso]] | **Não confirmado** |
| [[03 - Casos de teste#^ct-019\|CT-019]] | Servidor com permissão de administrador geral + Servidor sem administrador geral e sem a permissão extra "configuração de instância" | Acesso à tela de Configurações da Instância | [[QA Workspace/04 Conhecimento/Módulos/Configurações da Instância\|Configurações da Instância]] | A informar |
| [[03 - Casos de teste#^ct-020\|CT-020]] | Administrador/usuário autorizado | Servidores cadastrados com diferentes status e níveis de permissão (provavelmente já existentes na base) | *sem doc localizada* | A informar |

> [!warning] Pré-requisitos ainda não confirmados como existentes
> CT-004, CT-006, CT-007, CT-008, CT-009, CT-010, CT-017 e CT-018 dependem de configuração/massa de dados específica que não tem confirmação de já existir no ambiente (ver coluna acima). Rafael precisa confirmar ou montar essa massa antes de gravar esses CTs — nenhuma arquitetura de seed/dados de teste foi decidida nesta demanda (fora de escopo, `01 - Demanda.md`).

### Capturas para a automação

Aproveitar a execução manual para recolher o que a automação da Onda 1 ainda não tem no código (levantamento em [[QA Workspace/02 Demandas/DEV/SGV-12272 - Casos de teste e publicação da Onda 1 de sanidade do TR/01 Automação/01 - Análise|01 Automação/01 - Análise]]). CTs fora da tabela já têm código reaproveitável: só executar e gravar a evidência normal.

**Como capturar:**
- **Requisições:** DevTools → aba Network → marcar *Preserve log* → filtro `graphql` → executar o CT → exportar como HAR com o nome `12272-CT-0xx.har`.
- **Tela sem mapeamento:** `npx playwright codegen https://homolog.sogov.com.br` (ou a URL do ambiente em uso) e salvar o script gerado como `12272-CT-0xx.spec.ts`.
- **Comportamento a observar:** print ou o próprio vídeo da evidência, anotando na coluna Observação do resultado.

> [!danger] HAR leva o token da sessão
> Salvar em `~/Downloads/capturas-onda1/`, **fora do vault** (o vault sobe pro GitHub pelo backup automático). Nada de HAR ou script com credencial dentro do vault; o token é removido antes de qualquer trecho virar referência aqui.

| CT | O que capturar | Tipo | Por quê | Capturado? |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-002\|CT-002]] | Desbloqueio pelo link do e-mail de reativação **e** desbloqueio interno feito por servidor | HAR | Confirma o tipo de usuário do desbloqueio (`publicAgent`) e o fluxo do link | ☐ |
| [[03 - Casos de teste#^ct-003\|CT-003]] | Mudança de status do servidor-alvo (Ativo → Licença → Férias → Inativo) | HAR | A chamada só é conhecida pelo código do produto, que pode estar desatualizado | ☐ |
| [[03 - Casos de teste#^ct-007\|CT-007]] | Criar Categoria de uso, criar e publicar a Zona, consulta pública da Zona | HAR + codegen | Não existe nada no código de testes para Zona/Categoria de uso | ☐ |
| [[03 - Casos de teste#^ct-008\|CT-008]] | Abrir Processo urbanístico a partir da Zona e revisar o Anexo | HAR + codegen | Não existe nada no código de testes para Processo urbanístico | ☐ |
| [[03 - Casos de teste#^ct-014\|CT-014]] | Canais digitais da Central de atendimento | codegen | Sem funções de tela para essa área | ☐ |
| [[03 - Casos de teste#^ct-016\|CT-016]] | Acesso ao Jornal Oficial público, sem login | codegen | Sem funções de tela para o lado público | ☐ |
| [[03 - Casos de teste#^ct-017\|CT-017]] | O que aparece ao tentar assinar fora da vez | Observar | Comportamento não confirmado no próprio CT | ☐ |
| [[03 - Casos de teste#^ct-018\|CT-018]] | Notificação recebida pelo concedente | Observar | Comportamento e canal não confirmados no próprio CT | ☐ |
| [[03 - Casos de teste#^ct-019\|CT-019]] | Salvar cores/imagens como **administrador geral** **e** a tentativa de um servidor **sem administrador geral e sem a permissão extra "configuração de instância"**. Se der, conceder a permissão extra a um servidor e repetir a edição (segundo acesso válido, ainda não testado) | HAR + codegen | Não existe função de edição da instância no código de testes; a Onda 1 cria uma instância própria para este CT | ☐ |

> [!info] CT-002 e o SGV-12316
> O bug [[QA Workspace/02 Demandas/HML/SGV-12316 - Bug Login com senha correta aceito com a conta bloqueada/00 QA/01 - Bug|SGV-12316]] (senha correta ainda autentica depois do bloqueio, reproduzido em homologação) é erro de produto, já aberto — está fora do alcance do CT-002. O CT-002 continua validando só o bloqueio na 5ª tentativa (o alvo original do cenário) e deve ser registrado pelo que ele de fato verifica: o bloqueio. Se o comportamento do SGV-12316 reproduzir também em DEV durante a execução, registrar como observação referenciando o SGV-12316 — sem marcar o CT-002 como falho por causa dele. A captura do desbloqueio (tabela acima) continua valendo.

### Ordem sugerida de execução

Agrupando por conta/dados compartilhados, pra gravar menos vídeos:

1. **CT-001, CT-002** — tela de Login (contas diferentes: gravar o CT-001 primeiro, com a conta "boa"; o CT-002 usa uma conta sacrificável, que ficará bloqueada).
2. **CT-003** — estados funcionais do Servidor (Administrador + Servidor-alvo).
3. **CT-004, CT-006** — configuração de Setores/Tramitação (mesmo Módulo-base, mudando só a configuração testada em cada um).
4. **CT-005** — Assunto/Serviço herdando categoria-base (mesma área de configuração de Módulo do grupo anterior).
5. **CT-011, CT-012** — Mesa de trabalho + Etiquetas (mesmo Servidor vinculado a múltiplos Setores; Servidores A/B reaproveitáveis).
6. **CT-007, CT-008** — Zona pública + Processo urbanístico (mesma Zona publicada reaproveitada entre os dois).
7. **CT-009** — Modelos simples com/sem herança.
8. **CT-010** — Fluxo de trabalho com despacho/assinatura obrigatórios (isolado por depender do módulo contratado à parte).
9. **CT-017, CT-018** — Assinatura sequencial + Chave de acesso (podem reaproveitar os mesmos Servidores internos/externo como signatários/concedente-convenente).
10. **CT-013, CT-014, CT-015** — ciclo do usuário externo: cadastro (013) → Central de atendimento (014) → ambiente virtual/Demanda (015), mesma conta de Cidadão/Empresa em sequência.
11. **CT-016** — Divulgação (Servidor + Cidadão; pode reaproveitar o Cidadão do grupo anterior pra conferir o Jornal Oficial).
12. **CT-019, CT-020** — Personalização do Órgão + Estatísticas de Servidores (ambos com conta Administrador).

---

## Histórico de validação

Use esta seção somente quando houver reteste após correção:

- **Rodada inicial:** registre o CT reprovado e o defeito aberto.
- **Correção:** vincule o bug e o Fix DEV.
- **Reteste:** registre o resultado final e a data.

---

## Decisão

**Resultado geral:** aguardando / aprovado / reprovado / aprovado com ressalvas

---

## Checklist de encerramento QA

- [ ] Todos os CTs executados ou com justificativa registrada.
- [ ] Evidências e observações preenchidas quando necessário.
- [ ] Bugs filhos vinculados na coluna **Defeito/Bug**.
- [ ] Resultado geral definido.
- [ ] Status da validação e da demanda atualizados.
- [ ] Próximo passo registrado.
