---
tags: [qa]
task: SGV-12082
pai: SGV-11262
tipo: secao-tr
itens_tr: "1.24–1.25"
paginas_pdf: "p. 1–2"
status: aprovado
---
# 02 - Autenticação e ciclo de vida da identidade (itens 1.24–1.25)

> [!info]- Navegação
> **Matriz/índice:** [[../01 - Matriz de atores e relações|Matriz de atores e relações]] · **Demanda:** [[../../00 QA/01 - Demanda]] · **Plano de análise:** [[../../00 QA/02 - Plano de análise]] · **Mapa geral:** [[../00 - Mapa geral]]

> [!info] Escopo deste recorte — revisado e aprovado pelo Codex em 08/10/2026
> Itens do TR: **1.24–1.25**, cobertos em nível de subitem (1.24.1–1.24.3; 1.25.1–1.25.3.4). Páginas do PDF: **1.24–1.24.2 na p. 1; 1.24.3 em diante na p. 2** de [[../../Fontes/Termo de Referência SOGOV.pdf|Termo de Referência SOGOV.pdf]] (fonte de autoridade). Lido diretamente por render de página, não por extração textual. **O material arquivado da SGV-11971 não foi usado como evidência** — cobre os mesmos itens sob outra ótica (automação/CTs), mas não é fonte para este modelo conceitual.

## Cobertura dos itens

| Item do TR | Situação | Justificativa ou pendência |
|---|---|---|
| 1.24 | Mapeado | Regra geral: login por tipo de usuário, cada acesso vinculado a um único CPF ou CNPJ. |
| 1.24.1 | Mapeado | Ator "Servidor Público" — autenticação por CPF (obrigatório) + senha. |
| 1.24.2 | Mapeado | Ator "Cidadão (Pessoa Física)" — autenticação por CPF (obrigatório) + senha. |
| 1.24.3 | Mapeado | Ator "Empresas e outras entidades (Pessoa Jurídica)" — autenticação por CNPJ (obrigatório) + senha. |
| 1.25 | Mapeado | Validação de CPF/CNPJ + senha contra o cadastro do usuário. |
| 1.25.1 | Mapeado | Regra de acesso: 5 tentativas malsucedidas → conta bloqueada. |
| 1.25.2 | Não aplicável | Mensagem de erro clara quando credenciais não reconhecidas — requisito de UX, não define ator/entidade/estado. |
| 1.25.3 | Mapeado | Introduz "controle de acesso dinâmico baseado no ciclo de vida da identidade funcional" — 4 estados nos subitens a seguir. |
| 1.25.3.1 | Mapeado | Estado **Ativo** — conjunto completo de permissões/privilégios, acesso irrestrito conforme perfil. |
| 1.25.3.2 | Mapeado | Estado **Licença** — quarentena de privilégios: acesso restrito a funcionalidades não transacionais, sem modificação/aprovação. |
| 1.25.3.3 | Mapeado | Estado **Férias** — mesma quarentena da Licença; suspende permissões de escrita e execução de fluxos de trabalho. |
| 1.25.3.4 | Mapeado | Estado **Inativo** — negação explícita (explicit deny) de qualquer autenticação. |

**Resultado do recorte:** 12/12 itens (incluindo subitens) considerados; 11 Mapeados, 1 Não aplicável (1.25.2 — UX). Nenhum item pendente.

## Elementos identificados

| Referência do TR | Elemento | Tipo | Papel/descrição | Dados ou atributos relevantes | Certeza/evidência |
|---|---|---|---|---|---|
| 1.24.1 | Servidor Público | Ator | Tipo de usuário autenticável | CPF (identificador, obrigatório), senha | Confirmado |
| 1.24.2 | Cidadão (Pessoa Física) | Ator | Tipo de usuário autenticável | CPF (identificador, obrigatório), senha | Confirmado |
| 1.24.3 | Empresas e outras entidades (Pessoa Jurídica) | Ator | Tipo de usuário autenticável | CNPJ (identificador, obrigatório), senha | Confirmado |
| 1.24 | Identificador único de acesso | Dado/atributo | Vincula cada acesso a um único CPF ou CNPJ | CPF ou CNPJ | Confirmado |
| 1.25.1 | Bloqueio por tentativas | Configuração/regra | Bloqueia a conta após tentativas malsucedidas | Limite de tentativas malsucedidas: 5 | Confirmado |
| 1.25.3.1 | Estado Ativo | Estado | Acesso irrestrito, conjunto completo de permissões | — | Confirmado |
| 1.25.3.2 | Estado Licença | Estado | Quarentena de privilégios; restringe a funcionalidades não transacionais; sem modificação/aprovação | — | Confirmado |
| 1.25.3.3 | Estado Férias | Estado | Mesma quarentena da Licença; sem escrita/execução de fluxo de trabalho | — | Confirmado |
| 1.25.3.4 | Estado Inativo | Estado | Negação explícita de autenticação | — | Confirmado |

