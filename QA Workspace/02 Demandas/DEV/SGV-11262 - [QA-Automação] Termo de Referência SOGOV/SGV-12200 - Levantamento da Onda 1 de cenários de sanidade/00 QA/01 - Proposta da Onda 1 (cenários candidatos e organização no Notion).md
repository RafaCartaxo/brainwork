---
tags: [qa]
task: "SGV-12200"
pai: "SGV-11262"
tipo: "proposta-cenarios"
status: rascunho
---
# 01 - Proposta da Onda 1 (cenários candidatos e organização no Notion)

> [!info]- Navegação
> **README do card:** [[00 README|Abrir README do card]]
> **Modelo-alvo dos dados do preset (04):** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 - Modelo-alvo dos dados do preset]]
> **Matriz de fornecimento dos dados (05):** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/05 - Matriz de fornecimento dos dados|05 - Matriz de fornecimento dos dados]]
> **Mapa geral:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/00 - Mapa geral|00 - Mapa geral]]
> **Matriz de atores e relações:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/01 - Matriz de atores e relações|01 - Matriz de atores e relações]]
> **Recortes do TR:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/01 - Matriz de atores e relações|Seções do TR (índice: Matriz de atores e relações)]]
> **Fonte normativa:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/Fontes/Termo de Referência SOGOV.pdf|Termo de Referência SOGOV.pdf]]

> [!important] Proposta rastreável, pendente de aprovação do Rafael — não é seleção oficial, CT, automação ou execução
> Esta nota propõe a **Onda 1** de 20 cenários candidatos de sanidade, decidida por Rafael em 15/10/2026 como resposta à ausência de uma lista oficial na fonte disponível da SGV-12200. Cada cenário cita sua referência exata do TR, sua ligação com o modelo-alvo (04) e a matriz de fornecimento (05), e é justificado por valor de sanidade e rastreabilidade — nunca por já existir um CT ou automação correspondente. Nenhum passo de execução, asserção de CT ou código é redigido aqui. Ondas adicionais de 20 cenários são esperadas em rodadas futuras, cobrindo o que esta onda não cobre (ver §4).

## 1. Método e critérios da Onda 1

- **Fonte de cada cenário:** item(ns) exato(s) do TR (via [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/01 - Matriz de atores e relações|Seções do TR (índice: Matriz de atores e relações)]]), cruzado com a entidade/relação correspondente já registrada no modelo-alvo ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04]]) e, quando aplicável, o canal candidato da matriz ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/05 - Matriz de fornecimento dos dados|05]]). Nenhuma relação ou dado foi inventado para esta proposta — tudo cita a nota-fonte.
- **Critério de seleção:** valor de sanidade (caminho crítico, usado por muitos outros cenários, ou que expõe uma lacuna de automação já conhecida) **e** rastreabilidade direta ao TR — nunca a existência prévia de um CT/automação isoladamente. Quando um cenário já tem CT(s) reaproveitável(is) nas fatias aprovadas, isso é registrado como evidência adicional, não como critério de entrada.
- **Cobertura representativa, não total:** os 20 cenários cobrem pelo menos um caminho crítico de cada grupo C1–C6 do modelo-alvo, priorizando onde há (a) maior dependência de outros cenários, ou (b) lacuna de automação já documentada em 04/05 que vale expor cedo. Isso **não** significa cobertura do TR inteiro — grandes áreas ficam fora desta onda (ver §4).
- **Formato:** cada cenário é um bloco, não uma tabela larga — segue a mesma lição de legibilidade já aplicada aos diagramas da nota 04 (tabelas/diagramas muito largos cortam conteúdo na leitura).
- **Campos de cada cenário:** ID provisório · Objetivo de sanidade · Referência exata do TR · Ator/fluxo · Dados/estados/dependências (04/05) · Evidência/fonte · Razão para entrar na Onda 1 · Dúvidas/limites.

## 2. Tabela de orientação

