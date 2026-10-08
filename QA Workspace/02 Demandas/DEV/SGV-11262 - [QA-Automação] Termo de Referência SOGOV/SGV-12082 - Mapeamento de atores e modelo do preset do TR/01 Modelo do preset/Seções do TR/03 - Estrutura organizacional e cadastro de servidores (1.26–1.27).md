---
tags: [qa]
task: SGV-12082
pai: SGV-11262
tipo: secao-tr
itens_tr: "1.26–1.27"
paginas_pdf: "p. 2–7"
status: aprovado
---
# 03 - Estrutura organizacional e cadastro de servidores (itens 1.26–1.27)

> [!info]- Navegação
> **Matriz/índice:** [[../01 - Matriz de atores e relações|Matriz de atores e relações]] · **Demanda:** [[../../00 QA/01 - Demanda]] · **Plano de análise:** [[../../00 QA/02 - Plano de análise]] · **Mapa geral:** [[../00 - Mapa geral]]

> [!info] Escopo deste recorte — revisado e aprovado pelo Codex em 08/10/2026
> Itens do TR: **1.26–1.27**, cobertos recursivamente em todos os subitens numerados que o PDF apresenta (79 linhas na Cobertura — 18 sob 1.26, 61 sob 1.27). Lido diretamente por render de página, não por extração textual. **Material arquivado não foi usado como evidência.** Mapa de páginas: 1.26–1.26.11.1 (p. 2); 1.26.11.2–1.27.6 (p. 3); 1.27.6.1–1.27.9.3(intro) (p. 4); 1.27.9.3(lista)–1.27.9.4.6 (p. 5); 1.27.10–1.27.11.1(início) (p. 6); 1.27.11.1(fim)–1.27.11.6.1 (p. 7). Listas com letras (a, b, c...) dentro de um item numerado são conteúdo desse item, não subitens próprios do TR — não viram linhas separadas na Cobertura.

## Cobertura dos itens

