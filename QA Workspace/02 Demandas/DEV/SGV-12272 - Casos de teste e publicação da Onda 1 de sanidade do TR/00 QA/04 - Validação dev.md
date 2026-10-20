---
demanda: "[[01 - Demanda]]"
execucao: ""
ambiente: dev
versao: ""
status: execucao
responsavel: ""
resultado: aguardando
pontos: 0
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
| [[03 - Casos de teste#^ct-019\|CT-019]] | Servidor Administrador + Servidor com outro nível de acesso | Acesso à área de Personalização do Órgão | *sem doc localizada* | A informar |
| [[03 - Casos de teste#^ct-020\|CT-020]] | Administrador/usuário autorizado | Servidores cadastrados com diferentes status e níveis de permissão (provavelmente já existentes na base) | *sem doc localizada* | A informar |

> [!warning] Pré-requisitos ainda não confirmados como existentes
> CT-004, CT-006, CT-007, CT-008, CT-009, CT-010, CT-017 e CT-018 dependem de configuração/massa de dados específica que não tem confirmação de já existir no ambiente (ver coluna acima). Rafael precisa confirmar ou montar essa massa antes de gravar esses CTs — nenhuma arquitetura de seed/dados de teste foi decidida nesta demanda (fora de escopo, `01 - Demanda.md`).

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

## Resultado dos casos de teste

| CT | Resultado | Evidência | Observação | Defeito/Bug |
|---|---|---|---|---|
| [[03 - Casos de teste#^ct-001\|CT-001]] | ⚪ Pendente | | | |
| [[03 - Casos de teste#^ct-002\|CT-002]] | ⚪ Pendente | | | |
| [[03 - Casos de teste#^ct-003\|CT-003]] | ⚪ Pendente | | | |
| [[03 - Casos de teste#^ct-004\|CT-004]] | ⚪ Pendente | | | |
| [[03 - Casos de teste#^ct-005\|CT-005]] | ⚪ Pendente | | | |
| [[03 - Casos de teste#^ct-006\|CT-006]] | ⚪ Pendente | | | |
| [[03 - Casos de teste#^ct-007\|CT-007]] | ⚪ Pendente | | | |
| [[03 - Casos de teste#^ct-008\|CT-008]] | ⚪ Pendente | | | |
| [[03 - Casos de teste#^ct-009\|CT-009]] | ⚪ Pendente | | | |
| [[03 - Casos de teste#^ct-010\|CT-010]] | ⚪ Pendente | | | |
| [[03 - Casos de teste#^ct-011\|CT-011]] | ⚪ Pendente | | | |
| [[03 - Casos de teste#^ct-012\|CT-012]] | ⚪ Pendente | | | |
| [[03 - Casos de teste#^ct-013\|CT-013]] | ⚪ Pendente | | | |
| [[03 - Casos de teste#^ct-014\|CT-014]] | ⚪ Pendente | | | |
| [[03 - Casos de teste#^ct-015\|CT-015]] | ⚪ Pendente | | | |
| [[03 - Casos de teste#^ct-016\|CT-016]] | ⚪ Pendente | | | |
| [[03 - Casos de teste#^ct-017\|CT-017]] | ⚪ Pendente | | | |
| [[03 - Casos de teste#^ct-018\|CT-018]] | ⚪ Pendente | | | |
| [[03 - Casos de teste#^ct-019\|CT-019]] | ⚪ Pendente | | | |
| [[03 - Casos de teste#^ct-020\|CT-020]] | ⚪ Pendente | | | |

---

## Decisão

**Resultado geral:** aguardando

---

## Checklist de encerramento QA

- [ ] Todos os CTs executados ou com justificativa registrada.
- [ ] Evidências e observações preenchidas quando necessário.
- [ ] Bugs filhos vinculados na coluna **Defeito/Bug**.
- [ ] Resultado geral definido.
- [ ] Status da validação e da demanda atualizados.
- [ ] Próximo passo registrado.
