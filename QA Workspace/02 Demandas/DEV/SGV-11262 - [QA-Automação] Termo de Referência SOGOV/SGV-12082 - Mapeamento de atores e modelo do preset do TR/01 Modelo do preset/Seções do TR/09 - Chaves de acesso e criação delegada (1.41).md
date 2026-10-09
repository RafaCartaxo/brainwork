---
tags: [qa]
task: SGV-12082
pai: SGV-11262
tipo: secao-tr
itens_tr: "1.41"
paginas_pdf: "p. 18–19"
status: aprovado
---
# 09 - Chaves de acesso e criação delegada (item 1.41)

> [!info]- Navegação
> **Matriz/índice:** [[../01 - Matriz de atores e relações|Matriz de atores e relações]] · **Demanda:** [[../../00 QA/01 - Demanda]] · **Plano de análise:** [[../../00 QA/02 - Plano de análise]] · **Mapa geral:** [[../00 - Mapa geral]]

> [!info] Escopo deste recorte — revisado e aprovado pelo Codex em 08/10/2026
> Item do TR: **1.41**, coberto recursivamente em todos os subitens numerados que o PDF apresenta (3 linhas na Cobertura: 1.41, 1.41.1, 1.41.2). Lido diretamente por render de página, não por extração textual. **Material arquivado não foi usado como evidência.** Mapa de páginas: 1.41–1.41.1.c.i (p. 18, após 1.40, que pertence ao recorte 08 e já foi analisado); 1.41.1.d–1.41.2.f (p. 19, antes de 1.42, que pertence ao recorte 10 e não foi analisado aqui). Listas com letras dentro de um item numerado são conteúdo desse item, não subitens próprios do TR — exceto onde o próprio TR numera. Contexto de produto já confirmado por Rafael: o item 1.41.1.a usa literalmente o nome de nível "Visualizador", um dos 5 nomes originais do TR já mapeados no recorte 03 para o modelo canônico ativo (Visualizador → Somente leitura) — aplicado aqui por ser uso direto da própria terminologia do TR, não uma inferência nova. Os demais itens de contexto confirmado por Rafael (status Ativo/Inativo, presença online/offline, regra de criação de Assuntos e Serviços) não aparecem de forma literal neste recorte e não foram aplicados. Nesta rodada, a análise usou exclusivamente o texto do TR — Conhecimento > Módulos não foi consultado para este recorte.

## Cobertura dos itens

| Item do TR | Situação | Justificativa ou pendência |
|---|---|---|
| 1.41 | Mapeado | Criação de chaves de acesso para delegação de tarefas administrativas: servidores autorizados podem criar documentos em nome de outros, conforme permissões previamente estabelecidas, sem comprometer credenciais de acesso, garantindo segurança e rastreabilidade. |
| 1.41.1 | Mapeado | Criação/gerenciamento de chaves: (a) qualquer nível de usuário pode criar chave, **exceto o nível "Visualizador"** (termo original do TR — canônico "Somente leitura", ver recorte 03); (b) ao criar, informar (conforme Arts. 12 e 14 da Lei 9.784/1999): servidor convenente (i), limite de uso — período e/ou quantidade de documentos (ii), tipos de documentos gerados pela chave (iii); (c) chave pode ser concedida a servidor de outro setor; ao atingir o limite de permissões estabelecido, a chave é automaticamente encerrada (c.i); (d) servidores visualizam as chaves que têm como concedente ou como convenente, com opções de filtro de listagem: Ativas, Encerradas, Agendadas; (e) cada chave mantém histórico de documentos gerados por ela, acessível tanto ao convenente quanto ao concedente. |
| 1.41.2 | Mapeado | Requisitos adicionais: (a) servidor com chave(s) vinculada(s) pode usar permissões pessoais (nível/setor) ou a chave concedida — sistema exibe tipos de documento disponíveis conforme o setor em que o servidor está operando e conforme possua acesso próprio e/ou chave; (b) se só tiver chave para um tipo de documento (sem permissão própria), vai direto para a criação via chave, sem seleção; (c) se tiver chave e permissão própria, é exibido aviso de seleção (criar em nome próprio ou via chave de outro servidor) — **o TR não especifica o fluxo quando o servidor tem apenas permissão própria (sem chave) para o tipo de documento**; (d) ao gerar documento via chave, o servidor que criou a chave recebe notificação e pode visualizar/acompanhar o documento gerado; (e) todo uso da chave é registrado para garantir rastreabilidade e controle de atividades; (f) chaves podem ser encerradas automaticamente ou manualmente, conforme regras definidas na criação ou por vontade de quem concedeu. |

**Resultado do recorte:** 3/3 itens (incluindo subitens numerados) considerados; 3 Mapeados, 0 Não aplicáveis. Nenhum item pendente de leitura — pendências de detalhe registradas em Dúvidas/ambiguidades abaixo.

## Elementos identificados

