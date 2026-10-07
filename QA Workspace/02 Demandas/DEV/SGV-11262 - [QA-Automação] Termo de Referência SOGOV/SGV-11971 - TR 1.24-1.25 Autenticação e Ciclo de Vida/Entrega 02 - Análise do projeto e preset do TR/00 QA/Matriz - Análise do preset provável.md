---
tags: [qa, automacao, dados, matriz]
task: SGV-12082
pai: SGV-11971
tipo: matriz-analise
status: em levantamento
---
# Matriz — análise do preset provável para o TR

> [!info] Propósito
> Esta matriz vai da regra/caso aos dados e ao mecanismo atual de preparação. Ela deve orientar a recomendação do preset inicial; não é um catálogo geral do SOGOV nem uma especificação aprovada de seed.
>
> **Fonte funcional:** [[../../Arquivo/00 QA/03 - Casos de teste|38 CTs da SGV-11971]] · **Demanda:** [[01 - Demanda]] · **Plano:** [[02 - Plano de teste]] · **Roadmap:** [[../../../Roadmap - Automação TR|Automação TR]]

## Como preencher

- Use uma linha por CT quando as pré-condições ou dados diferirem; agrupe apenas quando ator, estado e preparação forem iguais.
- Para cada afirmação, registre a fonte (caso, arquivo, configuração ou execução existente).
- Use **Confirmado**, **Inferido** ou **A confirmar**. Não transforme lacuna em fato.
- Não copiar valores secretos. Registre apenas nomes de variáveis/chaves e onde a configuração deve ser verificada.

## Legenda de estado do conhecimento

| Estado | Significado |
|---|---|
| Confirmado | Visível diretamente no CT/código/documento ou em execução já registrada |
| Inferido | Interpretação provável que ainda precisa de validação |
| A confirmar | Evidência ausente, ambiente inacessível ou comportamento não verificado |

## Matriz de cobertura do TR completo

Esta visão cobre os requisitos do PDF (1.1–1.43). As linhas agrupam requisitos correlatos para orientar a investigação; subitens específicos devem ser desmembrados quando tiverem cobertura, dados ou evidências diferentes. **Os 38 CTs atuais cobrem os itens 1.24–1.25 apenas.**

> [!success] Verificação contra o PDF de origem (07/10/2026)
> **Fonte:** `Downloads/SGV-12082/Requisitos Sogov.pdf` (20 páginas, itens 1.1 a 1.43 — é mais completo que o PDF usado em 31/08/2026 pra conferir o ciclo 1.24-1.25, que ia só até o item 1.26). Lido por inteiro e conferido item a item contra a tabela abaixo: os intervalos descritos em cada linha (1.1–1.23, 1.26 a 1.43) batem com o conteúdo real do PDF — nenhuma linha precisou ser corrigida na descrição de escopo.
>
> **Confirmado, palavra por palavra**: os itens 1.24, 1.25 (incluindo 1.25.1 a 1.25.3.4), 1.27.10.1 e 1.27.11.2/1.27.11.4 batem exatamente com o texto citado em C1–C16 do [[../../Arquivo/00 QA/01 - Demanda|01 - Demanda da SGV-11971]] — a checagem de 31/08 se confirma também nesta versão mais completa do documento.
>
> **⚠️ Discrepância encontrada — níveis de permissão (CT-020):** o item **1.27.2** do PDF lista **5 níveis oficiais**: `1.27.2.1 Administrador`, `1.27.2.2 Administrador setorial`, `1.27.2.3 Assistente administrativo`, `1.27.2.4 Auxiliar administrativo`, `1.27.2.5 Visualizador` — com permissões detalhadas por nível em 1.27.3 a 1.27.8. Isso **não bate** com a decisão de produto registrada no `01 - Demanda` da SGV-11971 pra CT-020: *"Os níveis de permissão corretos são Especialista / Usuário básico / Somente leitura — confirmado em 4 fontes (i18n, migration, docs de business-rules e nota do vault)"*. São nomes e quantidades diferentes (5 vs. 3), não uma variação de redação. Antes de qualquer preset tocar em nível de permissão de servidor, vale confirmar com o Rafael qual das duas é a fonte válida hoje — pode ser que o Termo tenha sido atualizado depois de 18/08, ou que exista um mapeamento produto↔Termo não documentado ainda (ex.: Administrador+Administrador setorial → "Especialista").

