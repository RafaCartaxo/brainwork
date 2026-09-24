---
tags:
  - demanda
  - melhoria
  - qa
  - mesa-de-trabalho
task: "10151"
status: aberto
prioridade: media
deploy: pendente_hml
data_inicio: 2026-08-10
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: mesa-de-trabalho
ambiente: HML
---
# Demanda: [DEV][PARTE 4] Funcionalidade: Filtros "Criados por mim" / "Criados pelo setor"

> [!info] Informações
> - **Tipo:** Melhoria
> - **Status:** HML (aprovada em DEV; `deploy: pendente_hml` — o fix ainda não subiu pra homologação)
> - **Responsável QA:** Rafael
> - **Link:** [SGV-10151 no Notion](https://app.notion.com/p/alfa-group/DEV-PARTE-4-Funcionalidade-Filtros-Criados-por-mim-Criados-pelo-setor-3a02aec67d3080e0a69bcfd3f7e6796e) · [Figma — Mesa de Trabalho/Handoff](https://www.figma.com/design/57GnUc1cTERzuMCdea2eQa/Mesa-de-Trabalho---Handoff?node-id=957-2978)
> - **Dev:** B. Luan ([MR !666](https://gitlab.sogo.com.br/ari.garcia/sogov-dev/-/merge_requests/666))
> - **Item pai:** *[MELHORIA-CX] Melhoria no Layout da mesa de trabalho* (Parte 4 de N; item pai sem card próprio no vault)
> - **Refinamento:** mesa arquivada em [[QA Workspace/04 Conhecimento/Tasks/SGV-10151/SGV-10151 - Refinamento Filtros Criados Por Mim Ou Pelo Setor|04 Conhecimento/Tasks/SGV-10151]]

---

> [!abstract] Resumo

Adiciona à barra de filtros da mesa de trabalho um botão de filtro rápido por origem de criação, ao lado do botão "Favoritos". O rótulo e o comportamento mudam conforme a aba ativa: **"Criados por mim"** em "Meus documentos" (filtra por `createdById`); **"Criados pelo setor"** em "Documentos do setor" (filtra por `createdBySectorId`).

---

## Regras de negócio

**Um único componente, rótulo por aba** — não são dois botões: é o mesmo toggle, com hook próprio (`useCreatedByFilter`) que decide o rótulo pela aba ativa. Confirmado no Figma: as anatomias de "Criados por mim" e "Criados pelo setor" trazem a mesma nota de design, só troca o sujeito ("documentos criados pelo usuário" / "pelo setor selecionado").

**Anatomia de 3 estados** — Default (contornado) → Hover (contornado destacado) → Active (preenchido, ícone `PaperPlaneIcon`, rótulo em negrito). Mesma linguagem visual do botão "Favoritos", de onde a lógica de toggle com debounce foi extraída (`useDebouncedToggleFilter`). **Não existe 4º estado desenhado** em nenhuma das 3 anatomias do padrão (nem na de Favoritos) — ver Pontos de atenção sobre o estado desabilitado.

**Posição na barra** — imediatamente depois do botão "Favoritos", antes do ícone de ordenação e do filtro avançado, na mesma barra da busca (confirmado no frame "Anatomia - Alterações gerais na Mesa de Trabalho" → `tela-mesa-de-trabalho`).

**Toggle simples** — clicar ativa o filtro; clicar de novo desativa e a listagem volta ao estado padrão. Sem estado intermediário.

**Reset ao trocar de aba** — o filtro de criador é resetado (desativado) sempre que o usuário alterna entre "Meus documentos" e "Documentos do setor", mesmo que estivesse ativo antes da troca.

**Escopo do filtro** — propaga por todas as queries da mesa: lista, painel, contagem de lista e contagem de painel (kanban). Documento migrado sem criador identificado (`createdById`/`createdBySectorId` nulos) tem tratamento explícito — não pode quebrar a listagem nem aparecer indevidamente com o filtro ativo.

Regras gerais da mesa (abas, permissões, switch de setor): [[QA Workspace/04 Conhecimento/Módulos/Mesa de trabalho|Mesa de trabalho]].

---

> [!warning] Pontos de atenção
> - **Estado desabilitado sem lastro de design ou de doc.** O dev cita "botão desabilitado quando não há setor para filtrar" (chave de tradução `created-by-disabled`), mas nem o Figma nem a doc do módulo definem esse estado — nenhuma anatomia do padrão (Favoritos, Criados por mim, Criados pelo setor) desenha um 4º estado. Também não ficou claro **em que situação** a aba "Documentos do setor" existiria sem um setor ativo pra filtrar, já que o switch sempre carrega com um setor selecionado. **Confirmar com o dev o cenário exato do gatilho antes de executar o CT-008/CA8.**
> - **Reuso de componente com o Favoritos**: qualquer regressão no toggle de Favoritos (`ToggleFilterButton`/`useDebouncedToggleFilter` refatorados) é candidata a regressão cruzada — vale conferir o Favoritos na mesma rodada.

---

## Plano de teste

| Item | Definição |
|---|---|
| **Demanda** | SGV-10151 — Melhoria-CX (Parte 4) |
| **Responsável** | Rafael |
| **Ambiente** | DEV (rodada executada) → HML (próxima rodada) |
| **Escopo** | Botão de filtro "Criados por mim" / "Criados pelo setor" na barra de filtros da mesa (lista e painel): rótulo por aba, filtro por criador/setor, toggle, reset ao trocar de aba, consistência de contagem, documento migrado sem criador |
| **Fora de escopo** | Demais partes da melhoria de layout da mesa (abas, colunas do painel, filtros avançados) — cards próprios quando existirem |
| **Tipos de teste** | Funcional |
| **Dependências** | Usuário com documentos próprios e documentos do setor pra distinguir os dois filtros; setor com mais de um membro pra isolar "criado por mim" de "criado pelo setor, por outra pessoa" |

**Critérios de aceite**

*Agrupados na mesma ordem dos casos de teste.*

**A. Rótulo e filtro por aba**

- [x] **CA1** — Na aba "Meus documentos", o botão exibe o rótulo "Criados por mim"; ativo, a listagem (lista e painel) mostra só documentos criados pelo usuário logado
- [x] **CA2** — Na aba "Documentos do setor", o botão exibe o rótulo "Criados pelo setor"; ativo, a listagem mostra só documentos criados pelo setor ativo no switch

**B. Anatomia e posição do botão**

- [x] **CA3** — O botão segue os 3 estados da anatomia vigente (Default contornado, Hover contornado destacado, Active preenchido com rótulo em negrito), ícone `PaperPlaneIcon` — mesma linguagem do botão Favoritos, ao lado do qual fica na barra

**C. Toggle e troca de aba**

- [x] **CA4** — Clicar no botão ativo desativa o filtro; a listagem volta ao estado padrão (sem filtro de criador)
- [x] **CA5** — Trocar de aba (Meus documentos ↔ Documentos do setor) reseta o filtro de criador pra desativado, mesmo se estava ativo antes da troca

**D. Dados e consistência**

- [x] **CA6** — Documento migrado sem criador identificado não quebra a listagem nem aparece indevidamente com o filtro ativo (nem por `createdById` nem por `createdBySectorId`)
- [x] **CA7** — Com o filtro ativo, a contagem exibida no modo Painel (por coluna) é consistente com a contagem do modo Lista

**E. Estado desabilitado**

- [ ] **CA8** — Quando não há setor disponível pra filtrar, o botão "Criados pelo setor" aparece com tratamento visual de desabilitado, sem interação *(satisfeito por construção — ver CT-008)*

> [!info]- Critérios fora desta rodada (registro)
> - **CA8** (botão desabilitado sem setor pra filtrar) — **satisfeito por construção**, não por teste: o cenário é inalcançável (o switch sempre carrega um setor ativo na aba "Documentos do setor"). Fica **desmarcado** de propósito — aprovar critério não exercitado é registro falso ([[Sistema/Skills/SKILL_CASOS_DE_TESTE|SKILL_CASOS_DE_TESTE]]). Precedente do mesmo tratamento: SGV-9042/CT-003.
> - Nenhum critério descartado. Aprovação em DEV com **7 de 8** critérios exercitados.

---

## Casos de teste

### A. Rótulo e filtro por aba

#### **CT-001 "Criados por mim" filtra pelo usuário logado em Meus documentos** *(CA1)*

**Dado** que estou na aba "Meus documentos" da mesa de trabalho
**Quando** clico no botão de filtro "Criados por mim"
**Então** a listagem (lista e painel) passa a exibir somente documentos criados por mim

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-002 "Criados pelo setor" filtra pelo setor ativo em Documentos do setor** *(CA2)*

**Dado** que estou na aba "Documentos do setor", com um setor ativo no switch
**Quando** clico no botão de filtro "Criados pelo setor"
**Então** a listagem (lista e painel) passa a exibir somente documentos criados por qualquer servidor do setor ativo

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### B. Anatomia e posição do botão

#### **CT-003 Botão segue a anatomia de 3 estados e a posição na barra** *(CA3)*

**Dado** que estou na mesa de trabalho, em qualquer aba
**Quando** observo o botão de filtro de criador em Default, Hover e Active
**Então** ele aparece imediatamente depois do botão "Favoritos" na barra de filtros, com ícone `PaperPlaneIcon` contornado em Default/Hover e preenchido com rótulo em negrito em Active

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### C. Toggle e troca de aba

#### **CT-004 Clicar no botão ativo desativa o filtro** *(CA4)*

**Dado** que o filtro "Criados por mim" ou "Criados pelo setor" está ativo
**Quando** clico no botão novamente
**Então** o filtro desativa e a listagem volta a exibir todos os documentos da aba, sem o filtro de criador

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-005 Trocar de aba reseta o filtro de criador** *(CA5)*

**Dado** que o filtro de criador está ativo numa aba
**Quando** troco para a outra aba (Meus documentos ↔ Documentos do setor)
**Então** o filtro de criador aparece desativado na aba de destino, mesmo tendo ficado ativo na aba de origem

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### D. Dados e consistência

#### **CT-006 Documento migrado sem criador não quebra o filtro** *(CA6)*

**Dado** que existe um documento migrado sem `createdById`/`createdBySectorId` preenchido
**Quando** ativo o filtro "Criados por mim" ou "Criados pelo setor"
**Então** a listagem carrega sem erro, e o documento migrado não aparece no resultado filtrado

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

#### **CT-007 Contagem do Painel é consistente com a Lista, com o filtro ativo** *(CA7)*

**Dado** que o filtro de criador está ativo
**Quando** comparo a contagem de documentos por coluna no modo Painel com a contagem equivalente no modo Lista
**Então** os números são consistentes entre os dois modos

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

---

### E. Estado desabilitado

#### **CT-008 Botão "Criados pelo setor" desabilitado sem setor pra filtrar** *(CA8)*

> [!info]- Por que não se aplica
> O cenário não existe: a aba "Documentos do setor" sempre carrega com um setor ativo pelo switch, então **não há estado alcançável** em que o botão "Criados pelo setor" exista sem setor pra filtrar. Confirmado com o Rafael em 10/08/2026, na validação em DEV. O critério segue válido como regra — está satisfeito **por construção**, não por teste. Se o produto passar a permitir a aba sem setor ativo (ou exibir o botão fora dela), este CT volta a ser executável.
> O estado desabilitado **existe no código** (chave `created-by-disabled`, citada pelo dev no MR !666) sem cenário que o alcance — vale levar ao dev, ver pendência na fila.

**Dado** que eu esteja num cenário sem setor disponível pra filtrar (a confirmar com o dev)
**Quando** observo o botão "Criados pelo setor"
**Então** ele aparece com tratamento visual de desabilitado, sem responder a clique

**Execução Passou?**
- [ ] Sim
- [ ] Não
- [x] Não se aplica

**Evidências de Testes:**

---

## Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Desenvolvimento/) [🔍](evidencia://10151)

![[10151 - filtros criados por mim e criados pelo setor ok.mp4]]

*Gravação da validação em DEV. **Cobertura por CT ainda não mapeada** — quando o mapa CT → EV estiver definido, renomear pro padrão `10151 - EV-01 - CT-NNN, ... - <descrição>.mp4` e embedar em cada "Evidências de Testes" ([[QA Workspace/Evidências/README#Evidência de caso de teste|Evidências/README]]). Pendência na fila.*

---

> [!tip] Observações
> - Refinado a partir do export do Notion + entrega do dev (B. Luan, MR !666) + inspeção da anatomia no Figma (Claude em Chrome). Mesa de refinamento arquivada em [[QA Workspace/04 Conhecimento/Tasks/SGV-10151/SGV-10151 - Refinamento Filtros Criados Por Mim Ou Pelo Setor|04 Conhecimento]].
> - Regra completa da mesa em [[QA Workspace/04 Conhecimento/Módulos/Mesa de trabalho|Mesa de trabalho]] — seção "2. Filtros rápidos dinâmicos e inteligentes" já documenta o rótulo por aba (sem divergência com esta entrega); não documenta o estado desabilitado (CA8).

## Histórico

- 2026-08-10 - 📝 Melhoria refinada (critérios de aceite prontos)
- 2026-08-10 - ✅ Melhoria aprovada em DEV (7 de 8 critérios; CA8 satisfeito por construção)