| ID | Cenário | Grupo | TR (ref. principal) |
|---|---|---|---|
| ONDA1-01 | Login de Servidor com CPF+senha | C1 | 1.24, 1.24.1, 1.25 |
| ONDA1-02 | Bloqueio de conta após 5 tentativas | C1 | 1.25.1 |
| ONDA1-03 | Mudança de estado da identidade funcional | C1 | 1.25.3–1.25.3.4 |
| ONDA1-04 | Vínculo N:N Servidor↔Setor e tramitação por setor | C1 | 1.26.5, 1.26.11–1.26.11.3 |
| ONDA1-05 | Assunto/Serviço com categoria-base herdada do Módulo | C2 | 1.28.1, 1.29.1 |
| ONDA1-06 | Regras de tramitação por categoria e módulo | C2 | 1.29 |
| ONDA1-07 | Consulta pública de Zona e Categoria de uso | C2 | 1.29.10.2, 1.29.10.4 |
| ONDA1-08 | Abertura de Processo urbanístico a partir de Zona | C2 | 1.29.10.4.g–j |
| ONDA1-09 | Documento a partir de Modelo simples com herança | C3 | 1.31.1, 1.31.1.1 |
| ONDA1-10 | Tramitação por Fluxo com despacho e assinatura obrigatória | C3 | 1.30.1, 1.30.2 |
| ONDA1-11 | Mesa de trabalho: resumo e alternância de setor | C3 | 1.33.1–1.33.2.1 |
| ONDA1-12 | Organização por Etiqueta pessoal/compartilhada | C3 | 1.34.1 |
| ONDA1-13 | Cadastro de Contato externo com confirmação por e-mail | C4 | 1.32, 1.32.1 |
| ONDA1-14 | Central de atendimento: acesso a Serviço | C4 | 1.36 |
| ONDA1-15 | Ambiente virtual do Usuário externo e Demanda | C4 | 1.37 |
| ONDA1-16 | Divulgação: mural interno vs. canal externo/Jornal Oficial | C5 | 1.38.1, 1.38.3.1 |
| ONDA1-17 | Assinatura sequencial com signatários internos/externos | C5 | 1.40.3 |
| ONDA1-18 | Criação delegada de documento via Chave de acesso | C5 | 1.41.1, 1.41.2 |
| ONDA1-19 | Edição de identidade visual do órgão | C6 | 1.42.1.b, 1.42.1.c |
| ONDA1-20 | Indicadores de Servidores agrupados por status e nível | C6 | 1.43.5 |

## 3. Os 20 cenários candidatos

#### ONDA1-01 — Login de Servidor Público com CPF e senha
- **Objetivo de sanidade:** confirmar que um Servidor Público autentica-se com CPF (obrigatório) + senha e que o sistema valida as credenciais contra o cadastro.
- **Referência exata do TR:** 1.24 (regra geral de login por tipo de usuário), 1.24.1 (ator Servidor Público), 1.25 (validação de credenciais).
- **Ator/fluxo:** Servidor Público informa CPF + senha; sistema valida contra o cadastro.
- **Dados/estados/dependências (04/05):** Conta de usuário e Servidor ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 §3]]); canal da Conta de usuário ainda indefinido entre `.env` por QA e pool do seed ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/05 - Matriz de fornecimento dos dados|05 §2]]).
- **Evidência/fonte:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/Seções do TR/02 - Autenticação e ciclo de vida da identidade (1.24–1.25)|recorte 02]]; fatia 02 (`BASELINE.agents`).
- **Razão para entrar na Onda 1:** pré-requisito de praticamente todo outro cenário de sanidade — caminho crítico básico.
- **Dúvidas/limites:** nenhuma lacuna relevante identificada para este cenário específico; mapeamento campo a campo de qual conta vem de `.env` vs. pool do seed segue não decidido em 05.

#### ONDA1-02 — Bloqueio de conta após 5 tentativas malsucedidas
- **Objetivo de sanidade:** confirmar que 5 tentativas de login malsucedidas bloqueiam a conta.
- **Referência exata do TR:** 1.25.1.
- **Ator/fluxo:** qualquer ator autenticável (Servidor, Cidadão, Empresa) tentando login com credenciais inválidas repetidamente.
- **Dados/estados/dependências (04/05):** Conta de usuário ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 §3]]).
- **Evidência/fonte:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/Seções do TR/02 - Autenticação e ciclo de vida da identidade (1.24–1.25)|recorte 02]] (1.25.1); 04 §3 e 05 §2 registram que o mecanismo "só existe em branch Cypress não mesclada".
- **Razão para entrar na Onda 1:** requisito de segurança explícito do TR, com lacuna de automação já conhecida — vale expor cedo, não por já ter CT pronto (não tem, no `main` Playwright).
- **Dúvidas/limites:** mecanismo não confirmado no baseline Playwright `main` — gap de automação, não indício de ausência no produto (herdado de 04/05).

#### ONDA1-03 — Mudança de estado da identidade funcional com quarentena de permissões
- **Objetivo de sanidade:** confirmar que os estados Ativo/Licença/Férias/Inativo aplicam o nível de restrição de permissões descrito pelo TR.
- **Referência exata do TR:** 1.25.3–1.25.3.4 (estados Ativo, Licença, Férias, Inativo).
- **Ator/fluxo:** Servidor cujo estado funcional muda; sistema aplica/restringe permissões conforme o novo estado.
- **Dados/estados/dependências (04/05):** Servidor (b) — status funcional ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 §3]]); canal "ainda indefinido" em 05 §2.
- **Evidência/fonte:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/Seções do TR/02 - Autenticação e ciclo de vida da identidade (1.24–1.25)|recorte 02]] (1.25.3–1.25.3.4); 04/05 (mecanismo só em branch Cypress não mesclada).
- **Razão para entrar na Onda 1:** requisito central de controle de acesso dinâmico, caminho crítico de segurança, com lacuna de automação já documentada.
- **Dúvidas/limites:** o TR usa o rótulo "Inativo"; o contexto de produto confirmado por Rafael mapeia esse estado para "Suspenso" no cadastro atual — nomenclatura dupla já registrada em 04/05, não resolvida por este cenário.

