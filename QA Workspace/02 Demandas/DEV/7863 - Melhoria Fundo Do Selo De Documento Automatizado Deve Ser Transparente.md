---
tags:
  - demanda
  - qa
task: "7863"
status: resolvido
ambiente: PROD
prioridade: media
mel: ""
data_inicio: 2026-08-26
data_fim: 2026-08-26
responsavel: Rafael
modulo: documento automatizado
---
# Demanda: Fundo do selo de documento automatizado deve ser transparente

> [!info] Informações
> - **Tipo:** Melhoria
> - **Status:** DEV
> - **Responsável QA:** Rafael
> - **Link:** (Notion — SGV-7863)

> [!warning] Card criado tarde, a partir de evidência nova
> SGV-7863 vinha como pendência de "criar o card" desde 21/08 (defeito filho [[QA Workspace/02 Demandas/Concluídas/11001 - Defeito Tabela Com Fundo Branco E Imagem Oculta No Documento Automatizado Gerado|SGV-11001]] já existia, mas a pai nunca ganhou card local — ver aviso do 🔄 desde então). Card nasce agora porque uma evidência nova apareceu na raiz de `Evidências/`: `7863 - crop automatico e imagem fundo branco transparente ok.mp4`.

---

> [!abstract] Resumo

Ao aplicar um documento automatizado como carimbo/selo, o sistema renderizava o selo com fundo branco em vez de transparente — o fundo branco sobrepunha conteúdo do documento, gerava poluição visual e não seguia o padrão esperado de selos digitais.

---

## Regras de negócio

- O selo/carimbo deve possuir fundo transparente.
- O elemento deve se integrar visualmente ao documento, sem sobrepor conteúdo com fundo branco.

---

> [!warning] Pontos de atenção

> [!danger] Gate aberto — defeito filho ainda não fechado
> [[QA Workspace/02 Demandas/Concluídas/11001 - Defeito Tabela Com Fundo Branco E Imagem Oculta No Documento Automatizado Gerado|SGV-11001]] (tabela com fundo branco e imagem oculta no documento automatizado gerado) segue `status: aberto`. Pela regra do vault ("Melhoria não é aprovada em DEV com defeito aberto"), **não marquei esta melhoria como aprovada em DEV** mesmo com a evidência nova — só registrei o que a evidência mostra (crop automático + fundo transparente do selo). Confirmar com o Rafael se o defeito 11001 também foi corrigido nesta rodada antes de aprovar a pai.

---

## Casos de teste

#### **CT-001 Selo do documento automatizado renderiza com fundo transparente** *(regra de negócio)*

**Dado** que aplico um documento automatizado como selo/carimbo em um documento
**Quando** o selo é inserido
**Então** o fundo do elemento é transparente, sem sobrepor o conteúdo do documento com fundo branco

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

---

> [!danger] Bugs encontrados
> [[QA Workspace/02 Demandas/Concluídas/11001 - Defeito Tabela Com Fundo Branco E Imagem Oculta No Documento Automatizado Gerado|SGV-11001]] — defeito filho, ainda **aberto**. Bloqueia a aprovação desta melhoria em DEV até ser corrigido e revalidado.

---

## Evidências

![[7863 - crop automatico e imagem fundo branco transparente ok.mp4]]

---

> [!tip] Observações
> Escopo original (problema/resultado esperado) reconstituído a partir da descrição fornecida quando o defeito SGV-11001 foi cadastrado em 21/08 — não veio um card de melhoria formal antes disso.

---

## Histórico

- 2026-08-26 - 📝 Card criado (tardio) a partir de evidência nova; CT-001 (fundo transparente do selo) validado — defeito filho SGV-11001 segue aberto, aprovação em DEV pendente de confirmação