| Referência do TR | Elemento | Tipo | Papel/descrição | Dados ou atributos relevantes | Certeza/evidência |
|---|---|---|---|---|---|
| 1.41, 1.41.1, 1.41.2 | Chave de acesso | Entidade | Mecanismo de delegação: permite que um servidor (convenente) crie documentos em nome de outro (concedente), dentro de limites definidos, sem comprometer credenciais | servidor concedente; servidor convenente; limite de uso (período e/ou quantidade de documentos); tipos de documentos autorizados; setor do convenente (pode ser diferente do setor do concedente); categorias/opções de filtro de listagem (Ativas, Encerradas, Agendadas — ver linha "Chave de acesso" nas Relações sobre se são estados formais); histórico de documentos gerados por ela; encerramento (automático ao atingir o limite, ou manual) | Confirmado |
| 1.41.1.a | Nível de usuário habilitado a criar chave | Regra/configuração | Qualquer nível pode criar chave de acesso, exceto o nível "Visualizador" (TR) | termo original do TR já mapeado no recorte 03: Visualizador → canônico "Somente leitura" — logo, Administrador, Administrador Setorial, Especialista e Usuário básico podem criar chave; Somente leitura não pode | Confirmado — uso direto da terminologia original do TR, já mapeada por Rafael, sem inferência nova |
| 1.41.2.a–1.41.2.c | Documento (criado via permissão própria ou via chave) | Entidade/decisão | No momento de criar um documento, o sistema decide/pergunta se o servidor usa permissão própria ou chave de acesso, conforme o que ele possuir para aquele tipo de documento | sem opção própria (só chave) → cria direto via chave (1.41.2.b); ambas as opções (chave e permissão própria) → aviso de seleção (1.41.2.c); **só permissão própria (sem chave) → fluxo não especificado pelo TR neste item — A confirmar** | Confirmado quanto aos dois ramos explícitos (só chave; ambas as opções); ramo de só permissão própria — **A confirmar** |
| 1.41.2.d | Notificação ao concedente | Evento | Ao gerar documento via chave, o servidor que criou a chave (concedente) é notificado e pode visualizar/acompanhar o documento gerado | — | Confirmado |

## Relações/dependências identificadas

| Origem | Relação/dependência | Destino | Referência do TR | Certeza/evidência ou pendência |
|---|---|---|---|---|
| Servidor (concedente) | cria/concede | Chave de acesso | 1.41.1 | Confirmado |
| Chave de acesso | vinculada a | Servidor convenente | 1.41.1.b.i | Confirmado |
| Chave de acesso | tem | Limite de uso (período e/ou quantidade de documentos) | 1.41.1.b.ii | Confirmado |
| Chave de acesso | restrita a | Tipos de documento autorizados | 1.41.1.b.iii | Confirmado |
| Chave de acesso | pode ser concedida para servidor de | Setor diferente do setor do concedente | 1.41.1.c | Confirmado |
| Chave de acesso | tem opções de filtro de listagem (Ativas \| Encerradas \| Agendadas) — não declaradas como enum formal de status | 1.41.1.d | Confirmado que os filtros existem; formalização como estado/status da entidade — **A confirmar** |
| Chave de acesso | encerra automaticamente ao | atingir o limite de permissões estabelecido | 1.41.1.c.i | Confirmado |
| Chave de acesso | mantém | Histórico de documentos gerados por ela | 1.41.1.e | Confirmado |
| Servidor (concedente ou convenente) | acessa | Histórico da chave (documentos gerados por ela) | 1.41.1.e | Confirmado |
| Servidor (convenente) | usa | Chave de acesso ou Permissões pessoais (conforme nível/setor), para gerar documento | 1.41.2.a | Confirmado |
| Documento (gerado via chave) | gera notificação para | Servidor concedente | 1.41.2.d | Confirmado |
| Uso da Chave de acesso | é registrado para | rastreabilidade e controle de atividades | 1.41.2.e | Confirmado |
| Chave de acesso | pode ser encerrada | automaticamente (regra definida na criação) ou manualmente (por quem concedeu) | 1.41.2.f | Confirmado |
| Criação de Chave de acesso | permitida a | todos os níveis, exceto "Visualizador" (TR) — canônico "Somente leitura" (recorte 03) | 1.41.1.a | Confirmado |

## Dúvidas/ambiguidades

- **Histórico de documentos gerados pela chave (1.41.1.e) × Registro de uso da chave (1.41.2.e):** o TR descreve, em dois pontos diferentes, (i) um "histórico de documentos gerados" pela chave, acessível a convenente e concedente, e (ii) um registro de "todo uso da chave de acesso" para rastreabilidade/controle. Não fica explícito se são o mesmo registro (um histórico único que serve a ambos os propósitos) ou dois registros distintos (um específico de documentos gerados, outro mais amplo de todo uso, incluindo talvez tentativas ou outras ações). Não concluo por semelhança de contexto. **Pergunta objetiva para Rafael:** o histórico de documentos da chave (1.41.1.e) e o registro de uso para rastreabilidade (1.41.2.e) são a mesma estrutura de dados, ou dois registros distintos?

## Fontes/evidências

- PDF: `Fontes/Termo de Referência SOGOV.pdf`, p. 18–19 (ver mapa de páginas no Escopo acima). Lido por render de página, conferido diretamente nesta sessão em 08/10/2026. Material arquivado **não** foi consultado como evidência.
- Conhecimento > Módulos: não consultado nesta rodada (análise restrita ao texto do TR).
- Recorte 03 (`Seções do TR/03 - Estrutura organizacional e cadastro de servidores (1.26–1.27)`): mapeamento confirmado "Visualizador → Somente leitura", reutilizado aqui por citação direta do mesmo termo original do TR em 1.41.1.a.
