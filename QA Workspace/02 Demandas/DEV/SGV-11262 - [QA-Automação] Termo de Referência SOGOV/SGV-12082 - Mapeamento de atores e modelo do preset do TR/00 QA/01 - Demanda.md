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
> **Próximo passo:** revisão do Codex sobre o recorte 1 (itens 1.1–1.23, já lido e classificado contra o PDF) — os recortes 2–11 só começam depois dessa revisão.

> [!note] Abordagem anterior preservada
> A investigação original da SGV-12082 (matriz do preset, DISC-001–004), o ciclo SGV-11971 e o Roadmap anterior estão arquivados para consulta em [[../../Arquivo/Abordagem anterior/Roadmap - Automação TR|Arquivo/Abordagem anterior]] — referência histórica, não fonte de critério desta nova frente.

---

## Problema / contexto

O Termo de Referência do SOGOV (itens 1.1–1.43) ainda não tem um modelo conceitual explícito de atores, entidades, configurações, estados, relações e dependências, rastreável item a item. A abordagem anterior (preservada em [[../../Arquivo/Abordagem anterior/Roadmap - Automação TR|Arquivo/Abordagem anterior]]) inclui o ciclo de automação dos itens 1.24–1.25 (SGV-11971) **e** uma investigação mais ampla, que já havia classificado o TR completo (1.1–1.43) sob a ótica de automação e cobertura de CTs (SGV-12082 anterior, DISC-001–004). Esta nova frente não é a primeira a olhar o TR inteiro — ela se diferencia por produzir um **modelo conceitual** próprio do TR inteiro (atores, entidades, configurações, estados, relações e dependências), antes de qualquer decisão sobre casos de teste ou preset executável.

## Objetivo

Produzir um modelo conceitual rastreável do TR completo: para cada item/recorte, identificar atores/entidades, dados/atributos, configurações, estados e relações/dependências, registrados na nota temática do recorte correspondente (`01 Modelo do preset/Seções do TR/`) com a referência do item do TR e o estado de conhecimento (Confirmado/Inferido/A confirmar) — a matriz apenas indexa os recortes, sem duplicá-los — e sintetizados visualmente no mapa geral, derivado das notas temáticas confirmadas.

### Entrega desta capacidade

- Notas temáticas (por recorte do TR, ver `01 Modelo do preset/Seções do TR/`) cobrindo o TR completo, com cada item mapeado, marcado como não aplicável (sem elemento relevante para este modelo, com justificativa) ou registrado como pendente; a matriz central indexa os recortes, sem duplicar elementos/relações.
- Mapa geral (Mermaid) como síntese visual consistente das notas temáticas — nunca uma fonte própria de fato.
- Lacunas e ambiguidades encontradas registradas para revisão, não resolvidas por suposição.

---

## Decisões de método e escopo

- O TR completo (itens 1.1–1.43) é a fonte de escopo desta análise. Contexto externo pode esclarecer, mas não vira requisito sem identificação da fonte e validação.
- Os 11 recortes temáticos usados para percorrer o TR (nomes, quantidade e fronteiras) foram **aprovados pelo Rafael em 08/10/2026** — a segmentação não é mais definida durante a leitura. O que resta é analisar o conteúdo de cada recorte contra o PDF, um de cada vez, com pausa para revisão entre eles.
- Esta análise produz o modelo conceitual; não implementa seed/preset, automação, testes funcionais nem sincronização com a Qase. Isso é trabalho separado, a decidir depois, com os achados em mãos.

---

## Escopo

- Percorrer o TR completo (1.1–1.43), de forma progressiva, pelos recortes temáticos (`01 Modelo do preset/Seções do TR/`).
- Registrar, na nota temática de cada recorte, todo ator/entidade/configuração/estado identificado, com papel/descrição, dados/atributos relevantes, relações/dependências, referência ao item do TR e estado de conhecimento.
- Sintetizar o mapa geral (Mermaid) a partir do que estiver confirmado nas notas temáticas.
- Revisar cobertura (todo item do TR mapeado, não aplicável ou pendente) e consistência entre as notas temáticas e o mapa.

---

## Fora de escopo

- Casos de teste (CTs) e qualquer sincronização com a Qase.
- Automação, execução ou alteração de seed/preset.
- Decidir ou implementar o preset de dados — isso é direção futura, condicionada ao resultado deste mapeamento.

---

## Critérios de aceite

- C1. Todo item do TR completo (1.1–1.43) foi considerado; cada item está rastreável como mapeado, não aplicável (sem elemento relevante para este modelo, com justificativa) ou pendente. ^c1
- C2. Cada elemento mapeado na nota temática correspondente aponta a referência/item do TR e seu estado de conhecimento (Confirmado/Inferido/A confirmar). ^c2
- C3. Os elementos e as relações/dependências entre eles estão representados nas notas temáticas correspondentes; a matriz central indexa os recortes (intervalo de itens/páginas, status, link), sem duplicá-los. ^c3
- C4. O mapa geral (Mermaid) é uma síntese consistente do que está registrado nas notas temáticas, sem conteúdo que elas não sustentem. ^c4
- C5. Lacunas e ambiguidades encontradas durante o mapeamento estão registradas explicitamente para revisão, não resolvidas por suposição. ^c5

---

## Checklist de fechamento da análise

- [ ] Todo item do TR (1.1–1.43) está mapeado, não aplicável (com justificativa) ou pendente.
- [ ] Cada elemento/relação, registrado na nota temática correspondente, aponta a referência do item do TR.
- [ ] Notas temáticas e mapa geral (Mermaid) estão consistentes entre si.
- [ ] Lacunas e ambiguidades encontradas estão registradas para revisão.
- [ ] A [[04 - Revisão da análise|revisão da análise]] foi concluída.

---

## Pendências de decisão

Não há bloqueio atual nesta demanda. Duas decisões são **deliberadamente adiadas**, não pendências que travam o início do trabalho:

- A segmentação do TR em 11 recortes temáticos foi **aprovada pelo Rafael** (08/10/2026) — não é mais uma proposta em aberto. O conteúdo de cada recorte continua não analisado, exceto o que já estiver registrado, recorte a recorte, nas próprias notas (`Seções do TR/`); a fonte de autoridade permanece exclusivamente o PDF (`Fontes/Requisitos Sogov.pdf`) — nunca as notas temáticas, a matriz ou material arquivado.
- Se haverá entregas futuras separadas (casos de teste, preset executável) será decidido depois do mapeamento completo, com os achados em mãos — não nesta demanda.