| Item do TR | Situação | Justificativa ou pendência |
|---|---|---|
| 1.26 | Mapeado | Organograma: plataforma estrutura o órgão em setores/subsetores, com representação hierárquica. |
| 1.26.1 | Mapeado | Cadastro de setores, atribuição de usuários e tramitação de documentos com base na hierarquia. |
| 1.26.2 | Não aplicável | Visualização em árvore (tree view) interativa — requisito de interface. |
| 1.26.3 | Não aplicável | Arquitetura sem limite de quantidade de setores/subsetores — requisito de capacidade/escalabilidade. |
| 1.26.4 | Mapeado | Edição/gerenciamento de setores; adição e suspensão de setores. |
| 1.26.5 | Mapeado | Visualização e atribuição/remoção de usuários por setor/subsetor. |
| 1.26.6 | Mapeado | Suspensão temporária de setor/subsetor impede tramitação de documentos enquanto durar. |
| 1.26.7 | Mapeado | Verificação de pendências (documentos, fluxos, usuários atribuídos) antes de permitir suspensão. |
| 1.26.8 | Mapeado | Reativação de setor suspenso restabelece funcionalidades/documentos associados. |
| 1.26.9 | Não aplicável | Estatística agregada (total de setores e de usuários alocados), não elemento de ator/entidade. |
| 1.26.10 | Mapeado | Renomear setor/subsetor preserva o nome antigo em documentos já tramitados. |
| 1.26.11 | Mapeado | Cada setor pode ter regras próprias de tramitação por categoria de documento, configuráveis por usuário com permissão. |
| 1.26.11.1 | Mapeado | Regra de tramitação: criar documentos. |
| 1.26.11.2 | Mapeado | Regra de tramitação: receber e tramitar documentos. |
| 1.26.11.3 | Mapeado | Regra de tramitação: interagir com o cidadão (casos com interação externa). |
| 1.26.11.4 | Mapeado | Regra de tramitação: visualização de dados sigilosos. |
| 1.26.11.5 | Mapeado | Regra de tramitação: recebimento automático de documentos. |
| 1.26.12 | Mapeado | Setor/subsetor pode ser reparentado para outra hierarquia; subsetores são arrastados junto. |
| 1.27 | Mapeado | Cadastro/gerenciamento do quadro de servidores; vínculo a setor(es), com nível de permissão específico por setor vinculado. |
| 1.27.1 | Mapeado | Cadastro controlado por fluxo de convite, pré-cadastro e homologação. |
| 1.27.2 | Mapeado | Introduz os 5 níveis de usuário exigidos (nomes nos subitens a seguir). |
| 1.27.2.1 | Mapeado | Nível "Administrador". |
| 1.27.2.2 | Mapeado | Nível "Administrador setorial". |
| 1.27.2.3 | Mapeado | Nível "Assistente administrativo". |
| 1.27.2.4 | Mapeado | Nível "Auxiliar administrativo". |
| 1.27.2.5 | Mapeado | Nível "Visualizador". |
| 1.27.3 | Mapeado | Nível Administrador: acesso master a todas as funcionalidades/configurações. |
| 1.27.4 | Mapeado | Permissões do nível Administrador setorial, detalhadas nos subitens a seguir. |
| 1.27.4.1 | Mapeado | Administrador setorial no organograma: visualizar tudo; cadastrar/editar/suspender setores e vincular/desvincular servidores, restrito à hierarquia do próprio setor. |
| 1.27.4.2 | Mapeado | Administrador setorial em servidores: visualizar todos; cadastrar, restrito à hierarquia do próprio setor. |
| 1.27.4.3 | Mapeado | Administrador setorial em contatos externos: visualizar e cadastrar (PF/PJ). |
| 1.27.4.4 | Mapeado | Administrador setorial em assuntos/serviços: visualizar, cadastrar, editar, inativar (dos módulos disponíveis). |
| 1.27.5 | Mapeado | Assistente administrativo: mesmas 4 áreas do Administrador setorial, mas mais restrito — ver 1.27.5.1–1.27.5.4. |
| 1.27.5.1 | Mapeado | No organograma: visualizar tudo; cadastrar/editar setores (sem suspender); vincular/desvincular servidores — restrito ao próprio setor. |
| 1.27.5.2 | Mapeado | Em servidores: visualizar todos; cadastrar/editar/suspender — restrito ao próprio setor. |
| 1.27.5.3 | Mapeado | Em contatos externos: visualizar e cadastrar (PF/PJ) — igual ao Administrador setorial. |
| 1.27.5.4 | Mapeado | Em assuntos/serviços: só visualizar (sem cadastrar/editar/inativar). |
| 1.27.6 | Mapeado | Auxiliar administrativo: só 3 áreas (sem assuntos/serviços) — ver 1.27.6.1–1.27.6.3. |
| 1.27.6.1 | Mapeado | No organograma: só visualizar. |
| 1.27.6.2 | Mapeado | Em servidores: só visualizar. |
| 1.27.6.3 | Mapeado | Em contatos externos: visualizar e cadastrar (PF/PJ). |
| 1.27.7 | Mapeado | Visualizador: nível só-leitura — ver 1.27.7.1–1.27.7.4. |
| 1.27.7.1 | Mapeado | No organograma: só visualizar. |
| 1.27.7.2 | Mapeado | Em servidores: só visualizar. |
| 1.27.7.3 | Mapeado | Em contatos externos: só visualizar (sem cadastrar). |
| 1.27.7.4 | Mapeado | Na tramitação: pode acessar, mas sem poder interagir diretamente nos documentos dos setores dos quais faz parte. |
| 1.27.8 | Mapeado | Permissões extras, concedidas individualmente no cadastro/edição por um administrador — associadas/complementares às permissões já existentes no nível; independência não especificada pelo texto. |
| 1.27.8.1 | Mapeado | Concessão de permissão extra exige servidor administrador ou nível com permissão para isso. |
| 1.27.8.2 | Mapeado | Lista de 24 permissões extras possíveis (setores/subsetores, servidores, pré-cadastros, assuntos/serviços, acesso a mesas de outros setores, fluxos de trabalho). |
| 1.27.9 | Mapeado | Cadastro simplificado: ao menos 2 meios (interno e externo). |
| 1.27.9.1 | Mapeado | Cadastro interno: usuário com permissão cadastra; servidor recebe e-mail de confirmação de vínculo. |
| 1.27.9.2 | Mapeado | Cadastro externo em massa: link direto por setor, pré-cadastro sujeito a aprovação de administrador. |
| 1.27.9.3 | Mapeado | Dados exigidos no cadastro interno: CPF (validado por API, não editável), e-mail, matrícula (se houver), setor(es)+nível, permissões extras (se houver). |
| 1.27.9.3.2 | Mapeado | E-mail de confirmação enviado ao novo servidor. |
| 1.27.9.3.3 | Mapeado | Pré-cadastro pendente: pode ser excluído (perde a possibilidade de conclusão), reenviado, ou editado (exceto CPF). |
| 1.27.9.3.4 | Mapeado | Dados que o próprio novo servidor insere na conclusão: CPF de confirmação (deve bater com o do pré-cadastro), assinatura textual, cargo de contrato, senha (critérios de força), aceite de termos. |
| 1.27.9.3.5 | Mapeado | Após o preenchimento, redireciona para login com as permissões atribuídas. |
| 1.27.9.4 | Mapeado | Cadastro externo: link gerado para um setor específico, enviado a um ou mais servidores. |
| 1.27.9.4.1 | Mapeado | Cadastro via link passa por aprovação de usuário com permissão. |
| 1.27.9.4.2 | Mapeado | Dados exigidos no cadastro externo: CPF (via API), e-mail, data de nascimento, sexo, telefone, assinatura textual, cargo de contrato, matrícula, cargo no setor do link, senha (só forte), aceite de termos. |
| 1.27.9.4.3 | Mapeado | Servidor pode indicar, no mesmo fluxo, outros setores dos quais também faz parte. |
| 1.27.9.4.4 | Mapeado | Pré-cadastro externo fica exibido internamente numa área específica. |
| 1.27.9.4.5 | Mapeado | Na aprovação, usuário com permissão define o nível e setor(es); pode recusar com justificativa enviada por e-mail. |
| 1.27.9.4.6 | Mapeado | Após aprovação, servidor recebe e-mail com link de login. |
| 1.27.10 | Mapeado | Área de listagem de todos os servidores cadastrados. |
| 1.27.10.1 | Mapeado | Dados mínimos na listagem: nome, cargo, setor principal, e-mail, status (5 valores — ver dúvida sobre estados abaixo). |
| 1.27.10.2 | Não aplicável | Estatística agregada (total de servidores; total de ativos). |
| 1.27.10.3 | Mapeado | Dados detalhados (sem edição): nome, cargo de contrato, status, assinatura textual, CPF (parcialmente protegido por LGPD), e-mail, matrícula, dados de aprovação do pré-cadastro, setor principal (nível+cargo), setores adicionais (nível+cargo cada). |
| 1.27.10.4 | Não aplicável | Busca por palavra-chave e filtros (interface de listagem) — valores de filtro já cobertos em 1.27.10.1. |
| 1.27.10.4.2 | Não aplicável | Uso combinado de filtro e busca — interface. |
| 1.27.11 | Mapeado | Edição de cadastros e pré-cadastros de servidores. |
| 1.27.11.1 | Mapeado | Editáveis: assinatura textual, e-mail institucional, matrícula, setor principal (nível/cargo), setores adicionais (adicionar/remover, nível/cargo), permissões extras. |
| 1.27.11.2 | Mapeado | Status de atividade editável (4 valores — ver dúvida sobre estados abaixo). |
| 1.27.11.3 | Mapeado | Troca livre entre status, exigindo data de início e fim do novo status. |
| 1.27.11.4 | Mapeado | A partir do período definido, e-mail informa a mudança; acesso é limitado/restabelecido automaticamente nas datas definidas. |
| 1.27.11.5 | Mapeado | Dados pessoais na tela de edição, com regra de quem pode editar — ver 1.27.11.5.1. |
| 1.27.11.5.1 | Mapeado | CPF (não editável por ninguém); nome (não editável, vem da API); telefone, sexo e data de nascimento (editáveis só pelo próprio servidor). |
| 1.27.11.6 | Mapeado | Pré-cadastros internos/externos têm área própria de gerenciamento. |
| 1.27.11.6.1 | Mapeado | Pré-cadastros externos podem ser aprovados/reprovados; reprovação exige justificativa. |