#### ONDA1-04 — Vínculo N:N Servidor↔Setor com regras de tramitação herdadas
- **Objetivo de sanidade:** confirmar que um Servidor pode estar vinculado a mais de um Setor e que cada Setor aplica suas próprias regras de tramitação.
- **Referência exata do TR:** 1.26.5 (atribuição de usuários por setor), 1.26.11–1.26.11.3 (regras de tramitação por setor).
- **Ator/fluxo:** Servidor vinculado a um ou mais Setores/Subsetores; tramitação segue a regra do setor responsável.
- **Dados/estados/dependências (04/05):** Setor/Subsetor e Servidor, relação N:N ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 §3]]; também [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/00 - Mapa geral|00 - Mapa geral]]); Setor/Subsetor como seed persistente ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/05 - Matriz de fornecimento dos dados|05 §2]]).
- **Evidência/fonte:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/Seções do TR/03 - Estrutura organizacional e cadastro de servidores (1.26–1.27)|recorte 03]] (1.26.5, 1.26.11); fatia 02 (`BASELINE.sectors`/`subsectors`).
- **Razão para entrar na Onda 1:** base organizacional de quase toda tramitação; a relação N:N já é um ponto confirmado e auditado do modelo (ver histórico de correção Servidor↔Setor em 00/04).
- **Dúvidas/limites:** "Regras de Tramitação" é fonte reconstruída de diagrama de produto, ainda não validada em teste (herdada de 04).

#### ONDA1-05 — Assunto/Serviço com categoria-base herdada do Módulo
- **Objetivo de sanidade:** confirmar que um Assunto/Serviço criado sob um Módulo herda corretamente a categoria-base (DO/CO/PA) desse módulo.
- **Referência exata do TR:** 1.28.1 (campos mínimos do serviço/assunto), 1.29.1 (3 categorias-base).
- **Ator/fluxo:** Servidor com permissão cria Assunto/Serviço vinculado a um Módulo já existente.
- **Dados/estados/dependências (04/05):** Módulo, Assunto/Serviço, categoria-base ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 §4, Diagrama 2]]); Módulo como seed persistente ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/05 - Matriz de fornecimento dos dados|05 §2]]).
- **Evidência/fonte:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/Seções do TR/04 - Serviços, assuntos e categorias de documentos (1.28–1.29)|recorte 04]] (1.28.1, 1.29.1); fatia 03 (`BASELINE.services`, `makeModule`).
- **Razão para entrar na Onda 1:** núcleo do grupo C2, caminho crítico para qualquer cenário de documento/processo.
- **Dúvidas/limites:** demais tipos de campo personalizado além dos já confirmados seguem sem evidência (04 §4).

#### ONDA1-06 — Regras de tramitação pré-estabelecidas por categoria de documento e módulo
- **Objetivo de sanidade:** confirmar que regras de tramitação pré-estabelecidas variam conforme a categoria de documento e o módulo envolvidos.
- **Referência exata do TR:** 1.29 (texto introdutório — "regras de tramitação pré-estabelecidas por categoria e módulo").
- **Ator/fluxo:** sistema aplica regra de tramitação conforme a combinação categoria×módulo de um documento criado.
- **Dados/estados/dependências (04/05):** Categoria de documento, Módulo, Regras de tramitação (nós `CategoriaDoc`/`Modulo`/`RegrasTramitacao` em [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/00 - Mapa geral|00 - Mapa geral §C2]]).
- **Evidência/fonte:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/Seções do TR/04 - Serviços, assuntos e categorias de documentos (1.28–1.29)|recorte 04]] (texto literal do item 1.29).
- **Razão para entrar na Onda 1:** relação explicitamente citada no texto literal do TR, cruzando duas entidades centrais (categoria e módulo).
- **Dúvidas/limites:** nenhuma evidência de código localizada especificamente para essa regra combinada (herdada do Mapa geral — nó adicionado por citação literal do TR, sem evidência de código própria).

