---
prioridade: media
origem: conversa
pontos_alocados: ""
---

# SGV-12082 — Mapeamento de atores e modelo do preset do TR

**Ticket de origem:** SGV-12082 · **Demanda pai:** SGV-11262

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]
> **Plano de análise:** [[02 - Plano de análise]]
> **Revisão da análise:** [[04 - Revisão da análise]]
> **Mapa geral:** [[../01 Modelo do preset/00 - Mapa geral]]
> **Matriz de atores e relações:** [[../01 Modelo do preset/01 - Matriz de atores e relações]]
> **Fontes:** [[../Fontes/Requisitos Sogov.pdf|Requisitos Sogov.pdf]]

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

> [!info] Status atual
> **Próximo passo:** revisão/aprovação desta demanda e do [[02 - Plano de análise|plano de análise]] — a leitura/mapeamento do TR só começa depois disso.

> [!note] Abordagem anterior preservada
> A investigação original da SGV-12082 (matriz do preset, DISC-001–004), o ciclo SGV-11971 e o Roadmap anterior estão intactos em [[../../Arquivo/Abordagem anterior/Roadmap - Automação TR|Arquivo/Abordagem anterior]] — referência histórica, não fonte de critério desta nova frente.

---

## Problema / contexto

O Termo de Referência do SOGOV (itens 1.1–1.43) ainda não tem um modelo conceitual explícito de atores, entidades, configurações, estados, relações e dependências, rastreável item a item. A abordagem anterior (preservada em [[../../Arquivo/Abordagem anterior/Roadmap - Automação TR|Arquivo/Abordagem anterior]]) inclui o ciclo de automação dos itens 1.24–1.25 (SGV-11971) **e** uma investigação mais ampla, que já havia classificado o TR completo (1.1–1.43) sob a ótica de automação e cobertura de CTs (SGV-12082 anterior, DISC-001–004). Esta nova frente não é a primeira a olhar o TR inteiro — ela se diferencia por produzir um **modelo conceitual** próprio do TR inteiro (atores, entidades, configurações, estados, relações e dependências), antes de qualquer decisão sobre casos de teste ou preset executável.

## Objetivo

Produzir um modelo conceitual rastreável do TR completo: para cada item/bloco, identificar atores/entidades, dados/atributos, configurações, estados e relações/dependências, registrados na matriz com a referência do item do TR e o estado de conhecimento (Confirmado/Inferido/A confirmar), e sintetizados visualmente no mapa geral.

### Entrega desta capacidade

- Matriz de atores e relações cobrindo o TR completo, com cada item mapeado, marcado como não aplicável (sem elemento relevante para este modelo, com justificativa) ou registrado como pendente.
- Mapa geral (Mermaid) como síntese visual consistente da matriz — nunca uma fonte própria de fato.
- Lacunas e ambiguidades encontradas registradas para revisão, não resolvidas por suposição.

---

## Decisões de método e escopo

- O TR completo (itens 1.1–1.43) é a fonte de escopo desta análise. Contexto externo pode esclarecer, mas não vira requisito sem identificação da fonte e validação.
- Os blocos temáticos usados para percorrer o TR — nomes, quantidade e fronteiras — são definidos durante a leitura, não antecipados nesta demanda.
- Esta análise produz o modelo conceitual; não implementa seed/preset, automação, testes funcionais nem sincronização com a Qase. Isso é trabalho separado, a decidir depois, com os achados em mãos.

---

## Escopo

- Percorrer o TR completo (1.1–1.43), de forma progressiva, por blocos temáticos definidos durante a leitura.
- Registrar na matriz cada ator/entidade/configuração/estado identificado, com papel/descrição, dados/atributos relevantes, relações/dependências, referência ao item do TR e estado de conhecimento.
- Sintetizar o mapa geral (Mermaid) a partir do que estiver registrado na matriz.
- Revisar cobertura (todo item do TR mapeado, não aplicável ou pendente) e consistência entre matriz e mapa.

---

## Fora de escopo

- Casos de teste (CTs) e qualquer sincronização com a Qase.
- Automação, execução ou alteração de seed/preset.
- Decidir ou implementar o preset de dados — isso é direção futura, condicionada ao resultado deste mapeamento.

---

## Critérios de aceite

- C1. Todo item do TR completo (1.1–1.43) foi considerado; cada item está rastreável como mapeado, não aplicável (sem elemento relevante para este modelo, com justificativa) ou pendente. ^c1
- C2. Cada elemento mapeado na matriz aponta a referência/item do TR correspondente e seu estado de conhecimento (Confirmado/Inferido/A confirmar). ^c2
- C3. A matriz representa tanto os elementos quanto as relações/dependências entre eles. ^c3
- C4. O mapa geral (Mermaid) é uma síntese consistente do que está registrado na matriz, sem conteúdo que a matriz não sustente. ^c4
- C5. Lacunas e ambiguidades encontradas durante o mapeamento estão registradas explicitamente para revisão, não resolvidas por suposição. ^c5

---

## Checklist de fechamento da análise

- [ ] Todo item do TR (1.1–1.43) está mapeado, não aplicável (com justificativa) ou pendente.
- [ ] Cada elemento/relação na matriz aponta a referência do item do TR correspondente.
- [ ] Matriz e mapa geral (Mermaid) estão consistentes entre si.
- [ ] Lacunas e ambiguidades encontradas estão registradas para revisão.
- [ ] A [[04 - Revisão da análise|revisão da análise]] foi concluída.

---

## Pendências de decisão

Não há bloqueio atual nesta demanda. Duas decisões são **deliberadamente adiadas**, não pendências que travam o início do trabalho:

- Os blocos temáticos usados para percorrer o TR (nomes, quantidade, fronteiras) serão definidos durante a própria leitura, não antes.
- Se haverá entregas futuras separadas (casos de teste, preset executável) será decidido depois do mapeamento, com os achados em mãos — não nesta demanda.