**Resultado do recorte:** 79/79 itens (incluindo subitens numerados) considerados; 72 Mapeados, 7 Não aplicáveis (interface/usabilidade ou estatística agregada — 1.26.2, 1.26.3, 1.26.9, 1.27.10.2, 1.27.10.4, 1.27.10.4.2). Nenhum item pendente de leitura.

## Elementos identificados

| Referência do TR | Elemento | Tipo | Papel/descrição | Dados ou atributos relevantes | Certeza/evidência |
|---|---|---|---|---|---|
| 1.26, 1.26.12 | Setor/Subsetor | Entidade | Unidade organizacional hierárquica, reparentável entre hierarquias | nome (versionado — nome antigo preservado em documentos já tramitados), hierarquia (pai/filho), status (suspensão/reativação — 1.26.4, 1.26.6–1.26.8) | Confirmado que existem as ações de suspender/reativar; **Inferido** que isso se modele como enum nomeado "ativo/suspenso" — o TR não usa a palavra "ativo" para setor, só "suspenso" e "reativação/restabelecer" |
| 1.26.11 | Regra de tramitação por categoria de documento | Configuração | Por setor, configurável por categoria (Circulares, Ofícios, Processos administrativos): criar, receber/tramitar, interagir com cidadão, ver dados sigilosos, receber automaticamente | categoria de documento, setor | Confirmado |
| 1.27 | Servidor | Ator/Entidade | Tipo de usuário cadastrado, vinculado a um ou mais setores | CPF (identificador, não editável), nome completo (obtido por consulta a API a partir do CPF, não editável), e-mail, matrícula, cargo de contrato (único, do servidor), assinatura textual, telefone, sexo, data de nascimento (3 últimos editáveis só pelo próprio) | Confirmado |
| 1.27 | Vínculo Servidor–Setor | Relação com atributo | Servidor pode ter múltiplos setores; cada vínculo tem seu próprio nível e cargo | setor, nível, **cargo exercido no setor (distinto do cargo de contrato do servidor)** | Confirmado — 1.27.9.3.4 distingue explicitamente "cargo de contrato" (c) de "cargo exercido em cada setor ao qual foi vinculado" (d) |
| 1.27.2.1–1.27.2.5 | Nível de acesso | Configuração (enum) | 5 valores: Administrador, Administrador setorial, Assistente administrativo, Auxiliar administrativo, Visualizador — nomes exatamente como no TR, sem comparação com nomenclatura de produto | nível | Confirmado |
| 1.27.8 | Permissão extra | Configuração (enum, 24 valores) | Concedida individualmente, **em associação/complemento às permissões já existentes no nível do servidor** (independência do nível não é especificada pelo texto) — cobre setores/subsetores, servidores, pré-cadastros, assuntos/serviços, acesso a mesas de outros setores, fluxos de trabalho. Lista completa na subseção abaixo | lista de 24 flags (1.27.8.2) | Confirmado |
| 1.27.1, 1.27.9.1–1.27.9.4.6 | Pré-cadastro | Entidade/estado | Registro pendente de homologação, por 2 fluxos distintos (interno e externo via link), com conjuntos de dados exigidos diferentes entre si; resultado aprovado ou recusado | CPF, e-mail + (interno: matrícula, setor, nível, permissões extras) + (externo: data de nascimento, sexo, telefone, cargo de contrato, cargo no setor do link) + **estado (aprovado/recusado)** + **justificativa (obrigatória em caso de recusa, enviada por e-mail ao solicitante — 1.27.9.4.5)** + **para cadastro via link do organograma: responsável pela aprovação e data/hora da aprovação (1.27.10.3.h)** | Confirmado — **assimetria de dados entre os dois fluxos é achado literal do texto, não inferência** |
| 1.27.10.1 | Status exibido na listagem | Configuração (enum, 5 valores) | Ativo; Inativo ("offline" — sem sessão ativa no momento; exibe também a data/hora da última vez em que esteve ativo); Suspenso; Licença; Férias | status, **data/hora da última atividade (quando Inativo/offline)** | Confirmado — ver dúvida sobre consistência com outros status abaixo |
| 1.27.11.2 | Status de atividade editável | Configuração (enum, 4 valores) | Em atividade; Suspenso; Licença; Férias | status, data de início, data de fim | Confirmado — ver dúvida sobre consistência com outros status abaixo |