#### ONDA1-07 — Consulta pública de Zona publicada e Categoria de uso associada
- **Objetivo de sanidade:** confirmar que um ator externo (Cidadão/Empresa) consegue consultar uma Zona publicada e suas Categorias de uso associadas.
- **Referência exata do TR:** 1.29.10.2 (ferramenta acessível a cidadãos/empresas), 1.29.10.4 (entidades Zona e Categoria de uso, estado de publicação).
- **Ator/fluxo:** Cidadão/Empresa consulta Zona publicada e vê Categorias de uso associadas.
- **Dados/estados/dependências (04/05):** Zona, Categoria de uso ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 §4, Diagrama 3]]); 05 marca ambos como "nenhuma evidência de código/teste localizada".
- **Evidência/fonte:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/Seções do TR/04 - Serviços, assuntos e categorias de documentos (1.28–1.29)|recorte 04 §Zoneamento]] (1.29.10.2, 1.29.10.4).
- **Razão para entrar na Onda 1:** funcionalidade pública explícita do TR, sem nenhuma automação/evidência hoje — alto valor de sanidade justamente por expor essa lacuna cedo.
- **Dúvidas/limites:** nenhuma evidência de código/teste localizada para Zona/Categoria de uso; vínculo entre módulo PA e Zona permanece não confirmado por nenhuma fonte (aresta `D1`, tracejada, em 04).

#### ONDA1-08 — Abertura de Processo urbanístico a partir de Zona e revisão de Anexo
- **Objetivo de sanidade:** confirmar que um Cidadão/Empresa consegue iniciar um Processo urbanístico a partir de uma Zona publicada, e que um Servidor com permissão revisa o Anexo desse processo.
- **Referência exata do TR:** 1.29.10.4.g (consulta), 1.29.10.4.h (abertura de processo a partir da Zona), 1.29.10.4.i–j (revisão/aprovação/reprovação de Anexo).
- **Ator/fluxo:** Cidadão/Empresa inicia processo a partir de Zona; Servidor com permissão revisa/aprova/reprova o Anexo.
- **Dados/estados/dependências (04/05):** tratado em [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 §4]] como ação de cenário sobre a entidade Documento/Processo já modelada em §5 — não entidade persistente nova.
- **Evidência/fonte:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/Seções do TR/04 - Serviços, assuntos e categorias de documentos (1.28–1.29)|recorte 04 §Zoneamento]] (1.29.10.4.g–j).
- **Razão para entrar na Onda 1:** fluxo de ponta a ponta entre ator externo e Servidor revisor — caminho crítico que conecta C2 (zoneamento) a C3 (documento).
- **Dúvidas/limites:** estado de revisão do Anexo (revisado/aprovado/reprovado) não tem localização em código confirmada nesta análise.

#### ONDA1-09 — Criação de documento a partir de Modelo simples com herança de dados
- **Objetivo de sanidade:** confirmar que um documento criado a partir de um Modelo simples com herança preenche automaticamente os campos vinculados.
- **Referência exata do TR:** 1.31.1 (Modelo simples), 1.31.1.1 (herança de dados sim/não).
- **Ator/fluxo:** Servidor seleciona Modelo simples compatível com a categoria/serviço/assunto; sistema preenche campos herdados.
- **Dados/estados/dependências (04/05):** Modelo simples/Documento automatizado, Documento/Processo ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 §5]]).
- **Evidência/fonte:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/Seções do TR/05 - Fluxos de trabalho e modelos de documentos (1.30–1.31)|recorte 05]] (1.31.1, 1.31.1.1); fatia 04.
- **Razão para entrar na Onda 1:** caminho crítico de criação de documento, cobre a distinção herança sim/não (b.i/b.ii) já citada pelo TR.
- **Dúvidas/limites:** histórico de alterações do modelo (1.31.1.2) e a distinção exata Modelo simples × Documento automatizado seguem como achado a aprofundar (04 §5).

#### ONDA1-10 — Tramitação por Fluxo de trabalho com despacho customizado e assinatura obrigatória
- **Objetivo de sanidade:** confirmar que uma Etapa de Fluxo pode exigir despacho customizado e assinatura obrigatória antes de avançar.
- **Referência exata do TR:** 1.30.1 (configurações de Etapa e Fluxo), 1.30.2 (despacho customizado e assinatura obrigatória).
- **Ator/fluxo:** Documento tramita por Etapa de um Fluxo configurado; avanço bloqueado até despacho/assinatura serem concluídos.
- **Dados/estados/dependências (04/05):** Fluxo de trabalho/Etapa, Documento/Processo ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 §5]]); Fluxo marcado como "opcional/contratado" (Ambiente Cliente → Fluxo, tabela cruzada de 04).
- **Evidência/fonte:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/Seções do TR/05 - Fluxos de trabalho e modelos de documentos (1.30–1.31)|recorte 05]] (1.30.1–1.30.2); fatia 04.
- **Razão para entrar na Onda 1:** caminho crítico de fluxo configurável, distinto do caminho "mesa fora do fluxo" (lacuna (c) do Mapa geral) — vale cobrir os dois caminhos separadamente em ondas.
- **Dúvidas/limites:** regras de transição de etapa (1.30.3 — retrocesso de uma única etapa com justificativa, checklist de requisitos) não verificadas nesta análise.