## Relações/dependências identificadas

| Origem | Relação/dependência | Destino | Referência do TR | Certeza/evidência ou pendência |
|---|---|---|---|---|
| Servidor Público | autentica com | CPF + senha | 1.24.1 | Confirmado |
| Cidadão (Pessoa Física) | autentica com | CPF + senha | 1.24.2 | Confirmado |
| Empresas/outras entidades (Pessoa Jurídica) | autentica com | CNPJ + senha | 1.24.3 | Confirmado |
| Usuário/identidade com status funcional | tem estado | {Ativo, Licença, Férias, Inativo} | 1.25.3 | Estados/consequências confirmados; aplicabilidade às categorias de usuário a confirmar (ver dúvida abaixo) |
| Estado funcional | determina | conjunto de permissões/acesso | 1.25.3.1–1.25.3.4 | Confirmado |
| 5 tentativas malsucedidas | aciona | bloqueio da conta | 1.25.1 | Confirmado como regra; **relação com os 4 estados do ciclo de vida não é explícita no texto** — ver dúvida abaixo |

## Dúvidas/ambiguidades e contexto complementar

O TR continua sendo a fonte para os requisitos contratuais. As respostas abaixo vêm de documentação funcional do SOGOV e ajudam a entender o contexto atual; não alteram o que está explícito ou ausente no TR.

| Questão que o TR não resolve | Contexto documentado fora do TR | Fonte e limite da evidência |
|---|---|---|
| A quem se aplicam os estados funcionais de 1.25.3? | A documentação do Login descreve status do servidor: **Em Atividade**, Licença, Férias e Inativo. servidores em Licença ou Férias mantêm acesso total ao ambiente cidadão; Inativo bloqueia o workspace, mas o usuário pode acessar outros workspaces ou o ambiente cidadão. | [[QA Workspace/04 Conhecimento/Módulos/Login|Módulo Login]] (importado do Notion; documentação funcional, não validação feita nesta análise). Há uma diferença a preservar: o TR usa **Ativo** e diz que **Inativo** nega qualquer autenticação (1.25.3.4), enquanto a documentação do Login delimita o bloqueio ao workspace. O contexto não resolve o escopo contratual nem confirma o comportamento em execução. |
| O bloqueio por tentativas é um quinto estado ou mecanismo separado? | A especificação de Gestão de Desbloqueio trata “Bloqueado” separadamente do status de origem e prevê restaurar o status anterior após o desbloqueio. | [[QA Workspace/04 Conhecimento/Módulos/Gestão de Desbloqueio de Acessos|Gestão de Desbloqueio de Acessos]]. A própria nota informa que a funcionalidade está em especificação e ainda não foi testada; portanto, isso não confirma o comportamento em produção. |
| Como o bloqueio é revertido? | A especificação prevê que, ao concluir o fluxo de redefinição de senha — manual ou sistêmico —, o usuário seja removido da lista de bloqueios e retorne ao status anterior. | [[QA Workspace/04 Conhecimento/Módulos/Gestão de Desbloqueio de Acessos#Fluxo de desbloqueio e sincronização|Fluxo de desbloqueio e sincronização]]. Regra documentada, ainda não validada em execução. O TR não descreve esse procedimento. |

## Fontes/evidências

- PDF: `Fontes/Termo de Referência SOGOV.pdf` — itens 1.24, 1.24.1, 1.24.2 na p. 1; itens 1.24.3, 1.25, 1.25.1, 1.25.2, 1.25.3, 1.25.3.1–1.25.3.4 na p. 2. Lido por render de página, conferido diretamente nesta sessão em 08/10/2026. Material arquivado da SGV-11971 **não** foi consultado como evidência.