### Permissões extras (1.27.8.2) — lista completa

| Letra (TR) | Permissão extra | Domínio |
|---|---|---|
| a | Cadastrar setores e subsetores no organograma | Organograma |
| b | Editar setores e subsetores no organograma | Organograma |
| c | Suspender setores e subsetores no organograma | Organograma |
| d | Atribuir usuários aos setores e subsetores no organograma | Organograma |
| e | Desvincular usuários de setores e subsetores no organograma | Organograma |
| f | Ajustar regras de tramitação dos setores na atuação em módulos, serviços e assuntos | Regras de tramitação |
| g | Cadastrar servidores | Servidores |
| h | Editar servidores | Servidores |
| i | Atualizar situação de atividade dos servidores | Servidores |
| j | Visualizar pré-cadastros | Pré-cadastros |
| k | Validar pré-cadastros | Pré-cadastros |
| l | Excluir pré-cadastros | Pré-cadastros |
| m | Cadastrar contatos externos | Contatos externos |
| n | Editar contatos externos | Contatos externos |
| o | Cadastrar categorias e subcategorias de assuntos e serviços | Assuntos e serviços |
| p | Cadastrar assuntos e serviços | Assuntos e serviços |
| q | Editar assuntos e serviços | Assuntos e serviços |
| r | Inativar assuntos e serviços | Assuntos e serviços |
| s | Dar acesso a mesas de outros setores, sem permissão de interação | Mesas de outros setores |
| t | Visualizar fluxos de trabalho | Fluxos de trabalho |
| u | Cadastrar fluxos de trabalho | Fluxos de trabalho |
| v | Ativar e inativar fluxos de trabalho | Fluxos de trabalho |
| w | Editar fluxos de trabalho, incluindo excluí-lo | Fluxos de trabalho |
| x | Duplicar fluxos de trabalho | Fluxos de trabalho |