#### ONDA1-11 — Mesa de trabalho: resumo de demandas e alternância entre setores
- **Objetivo de sanidade:** confirmar que, ao acessar a Mesa de trabalho, o Servidor vê um resumo de demandas e consegue alternar entre os setores aos quais está vinculado.
- **Referência exata do TR:** 1.33.1 (alternância de setor), 1.33.2–1.33.2.1 (resumo de demandas na tela inicial).
- **Ator/fluxo:** Servidor acessa a Mesa; vê resumo (em aberto/em tramitação/concluído/assinaturas pendentes/vencendo); alterna o setor ativo.
- **Dados/estados/dependências (04/05):** Mesa de trabalho, vínculo Servidor↔Setor ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 §5]]).
- **Evidência/fonte:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)|recorte 07]] (1.33.1–1.33.2.1); fatia 06.
- **Razão para entrar na Onda 1:** tela inicial do Servidor, caminho crítico de uso diário e pré-requisito de visibilidade de outros cenários de tramitação.
- **Dúvidas/limites:** estado da Mesa como entidade própria (status in aberto/elaboração/tramitação/pausado/encerrado) ainda sem prova técnica de enum no código (04 §5).

#### ONDA1-12 — Organização de documentos na mesa por Etiqueta pessoal/compartilhada
- **Objetivo de sanidade:** confirmar que documentos podem receber Etiquetas pessoais (visíveis só ao servidor) e compartilhadas (entre setores).
- **Referência exata do TR:** 1.34.1 (tipos de etiqueta: pessoal e compartilhada).
- **Ator/fluxo:** Servidor cria/aplica Etiqueta pessoal ou compartilhada a um Documento na Mesa.
- **Dados/estados/dependências (04/05):** Etiqueta ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 §5]]).
- **Evidência/fonte:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)|recorte 07]] (1.34.1); fatia 07 (CT A19, `LABEL_ID=1`, "Urgente").
- **Razão para entrar na Onda 1:** funcionalidade de organização citada explicitamente pelo TR, com CT já existente potencialmente reaproveitável — mas a entrada na onda é pelo valor de sanidade da funcionalidade, não pelo CT.
- **Dúvidas/limites:** o CT A19 usa um rótulo pré-existente assumido (dependência observada do teste, não criado por `provision.ts`) — não tratar esse ID fixo nem a existência prévia como requisito do modelo-alvo (herdado de 04 §5).

#### ONDA1-13 — Cadastro de Contato externo (PF/PJ) com e-mail de confirmação
- **Objetivo de sanidade:** confirmar que um novo Contato externo (Cidadão PF ou Empresa PJ) recebe e-mail de confirmação ao ser cadastrado.
- **Referência exata do TR:** 1.32 (cadastro único de contato externo), 1.32.1 (e-mail de confirmação).
- **Ator/fluxo:** Cidadão/Empresa se cadastra como Contato externo; sistema envia e-mail de confirmação.
- **Dados/estados/dependências (04/05):** Contato externo PF/PJ = Usuário externo ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 §6]]).
- **Evidência/fonte:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/Seções do TR/06 - Atores externos e atendimento ao cidadão (1.32, 1.36–1.37)|recorte 06]] (1.32, 1.32.1); fatia 05.
- **Razão para entrar na Onda 1:** porta de entrada do ator externo, pré-requisito de todo cenário do grupo C4.
- **Dúvidas/limites:** cadastro único/auto-registro de Pessoa Física não encontrado no código consultado (04 §6).

#### ONDA1-14 — Central de atendimento: acesso a Serviço via canais digitais do órgão
- **Objetivo de sanidade:** confirmar que cidadãos, empresas e entes externos acessam Serviços oferecidos pelo órgão através da Central de atendimento.
- **Referência exata do TR:** 1.36 (Central de atendimento disponibilizada via canais digitais do órgão).
- **Ator/fluxo:** Cidadão/Empresa/Ente externo acessa a Central e consegue ver/acessar um Serviço oferecido pelo órgão.
- **Dados/estados/dependências (04/05):** Central de atendimento / Canal Oficial, Assunto/Serviço ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 §6]]).
- **Evidência/fonte:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/Seções do TR/06 - Atores externos e atendimento ao cidadão (1.32, 1.36–1.37)|recorte 06]] (1.36); fatia 05.
- **Razão para entrar na Onda 1:** funcionalidade explícita do TR que conecta atores externos a Serviço — caminho crítico de entrada para o cidadão.
- **Dúvidas/limites:** mecanismo exato dos "canais digitais do órgão" não detalhado pelo TR; vínculo exato com a entidade Serviço do recorte 04 não detalhado neste item (ambos A confirmar, recorte 06).

