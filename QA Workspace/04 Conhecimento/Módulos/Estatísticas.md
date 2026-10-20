---
title: Estatísticas
tags:
  - qa
  - conhecimento
  - sogov
  - estatisticas
tipo: modulo
revisado: 2026-10-20
fonte: https://app.notion.com/p/alfa-group/Estat-sticas-6be8493961ac474abdffffd1f14db5d4
fonte_criado: 2024-07-08 (Rafael)
fonte_ultima_edicao: 2026-08-19 (Vinícius Sogo)
---
# Estatísticas

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-10-20 — a página do Notion continua sendo a fonte de verdade externa; esta cópia é o acervo local pesquisável. Sem task própria pro módulo em si. **Export bem mais longo e confuso que o normal** (2233 linhas): além da definição final por categoria, tem uma seção extensa de **discussões de planejamento** datadas (04/06, 05/06, 12/06 presencial, reviews de 18/06, 20/06, 21/06) que antecedem e já foram incorporadas à definição final — não transcritas em detalhe aqui por serem brainstorm já superado. Também tem pelo menos uma **fórmula com 3 versões ao longo do tempo** (Economia Gerada) e uma **mudança completa de propósito de uma tabela inteira** (Servidores, 16/04 e 22/07/2026). Nos dois casos, documentei qual é a regra **atual** e registrei o histórico, em vez de misturar tudo — ver as seções marcadas com ⚠️ e Dúvidas em aberto pras contradições que não têm resposta clara no export.

## Visão geral
- Estatísticas dá a administradores (e a quem tiver a permissão extra) uma visão analítica de uso e desempenho do sistema, organizada em 4 categorias: **Setores**, **Módulos**, **Servidores**, **Consumo e Economia**. Cada categoria tem dados estáticos (cards no topo), gráficos (visão gerencial, dados agregados) e uma tabela (visão operacional, mais detalhada).

## Regras de negócio

### Permissões
- **Administrador**: acesso total a todos os dados estatísticos da organização.
- **"Estatística"** também existe como permissão **extra** — vinculada a um usuário de outro nível, dá o mesmo acesso total.

### Visualização de dados — regras gerais
- Dois formatos: **Gráfico** (visão gerencial) e **Tabela** (visão operacional, complementar, mais detalhe por item).
- **Implantação**: documentos criados durante a fase "em implantação" do cliente são temporários/simulação — não contam pras estatísticas. Ao cliente virar **ativo**, os dados da implantação são **zerados**, e a contagem começa do zero a partir da ativação (regra de 20/07/2026 — resolve o pedido de backlog "[MELHORIA-CX] Aba de Estatísticas apenas com dados a partir da ativação", ver Dúvidas em aberto).
- **Cópia de gráfico** (16/04/2026): qualquer gráfico de qualquer relatório pode ser copiado como imagem, respeitando os filtros aplicados (ou default). Botão de copiar fica ao lado do retrair/expandir; a imagem copiada tem o mesmo tamanho em que o gráfico está sendo exibido no momento (expandido ou não).

### Setores
- **Dados estáticos**: Total de setores (soma dos 3 abaixo) · Setores principais (ativos) · Subsetores (ativos) · Setores inativos.
- **Gráficos**:
	- **Demandas recebidas** — total de documentos recebidos por todos os setores, dividido em Interna/Externa. Filtros: período (mês atual/3 meses/6 meses/ano) + setor (seleção múltipla pra comparar). *Refinamentos*: melhor formato é linha (como "Usuários por status"); filtro "Todos os Setores" mostra o total pelo qual os setores são **responsáveis**; filtro por setor específico mostra só o que ele é responsável (não o que só está envolvido); exibir o número total no gráfico; com filtro aplicado vira linha com eixo X = meses, eixo Y = setores.
	- **Tempo médio de resolução (TMR)** — fórmula: `TMR = ΣTRDE / TDE` (soma do tempo de resolução de todos os documentos encerrados ÷ total de documentos encerrados). Tempo contado em **dias úteis**, da abertura até o encerramento no **setor dono**; reabertura soma o tempo de novo ao que já tinha. *Pendência registrada na doc*: a média geral deveria sempre considerar **todos** os setores, independente do filtro de comparação — mas, no momento da doc, o cálculo só considerava os setores selecionados no filtro (ajuste ainda não confirmado como corrigido).
	- **Documentos por status** — Em aberto, Em elaboração, Em tramitação, Pausado, Encerrado (interno + externo). *Refinamentos*: copy "STATUS" → "SITUAÇÃO" e "ENCERRADA" → "ENCERRADO"; fica só com filtro **"Momento Atual"** (demais filtros de período removidos), em gráfico de linha (eixo X = status, eixo Y = setores).
	- **Engajamento de setores** — mede ações ponderadas por peso. Fórmula: `ES = (Σ ações do setor × peso) / (Σ ações da organização × peso) × 100`. Tabela com 24 ações e pesos de 1 a 5 (ex.: Responder/Despacho, Assinar solicitação, Emitir documento = peso 5; Imprimir, Pausar documento = peso 1). *Bug conhecido registrado na doc*: a média fica **zerada** em meses sem dado (ex.: fevereiro) — sem confirmação de correção.
	- **Qualidade de atendimento externo** — avaliação de 1 a 5 estrelas; CSAT conta só notas 4 e 5: `CS = (QAB+QAE) / TA`. *Refinamentos*: "Mês atual" em pizza; default **"Consolidado"** mostra tudo até o momento, independente de período; outros períodos em barras; a data de **abertura** do documento não importa — a avaliação entra no período em que foi **feita**.
	- **Documentos impressos** — total impresso por todos os setores. *Refinamentos*: inclui despachos; conta só pelo **switch ativo** no momento da impressão; impressão de "folha de recebimento" não entra (removida do cálculo).