| Itens do TR | Área/requisito | Automação/evidência atual a localizar | Massa/preset a investigar | Situação |
|---|---|---|---|---|
| 1.1–1.23 | Infraestrutura, hospedagem, disponibilidade, banco de dados, rede, e-mail, segredos, segurança, armazenamento, filas, criptografia e monitoramento | Requisitos predominantemente técnicos/operacionais; confirmar se há testes no projeto e qual evidência os valida | Não presumir preset de dados; mapear dependências ambientais e evidência exigida | A confirmar |
| 1.24–1.25 | Autenticação e ciclo de vida da identidade funcional | 38 CTs existentes na SGV-11971; 13 localizados em Playwright (CT-001–012, CT-038); estado dos demais deve ser reconciliado | Seed global, fixtures/pools e credenciais do ambiente; detalhes no mapa atual do seed | Parcialmente conhecido; portabilidade entre ambientes não demonstrada |
| 1.26 | Organograma, setores/subsetores, suspensão, hierarquia e permissões de setor | Localizar cobertura existente; não assumir que os CTs de 1.24–1.25 cobrem este requisito | Seed declara setores/subsetores; dependência por teste e estado de execução a mapear | A confirmar |
| 1.27 | Cadastro de servidores, 5 níveis oficiais (Administrador/Administrador setorial/Assistente administrativo/Auxiliar administrativo/Visualizador — item 1.27.2, confirmado no PDF — **diverge do "Especialista/Usuário básico/Somente leitura" do CT-020, ver achado acima**), permissões extras, convites, listagem e ciclo de vida | Localizar testes e separar atores/papéis necessários; checar qual conjunto de nomes o produto real usa | Seed declara muitos servidores e perfis; relação com testes/TR a mapear | Requisito confirmado; automação/massa e qual nomenclatura vale seguem a confirmar |
| 1.28 | Gerenciamento de serviços/assuntos e campos configuráveis | Localizar testes que criam ou consomem serviços/assuntos | Seed declara serviços; dependências, configuração por ambiente e reuso a mapear | A confirmar |
| 1.29 | Categorias de documentos e módulos, formulários e zoneamento | Localizar suítes e dados dependentes por categoria | Seed declara módulos; determinar subconjunto realmente consumido | A confirmar |
| 1.30 | Fluxos de trabalho e etapas | Localizar testes e estados de workflow exigidos | Seed declara três workflows; mapear correspondência, estabilidade e reset | A confirmar |
| 1.31 | Modelos simples e automatizados de documentos | Localizar testes, modelos e documentos próprios do teste | Mapa atual aponta que o seed não fornece massa-base de documentos para os CTs de autenticação; demais suítes a investigar | A confirmar |
| 1.32 | Cadastro de contatos externos e notificação por e-mail | Localizar testes, identidade externa e requisitos de caixa de e-mail | Seed declara cidadãos; mapear contatos, e-mail e limitações de ambiente | A confirmar |
| 1.33 | Mesa de trabalho, filas, visões, alertas e busca | Localizar testes e massa de documentos/atribuições | Mapear dependências de setores, documentos, estados, datas e usuários | A confirmar |
| 1.34 | Etiquetas e aplicação/compartilhamento por setor | Localizar testes e relações com documentos/setores | A verificar no seed e nos dados criados pelos testes | A confirmar |
| 1.35 | Tramitação, histórico e estados de documentos/processos | Localizar testes, transições, prazos e limpeza | Mapear documentos, workflows, setores e atores; verificar isolamento e reset | A confirmar |
| 1.36–1.37 | Central de atendimento e acompanhamento por usuários externos | Localizar fluxos externos e identidades PF/PJ | Seed declara cidadãos; mapear cadastro, solicitações e massa entre ambientes | A confirmar |
| 1.38 | Divulgação/publicação de documentos (jornal/transparência) | Localizar testes, permissões, estado de publicação e documentos | A verificar no seed e nos dados próprios de cada teste | A confirmar |
| 1.39 | Exportação e impressão de documentos/processos | Localizar formatos, tamanho e dados documentais exigidos | Mapear documentos/árvore processual e dependências de armazenamento | A confirmar |
| 1.40 | Assinaturas eletrônicas/digitais e solicitações | Localizar atores, tipos, ordem e estado de assinatura | Seed lista perfis relacionados a assinatura; confirmar consumo, configuração e dependências externas | A confirmar |
| 1.41 | Chaves de acesso e criação delegada | Localizar permissões, limites, documentos e ciclo de vida da chave | Seed declara módulo accessKey e servidor dedicado; confirmar cobertura e massa exigida | A confirmar |
| 1.42 | Personalização e identidade visual do órgão | Localizar testes e dados de configuração do cliente | Provável configuração da instância; validar se automatizável e se pertence ao preset | A confirmar |
| 1.43 | Estatísticas de uso, setores, documentos, servidores e recursos | Localizar testes e massa agregada necessária aos cálculos | Mapear volume, variedade e consistência dos dados; avaliar se seed é apropriado | A confirmar |