#### ONDA1-15 — Ambiente virtual do Usuário externo: abertura e acompanhamento de Demanda
- **Objetivo de sanidade:** confirmar que um Usuário externo abre uma Demanda e consegue acompanhá-la (notificações, andamento) em seu ambiente virtual próprio.
- **Referência exata do TR:** 1.37 (ambiente virtual próprio do usuário externo; abertura/acompanhamento de demandas).
- **Ator/fluxo:** Usuário externo abre Demanda; recebe notificações; acompanha andamento.
- **Dados/estados/dependências (04/05):** Demanda externa, Contato/Usuário externo ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 §6]]).
- **Evidência/fonte:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/Seções do TR/06 - Atores externos e atendimento ao cidadão (1.32, 1.36–1.37)|recorte 06]] (1.37); fatia 05 (`makeExternalDocument`/`generateExternalDocument`).
- **Razão para entrar na Onda 1:** caminho crítico de ponta a ponta do cidadão, da abertura ao acompanhamento da sua própria solicitação.
- **Dúvidas/limites:** se Demanda é entidade própria ou um Documento/Processo comum de origem externa segue como inferência aberta da fatia 05, não confirmada (04 §6).

#### ONDA1-16 — Divulgação de Documento: mural interno vs. canal externo/Jornal Oficial
- **Objetivo de sanidade:** confirmar que um Documento divulgado aparece no mural interno (servidores) e, quando configurado para canal externo, fica acessível ao público no Jornal Oficial.
- **Referência exata do TR:** 1.38.1 (tipos de divulgação: mural interno / canal oficial externo), 1.38.3.1 (acesso público ao jornal oficial, com busca e filtros).
- **Ator/fluxo:** Documento é divulgado; Servidor vê no mural interno; Cidadão acessa via Jornal Oficial (interface pública).
- **Dados/estados/dependências (04/05):** Parâmetro de divulgação, Mural interno, Canal externo, Jornal Oficial ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 §7]]).
- **Evidência/fonte:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/Seções do TR/08 - Divulgação, exportação e assinaturas (1.38–1.40)|recorte 08]] (1.38.1, 1.38.3.1); [[../../../../../04 Conhecimento/Módulos/Divulgar Documento|Divulgar Documento]] (produto).
- **Razão para entrar na Onda 1:** funcionalidade com dois canais de destino distintos, caminho crítico de transparência pública exigida pelo TR.
- **Dúvidas/limites:** acesso público sem login é documentado no produto, mas sem evidência de teste automatizado localizada (04 §7).

#### ONDA1-17 — Solicitação de assinatura sequencial com signatários internos/externos
- **Objetivo de sanidade:** confirmar que uma solicitação de assinatura sequencial respeita a ordem definida, bloqueia até a vez de cada signatário, e aceita signatários internos (servidores) e externos (cidadãos).
- **Referência exata do TR:** 1.40.3 (solicitação de assinaturas, assinaturas sequenciais, seleção de signatários internos/externos, locais de assinatura no documento).
- **Ator/fluxo:** Servidor solicita assinatura sequencial a signatários internos e/ou externos; cada um assina na ordem definida.
- **Dados/estados/dependências (04/05):** Assinatura, Solicitação de assinatura/Signatário ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 §7]]).
- **Evidência/fonte:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/Seções do TR/08 - Divulgação, exportação e assinaturas (1.38–1.40)|recorte 08]] (1.40.3); fatia 17 (CTs A30-C01–C08, `makeSignRequest`/`executeSignatures`).
- **Razão para entrar na Onda 1:** fluxo de maior complexidade de regras do grupo C5 (ordem sequencial, bloqueio até a vez), com CTs já existentes que podem ser reaproveitados como evidência adicional — não como critério de seleção.
- **Dúvidas/limites:** "contribuinte" como ator distinto do Signatário externo não tem evidência de código (04 §7). **Fora deste cenário:** recusa de assinatura (simples ou em cascata) é o item TR 1.40.5, distinto de 1.40.3 — não misturada aqui; fica candidata a cenário próprio em onda futura.

#### ONDA1-18 — Criação delegada de documento via Chave de acesso
- **Objetivo de sanidade:** confirmar que um servidor convenente usa uma Chave de acesso concedida por outro servidor para criar um documento dentro do limite de uso definido, e que o concedente é notificado.
- **Referência exata do TR:** 1.41.1 (criação/gerenciamento de chaves, limite de uso, encerramento automático), 1.41.2 (uso da chave para gerar documento, notificação ao concedente).
- **Ator/fluxo:** Servidor convenente usa Chave de acesso (em vez de permissão própria) para criar documento; Servidor concedente é notificado.
- **Dados/estados/dependências (04/05):** Chave de acesso, Servidor (concedente/convenente) ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 §7]]).
- **Evidência/fonte:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/Seções do TR/09 - Chaves de acesso e criação delegada (1.41)|recorte 09]] (1.41.1–1.41.2); fatia 18 (aprovada — não reaberta aqui).
- **Razão para entrar na Onda 1:** mecanismo de delegação com regras de segurança explícitas (limite de uso, encerramento automático, rastreabilidade) — caminho crítico do grupo C5.
- **Dúvidas/limites:** o fluxo para quando o servidor tem só permissão própria (sem chave) para o tipo de documento não é especificado pelo TR neste item (1.41.2.c, recorte 09) — A confirmar.