- **Tabela de setores**: Setor (sigla+nome; subsetor mostra sigla do pai + sigla/nome do filho) · Servidores (total ativos por status: somente leitura, usuário básico, usuário avançado, admin setorial, admin) · Total de documentos (por status) · Engajamento (média do setor) · Tempo de resolução · Avaliação externa (% satisfeitos + quantidade por nota).

### Módulos
- **Dados estáticos**: Total de documentos criados · Total internos · Total externos · Nota geral de satisfação (%).
- **Gráficos**:
	- **Documentos criados** — por módulo/assunto/serviço, interno × externo. Filtros: período, módulo, A/S (dependente do módulo selecionado), Top 5 mais/menos utilizados.
	- **Demandas de assuntos e serviços** — Top 5 (mais/menos utilizados, impressões, assinaturas, nota de atendimento). *Refinamentos*: filtro de ordenação explícito (5 mais / 5 menos); resultado zerado **não** mostra imagem de "empty" — mostra os últimos módulos/A-S cadastrados com valor zero.
	- **Documentos por status** — por módulo/A-S (aberto/tramitando/encerrado/pausado). *Refinamentos*: número total no gráfico; zerado mostra zero (não "empty"); legenda mostra só nomes de módulos quando o filtro tem 2+ itens, ou todos os A/S do módulo quando o filtro é de 1 módulo só.
	- **Demandas por módulo** — Top 5 módulos (mais/menos utilizados, impressões, assinaturas, nota).
	- **Quantidade de documentos impressos** — por serviço/assunto específico ou total.
	- **Qualidade do atendimento externo** — mesma fórmula CSAT, por módulo/A-S.
- **Tabela de módulo**: Serviços e assuntos · Módulo · Documentos emitidos · Documentos encerrados · Avaliação externa.

### Servidores
- **Dados estáticos**: Total de servidores · Servidores ativos · Servidores inativos.
- **Gráficos**:
	- **Usuários servidores por status** — ativo/inativo/licença/férias, por dia no mês selecionado + setor.
	- **Servidores por nível de permissão** — Somente leitura (= N3), Usuário básico (= N2), Usuário avançado (= N1), Admin setorial, Admin.
	- **Tempo médio de permanência na plataforma** — do login ao logout. *Esclarecido em reunião pós-entrega (10/09)*: "todos os setores" = tempo total no sistema, independente do switch; com filtro de período = tempo logado naquele período; sem filtro de período = tempo acumulado; filtrando por setor específico, contabiliza o tempo de cada intervalo no switch daquele setor.
	- **Engajamento por usuário** — top 10 com maior engajamento. Fórmula **simplificada após reunião de 10/09** (antes tinha passos redundantes): `ES = Σ(QO×P) / MESU`, onde MESU é a média de engajamento dos setores que o usuário participa. Exemplo documentado chega a ES ≈ 83,33%.
	- **Usuários ativos** — total por setor, com filtro de última semana/mês/3/6 meses/ano.
	- **Qualidade do atendimento externo** (aba servidores) — mesma fórmula CSAT, por setor.
- **Tabela de servidores** — ⚠️ **mudança completa de propósito** (16/04/2026, atualizada 22/07/2026 pela **SGV-8619**):
	- A tabela **original** era comportamental: Servidor, Setores, Engajamento, Número de acessos, Média de Permanência Diária.
	- Ela foi **substituída** por uma tabela de cadastro/status pra fins de **faturamento** (uso interno do CX): **Servidor** (nome + setor principal como linha secundária) · **Data de criação** (+ quem criou e o nível de quem criou, linha secundária no formato "por $assinatura-textual ($nível)") · **Data de aprovação** · **Status** (badge + "desde dd/mm/aaaa" como linha secundária) · **Último acesso** (hora + "em dd/mm/aaaa") · botão de visualização (abre o mesmo modal da listagem de Servidores).
	- Servidores cadastrados **antes de 22/04/2026** mostram "cadastrado por Administrador SOGOV" — a autoria real não era rastreável antes dessa data.
	- **Exportação**: botão "Exportar Resultados" acima da listagem; toast "preparando seu documento..." com barra de progresso; download dispara automaticamente ao concluir; dados refletem o **momento exato** da exportação (não um período). Todas as 7 colunas vão pro arquivo; só a célula "Servidor" é desmembrada na exportação — as demais saem como string única.
	- **Objetivo**: o CX usa isso no fim de cada mês pra conciliação bancária e faturamento (número de servidores ativos + datas de aprovação/status, pra justificar cobrança junto ao cliente).