## Detalhamento dos 38 CTs de 1.24–1.25

A tabela acima não substitui o mapeamento caso a caso. Para cada CT-001–CT-038, cruzar cenário/pré-condição com código Playwright/Cypress ou execução manual, identificando ator, identificador, status inicial, preparação, mutação/limpeza, credenciais/configuração e evidência. O estado prévio dos CTs deve ser revalidado; não inferir resultado atual a partir do placar histórico.

| CT | Requisito/subitem | Framework/teste localizado | Ator e estado | Dados consumidos/alterados | Preparação/limpeza | Ambiente e evidência | Situação |
|---|---|---|---|---|---|---|---|
| CT-001–CT-038 | 1.24–1.25 | A decompor caso a caso; 13 conhecidos em Playwright (CT-001–012 e CT-038) | A preencher pela fonte de cada caso | A preencher pela fonte de cada caso | A cruzar com seed, fixtures e setup manual/API | A confirmar por ambiente | Em levantamento |

> O resumo de 13 CTs é um ponto de partida conhecido; decompor em linhas individuais e agrupar apenas CTs com pré-condições e preparação equivalentes.

## Catálogo mínimo candidato

Preencher somente após cruzar os CTs com código e fontes de dados. Manter cada entrada ligada aos CTs que a exigem.

| Dado/estado candidato | CTs que justificam | Preparação existente | Reuso entre ambientes | Ação candidata | Evidência/pendência |
|---|---|---|---|---|---|
| Instância-alvo e configuração de endpoint | CTs que executam contra a instância | Perfil fixo no baseline; URLs fornecidas pelo ambiente | Não demonstrado para seleção de instância diferente | Avaliar parametrização segura com validação explícita do alvo | Confirmar ambientes e proteção contra criação acidental |
| Atores de servidor/cidadão e credenciais de teste | CTs de autenticação/estado | Pools por worker e credenciais ambientais no baseline Playwright | Reuso de atores no mesmo backend existe; entre ambientes a confirmar | Documentar pré-condições, ownership e reset por ambiente | Validar estado real e política de credenciais de teste |
| Estados de conta (bloqueio, licença, férias, inativo/suspenso) | CTs de 1.24–1.25 correspondentes após mapeamento individual | A verificar por CT | A confirmar | Determinar se são provisionados, alterados em teste ou preparados por API | Registrar operação inversa/limpeza e isolamento |
| Módulo/serviço/permissões | Requisitos e testes que comprovarem dependência | Seed declara catálogo mais amplo; consumo de cada CT a verificar | A confirmar | Incluir apenas dependências rastreadas | Cruzar passos/precondições e código dos testes |

## Decisões ao concluir

- **O que entra no preset:** apenas massa/estados necessários a requisitos que serão validados por automação; requisitos de infraestrutura ou operação devem apontar para evidência adequada.
- **Forma recomendada do preset:** a preencher com comparação fundamentada (perfil/configuração, seed reconciliador, preparação específica por suíte ou combinação).
- **Escopo mínimo inicial:** CTs, atores, entidades e estados que a matriz comprovar necessários.
- **Diferenças por ambiente:** endpoint, credenciais, disponibilidade de entidades, permissões e limpeza.
- **Riscos de isolamento e concorrência:** a preencher.
- **Primeiras entregas sugeridas:** a preencher com escopo pequeno, dependências e aceite próprio.