#### ONDA1-19 — Edição de identidade visual do órgão exigindo nível Administrador
- **Objetivo de sanidade:** confirmar que a edição de cores temáticas e imagens institucionais do órgão exige nível de acesso Administrador.
- **Referência exata do TR:** 1.42.1.b (edição de cores temáticas), 1.42.1.c (upload/gerenciamento de imagens institucionais).
- **Ator/fluxo:** Servidor com nível Administrador edita cores/imagens da Personalização do Órgão.
- **Dados/estados/dependências (04/05):** Personalização/identidade visual ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 §8]]).
- **Evidência/fonte:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/Seções do TR/10 - Personalização e identidade visual do órgão (1.42)|recorte 10]] (1.42.1.b–c).
- **Razão para entrar na Onda 1:** funcionalidade de personalização citada explicitamente pelo TR, exigindo nível específico — bom caso representativo de permissão positiva/negativa.
- **Dúvidas/limites:** o modo de acesso às informações cadastrais do órgão (1.42.1.a — visualização apenas ou também edição) segue A confirmar (recorte 10); o ator exato autorizado à área de personalização como um todo não é especificado pelo TR.

#### ONDA1-20 — Consulta de indicadores de Servidores agrupados por status e por nível de permissão
- **Objetivo de sanidade:** confirmar que o painel de Estatísticas exibe, para os servidores cadastrados, os indicadores de total ativos/inativos e os agrupamentos por status e por nível de permissão descritos pelo TR.
- **Referência exata do TR:** 1.43.5 (dados detalhados de servidores: total ativos/inativos; servidores por status; servidores por nível de permissão).
- **Ator/fluxo:** Administrador/usuário autorizado consulta o painel de Estatísticas de Servidores e visualiza os indicadores já agrupados por status e por nível de permissão — exibição/consulta; o TR 1.43.5 não confirma a existência de um filtro interativo de tela neste subitem, por isso nenhum filtro é incluído no cenário.
- **Dados/estados/dependências (04/05):** Estatísticas/Relatórios ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 §8]]).
- **Evidência/fonte:** [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/Seções do TR/11 - Estatísticas e indicadores (1.43)|recorte 11]] (1.43.5); classificação Ativos/Inativos confirmada por Rafael (04 §8, recorte 03).
- **Razão para entrar na Onda 1:** fecha a cobertura representativa com o grupo C6, caminho crítico de relatórios gerenciais citado explicitamente pelo TR.
- **Dúvidas/limites:** cálculo/implementação do indicador não verificado; correspondência entre "administradores e usuários autorizados" (termo do TR) e os 5 níveis canônicos segue A confirmar (recorte 11); se existir filtro interativo de tela para status/nível, isso não está confirmado por nenhuma fonte revisada neste subitem — não presumir sem evidência adicional.

## 4. Cobertura e exclusões desta onda

Esta onda cobre pelo menos um caminho crítico de cada grupo C1–C6, mas **não** cobre o TR inteiro. Ficam fora, candidatos a ondas futuras:

- **Infraestrutura técnica e operacional (1.1–1.23)** — [[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/Seções do TR/01 - Infraestrutura técnica e operacional (1.1–1.23)|recorte 01]], não tocado nesta onda.
- **Exportação de documentos (1.39)** — exportação em PDF, árvore completa, formatos PAdES ([[../../SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/Seções do TR/08 - Divulgação, exportação e assinaturas (1.38–1.40)|recorte 08]]).
- **Tipos de assinatura e requisitos técnicos (1.40.1–1.40.2.1)** — eletrônica simples/avançada/qualificada; a onda 1 cobre só a solicitação sequencial (1.40.3).
- **Gerenciamento/edição de solicitações de assinatura já criadas (1.40.4–1.40.4.1)**.
- **Demais filtros/buscas da Mesa (1.33.4–1.33.6)** além do resumo inicial e alternância de setor.
- **Status do Documento/Processo nos 5 valores do TR, de ponta a ponta (1.35)** — a onda 1 toca Documento via outros cenários (ONDA1-09, 10), mas não testa a transição completa entre os 5 estados.
- **Suspensão/reativação de Setor (1.26.4, 1.26.6–1.26.8)**.
- **Acesso às informações cadastrais do órgão (1.42.1.a)** — só a identidade visual (1.42.1.b–c) entrou nesta onda.
- **Demais categorias de documento (Memorando, Circular, Ofício — 1.29.2–1.29.9)** — a onda 1 cobre só a categoria-base e o caso de Zoneamento.

Nenhum desses itens foi descartado — ficam registrados aqui como candidatos explícitos para a Onda 2 (ou além), quando Rafael priorizar.

## 5. Proposta de conteúdo para o Notion