### Consumo e Economia
- **Dados estáticos**: Armazenamento total (MB/GB) · Total de documentos gerados · Total de assinaturas · Impressões realizadas · Economia gerada.
- **Gráficos**:
	- **Economia gerada** — ⚠️ **fórmula com histórico de 3 versões; a mais recente é a válida**:
		1. Versão original: `Ecm = AG/2kb × 0,35` (armazenamento total ÷ tamanho médio de uma folha de 2kb × custo médio por folha).
		2. "Novo cálculo" (sem data): detalhamento por item de custo — papel/impressão R$0,15, armazenamento físico R$0,25, transporte R$0,50, segurança R$0,10, retrabalho R$0,50 (total R$1,50/folha; 20.480 folhas por GB) → **R$30.720 por GB**.
		3. **Correção de 11/05/2026** (Alice Martins, após ver os números aplicados na POC de Natal — valor considerado muito alto): **R$10.000 por GB** — **é o valor atualmente válido**.
		- Filtro: só período (mês atual/3/6 meses/ano).
	- **Licenças ativas**, **Assinaturas** (ICP + SoGov), **Impressões**, **Total de usuários externos** (PF/PJ), **Atendimentos externos**, **Acesso ao ambiente** (interno + externo), **Uso do armazenamento**: todos com filtro só de período (mês atual/3/6 meses/ano).
- **Tabela de economia**: Período (mensal mostra os dias do mês; anual mostra os meses do ano) · Licenças ativas · Número de acessos · Atendimentos externos · Assinaturas · Impressões · Economia estimada.

## Comportamentos observados em teste
<!-- O que foi aprendido validando: comportamentos não documentados, pegadinhas, efeitos colaterais -->
- Ainda não testado — importação é só a documentação de referência.

## Dúvidas em aberto
- [ ] **Frequência de atualização dos dados — duas regras conflitantes no export**: um trecho diz que os gráficos/tabelas só atualizam ao recarregar a página ou trocar de categoria; outro trecho (logo em seguida, na mesma seção) diz que a atualização é automática a cada 12 horas. Parecem duas redações da mesma regra, uma substituindo a outra sem remover a anterior no Notion — **confirmar qual das duas vale**, não assumi nenhuma das duas como certa.
- [ ] Tempo médio de resolução: a doc registra como pendência que o cálculo da "média geral" estava considerando só os setores do filtro de comparação, quando deveria sempre considerar todos — sem confirmação se já foi corrigido.
- [ ] Engajamento de setores: bug conhecido (média zerada em mês sem dado) sem confirmação de correção.
- [ ] O export tem uma seção extensa de **discussões de planejamento** (04/06, 05/06, 12/06 presencial, reviews 18/06, 20/06, 21/06) anterior à consolidação da doc final — não trazida em detalhe por ser brainstorm já superado. Um ponto que chamou atenção lá e **não aparece refletido** nas seções finais: a decisão de renomear "Cidadão" pra **"Usuário Externo"** na aba de usuários/servidores — se essa terminologia for cobrada em algum teste, vale confirmar se pegou ou se foi revertida.
- [ ] Backlog cita "[MELHORIA-CX] Exportação da Lista de Usuários do Sogov em .XLXs" — pode ser o mesmo recurso de exportação da Tabela de Servidores (16/04/2026) ou um recurso distinto (lista de usuários **SOGO**, não servidores do cliente); não confirmado no export.
- [ ] "[MELHORIA-CX] Melhoria na visualização do painel de estatísticas (informações do servidor)" = **SGV-8619**, já implementado (ver Tabela de servidores acima) — item de backlog desatualizado, deveria estar fechado.
- [ ] "[MELHORIA-CX] Aba de Estatísticas apenas com dados a partir da ativação" parece resolvido pela regra "Cliente em implantação → Cliente ativo" (20/07/2026) — confirmar se é o mesmo item antes de dar como fechado.

## Cards relacionados
<!-- SGVs validados que tocam este módulo -->
- **SGV-8619** — Melhoria na visualização do painel de estatísticas / nova Tabela de Servidores (22/07/2026, ver seção própria).
- Sem outro SGV vinculado — demais atualizações sem task própria no Notion.

## Referências
<!-- Docs do repo (caminho), links externos, leis -->
- Notion (fonte): ver `fonte` no frontmatter.
- [[QA Workspace/04 Conhecimento/Módulos/Mesa de trabalho|Mesa de trabalho]] — status de documento (Em aberto/elaboração/tramitação/pausado/encerrado) usados nos gráficos de status.
- [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]] — tipos de assinatura (ICP/SoGov) usados no gráfico de Assinaturas.