> 24/24 permissões extras de 1.27.8.2, sem omissão. Agrupamento por domínio é só organizacional — o TR não nomeia esses grupos.

## Relações/dependências identificadas

| Origem | Relação/dependência | Destino | Referência do TR | Certeza/evidência ou pendência |
|---|---|---|---|---|
| Servidor | vinculado a (N:N, com nível/cargo por vínculo) | Setor | 1.27, 1.26.5 | Confirmado — 1.26.5 permite vários usuários por setor e 1.27 permite um servidor vinculado a múltiplos setores |
| Setor | hierarquia de | Subsetor (reparentável) | 1.26, 1.26.12 | Confirmado |
| Setor suspenso | bloqueia | tramitação de documentos no setor | 1.26.6 | Confirmado |
| Suspensão de setor | depende de | ausência de pendências (documentos/fluxos/usuários) | 1.26.7 | Confirmado |
| Nível de acesso | determina | escopo de permissões nas 4 áreas (organograma/servidores/contatos externos/assuntos-serviços) | 1.27.3–1.27.7.4 | Confirmado — escopo de alguns níveis é restrito à hierarquia do próprio setor (1.27.4–1.27.6), não à organização inteira |
| Permissão extra | complementa/associa-se a | nível de acesso | 1.27.8 | Confirmado que complementa; **independência do nível não é especificada** pelo texto |
| Status de atividade (edição) | tem transição com | data de início/fim obrigatórias | 1.27.11.2, 1.27.11.3 | Confirmado |
| Status de atividade (edição) | aciona automaticamente, nas datas definidas | limitação/restabelecimento de acesso | 1.27.11.4 | Confirmado |
| Status exibido na listagem (1.27.10.1) | — | Status de atividade editável (1.27.11.2) | 1.27.10.1, 1.27.11.2 | **A confirmar — ver dúvida**: os dois conjuntos de valores não coincidem (5 vs. 4 valores; "Ativo" vs. "Em atividade"; "Inativo" presente só no primeiro) |
| Status de atividade (1.27.x) | — | Estados do ciclo de vida da identidade funcional (1.25.3, recorte 2) | 1.27.10.1, 1.27.11.2, 1.25.3 | **A confirmar — ver dúvida**: "Inativo" tem dois sentidos diferentes no TR |

## Dúvidas/ambiguidades

- **Três enumerações de status não coincidem.** (a) 1.25.3 (ciclo de vida da identidade funcional, recorte 2): Ativo, Licença, Férias, Inativo (desprovisionamento lógico, vínculo encerrado). (b) 1.27.10.1 (status exibido na listagem de servidores): Ativo, **Inativo** ("offline" — sem sessão ativa no momento, sentido de presença, não de desprovisionamento), Suspenso, Licença, Férias. (c) 1.27.11.2 (status editável do servidor): Em atividade, Suspenso, Licença, Férias (sem "Inativo"). A palavra **"Inativo" tem dois sentidos diferentes dentro do próprio TR** — (a)/(desprovisionamento) e (b)/(presença/offline) — e a lista editável (c) nem inclui a palavra. O texto não afirma se são a mesma máquina de estados vista de três ângulos, ou mecanismos distintos. **A confirmar — não unifiquei por conta própria.**
- **Permissões do nível Auxiliar administrativo (1.27.6) não listam a área "Assuntos e serviços"**, presente nos níveis Administrador setorial (1.27.4.4) e Assistente administrativo (1.27.5.4). O texto não esclarece se é omissão do documento ou ausência deliberada de permissão nessa área para esse nível. **A confirmar.**
- **Reversão do bloqueio por tentativas (achado do recorte 2)** permanece sem resposta neste recorte — 1.27.11.2/1.27.11.3 descrevem transição de status por data, não por desbloqueio de tentativas malsucedidas; não há indicação de que sejam o mesmo mecanismo.

## Fontes/evidências

- PDF: `Fontes/Termo de Referência SOGOV.pdf`, p. 2–7 (ver mapa de páginas no Escopo acima). Lido por render de página, conferido diretamente nesta sessão em 08/10/2026. Material arquivado **não** foi consultado como evidência.