> Proposta apenas — nenhuma página foi criada, publicada ou transferida. Não há conector de escrita para o Notion disponível nesta sessão; mesmo que houvesse, a criação/transferência depende de decisão do Rafael e da conversa com Alice (ver §6).

> **Diretriz do Rafael (15/10/2026):** o TR é a referência normativa do que o produto deve atender. A documentação publicada precisa trazer **conteúdo funcional real, rastreável e organizado** — sem metadados do vault ou do processo de QA (nomes de arquivo internos, commits, "aprovado por Rafael/Codex", datas de revisão). Esta seção foi reescrita para refletir essa diretriz; nada foi criado, publicado ou transferido.

### 5.1 Fonte normativa

O PDF original do Termo de Referência continua sendo a **única fonte normativa**. A página no Notion referencia esse PDF diretamente (ex.: link estável para onde a equipe já o acessa) — nunca o substitui nem o parafraseia como se a paráfrase fosse o requisito.

### 5.2 Transcrição integral do TR como índice navegável

A peça central da página é uma **transcrição fiel e completa** do texto do TR (itens 1.1–1.43), estruturada pelos **IDs e páginas originais do próprio PDF** — não pela segmentação em 11 recortes usada internamente pelo QA. Cada item (ex.: 1.1, 1.24.1, 1.29.10.4) vira uma âncora navegável da transcrição, com a página correspondente do PDF registrada junto. É essa transcrição que a equipe lê como referência funcional; a segmentação em recortes continua existindo só como ferramenta de trabalho da análise, dentro do vault.

### 5.3 Como o conteúdo derivado se conecta à transcrição

Cada achado funcional (atores, entidades, relações, dados/estados) referencia o **item/âncora da transcrição** correspondente e, quando útil, aponta também **diretamente à página do PDF original**. A direção da referência é sempre transcrição/PDF → achado — nunca o inverso: a transcrição e o conteúdo publicado não citam o vault, suas notas ou sua estrutura de pastas.

### 5.4 Conteúdo funcional derivado — sem metadados de processo

Para cada área do TR, a página apresenta:

- **Atores/entidades envolvidos.**
- **Relações entre eles.**
- **Comportamento esperado do produto**, redigido como requisito funcional — não como "o que um modelo interno de QA registrou".
- **Dados/estados necessários** para esse comportamento.

Este conteúdo **não expõe**: o vault ou sua estrutura de pastas; nomes de arquivo internos (ex. "Mapa geral", "Modelo-alvo dos dados do preset"); commits, datas de revisão de QA, ou frases como "aprovado por Rafael/Codex". A redação deve ler como documentação funcional de produto, não como relatório de auditoria de QA.

### 5.5 Status de atendimento do produto — só com evidência funcional suficiente

A página só pode declarar que o produto **"atende"** a um item do TR quando houver evidência funcional suficiente (ex.: teste automatizado reproduzível, observação direta confirmada do produto). **Análise conceitual não equivale a atendimento** — um item estar identificado/modelado (entidade ou relação reconhecida) não é prova de que o produto o implementa. Nesses casos, o status publicado deve ser **"não verificado"** ou **"parcial"**, sempre citando a fonte que sustenta essa classificação — sem citar o vault como fonte na página; internamente, essa fonte pode ser uma fatia aprovada, um recorte do TR ou uma lacuna já registrada.

**Explicitamente fora desta proposta de conteúdo:**

- As 17 fatias de evidência técnica (artefato interno de QA sobre a automação atual, `Especificações do preset piloto/`) não entram na página, integral ou resumida — elas sustentam, só internamente, a classificação de status descrita em §5.5, sem aparecer citadas na página publicada.
- Anotações pessoais de QA, dúvidas em aberto e material arquivado (`Arquivo/Abordagem anterior/`) não entram na página.
- A preparação técnica do preset (passo 11) e os CTs formais não foram feitos e não devem ser descritos como prontos ou em andamento na página.

## 6. Pendências e próximos passos

- **Aprovação da Onda 1:** esta lista de 20 cenários é uma proposta — segue pendente de aprovação específica do Rafael antes de qualquer CT, automação ou execução.
- **Conversa com Alice (ação pendente, não realizada):** reservar uma página no Notion para a documentação listada em §5. Esta nota não contatou Alice, não criou página e não transferiu/publicou conteúdo — apenas identifica a dependência e o conteúdo candidato a levar a essa conversa. Responsável, prazo e processo de manutenção da página seguem indefinidos (lacuna já registrada no diagnóstico).
- **Ondas futuras:** após avaliação da Onda 1, propor a Onda 2 cobrindo os itens listados em §4, mantendo o mesmo método e os mesmos campos por cenário.
- **Passo 11 da SGV-12082:** permanece trilha futura e separada — nenhum cenário desta onda exigiu, até aqui, uma decisão de arquitetura ainda não tomada para ser avaliado.
