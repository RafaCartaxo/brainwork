---
tags: [qa, automacao, roadmap]
task: SGV-11262
tipo: roadmap
status: ativo
---
# Roadmap — Modelo de atores e preset do TR

> [!info] Diferença entre este Roadmap e o Índice
> Este documento registra a **direção, a sequência macro e as dependências** da iniciativa. Ele não substitui a navegação/localização de documentos — isso vive no [[Conhecimento/0 - SGV-11262 - Índice|Índice da SGV-11262]].

## Objetivo e limite de escopo

Construir um modelo de **atores, entidades, configurações, estados, relações e dependências** do SOGOV, com base no **Termo de Referência completo** (itens 1.1–1.43), que sirva de referência pra avaliar e preparar um preset de dados reproduzível.

**Fora de escopo nesta demanda:** escrever/alterar CTs, sincronizar com a Qase, automatizar ou implementar o seed/preset. As fatias e a consolidação da Fase 2 registram evidências sobre o seed/testes atuais; elas não definem nem limitam o modelo-alvo. O modelo-alvo dos dados necessários aos cenários de sanidade já foi derivado do TR e da documentação de produto e está aprovado; o produto ativo agora é a matriz que mapeia, campo a campo, o canal de fornecimento (`.env`, seed persistente ou cenário). A preparação técnica/implementação do preset continua futura, fora do escopo atual.

## Estado atual

- **Abordagem anterior:** arquivada para consulta em [[Arquivo/Abordagem anterior/Roadmap - Automação TR|Arquivo/Abordagem anterior]] — referência de consulta, **não é fluxo ativo**.
- **Fase 1 — Modelo conceitual do TR completo:** ✅ **concluída** (09/10/2026). Segmentação em 11 recortes temáticos aprovada pelo Rafael (08/10/2026); os 11 recortes (itens 1.1–1.43) revisados e aprovados pelo Codex; revisão documental concluída (ver [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/00 QA/04 - Revisão da análise|04 - Revisão da análise]]).
- **Fase 2 — Evidências da automação atual (concluída):** 17 fatias aprovadas pelo Codex (notas 02–18) e consolidação aprovada registram o que os testes e o seed atuais demonstram. São referência técnica para rastreabilidade e possível reaproveitamento, não especificação do preset-alvo.
- **Triagem do caminho inicial:** ✅ **concluída** como seleção da ordem de partida. A nota [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/03 - Triagem dos itens sem fatia (passo 8)|03 - Triagem dos itens sem fatia]] foi aprovada para orientar o modelo-alvo; extensões e dúvidas continuam abertas, sem exclusão de requisitos. A aprovação do caminho não confirma automaticamente as evidências técnicas de cada linha.
- **Fase 3 — Modelo-alvo dos dados do preset:** ✅ **concluída** (13/10/2026). [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 - Modelo-alvo dos dados do preset]] foi revisado e aprovado pelo Rafael/Codex — atores, entidades, configurações, estados e relações necessários aos cenários de sanidade, com síntese visual Mermaid por grupo (C1–C6). Não decide canal de fornecimento.
- **Fase 4 — Mapeamento de fornecimento:** ✅ **concluída e aprovada pelo Codex** (13/10/2026). Artefato: [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/05 - Matriz de fornecimento dos dados|05 - Matriz de fornecimento dos dados]], cobrindo C1–C6 — um canal candidato pra cada dado/estado do modelo-alvo (`.env` individual, seed persistente, cenário de teste, ou combinação), sem reclassificar a natureza do dado/configuração. A aprovação valida a matriz como artefato; cada atribuição de canal segue **hipótese candidata**, não decisão de arquitetura.
- **SGV-12082 encerrada neste escopo (15/10/2026, decisão do Rafael):** as Fases 1–4 (passos 1–10 da Sequência macro, abaixo) estão concluídas e aprovadas; a demanda foi fechada nesse escopo sem reabrir TR, recortes, 04 ou 05. Ver [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/00 QA/00 README|README]] e [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/00 QA/01 - Demanda|Demanda]].
- **Fase 5 — Decidir a preparação técnica (trilha futura e separada):** determinar persistência, reconciliação e execução por ambiente/instância a partir das hipóteses de canal da matriz. Nenhuma arquitetura ou implementação foi iniciada. A hipótese de seed de alto custo preparado uma vez continua relevante, mas não exclui dados fornecidos pelo `.env` individual nem define arquitetura agora. **Esta fase é uma trilha futura e separada — não bloqueia o encerramento da SGV-12082 nem o levantamento da SGV-12200, e nenhuma nova task técnica foi criada para ela neste encerramento.**
- **SGV-12200 — Levantamento da Onda 1 de cenários de sanidade (iniciada em 15/10/2026):** frente irmã que usa os artefatos aprovados 04/05 como referência para propor um primeiro lote de 20 cenários candidatos de sanidade, rastreáveis ao TR. Foi pacote filho desta SGV-11262 até 16/10/2026, quando passou a demanda irmã independente (movida para `02 Demandas/DEV/`, fora desta pasta). Não é continuação da SGV-12082 nem decide o passo 11. Ver [[QA Workspace/02 Demandas/DEV/SGV-12200 - Levantamento da Onda 1 de cenários de sanidade/00 QA/00 README|README da SGV-12200]].
- **Dúvidas de negócio (trilha paralela):** levantadas durante o mapeamento (Fase 1) — Canal Oficial (1.38.1.b) e Jornal Oficial (1.38.3.1) foram esclarecidos no contexto do produto atual em 13/10/2026 (mesmo fluxo de divulgação externa, via [[QA Workspace/04 Conhecimento/Módulos/Divulgar Documento|Divulgar Documento]]); outras seguem abertas (ver [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/00 - Mapa geral#Lacunas registradas (arestas tracejadas)|lacunas no mapa geral]]). Não bloqueiam a seleção do caminho inicial nem o modelo-alvo; quando uma dúvida afetar um dado específico, esse ponto fica marcado como aberto e pode ser aprofundado depois.

## Entregas existentes

| Entrega | Referência | Escopo | Status |
|---|---|---|---|
| Ciclo 1.24-1.25 | [[Arquivo/Abordagem anterior/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/00 README\|SGV-11971]] | Autenticação e ciclo de vida do usuário (itens 1.24–1.25) | 🗄️ Histórico arquivado |
| Entrega 01 — Baseline na instância 225 | [[Arquivo/Abordagem anterior/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Entrega 01 - Baseline de autenticação na instância 225/00 QA/00 README\|Entrega 01]] | Piloto de seleção da instância 225 pelo seed | 🗄️ Histórico arquivado; não executada nem validada |
| SGV-12082 — Análise do TR e preset de dados (anterior) | [[Arquivo/Abordagem anterior/SGV-12082 - Análise do TR e preset de dados/00 QA/00 README\|SGV-12082 anterior]] | Mapa do projeto de automação, cobertura do TR (DISC-001–004) e recomendação de porte | 🗄️ Histórico arquivado; concluída com recomendação registrada |
| SGV-12082 — Mapeamento de atores e modelo do preset do TR | [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/00 QA/00 README\|SGV-12082]] | Modelo-alvo dos dados necessários aos cenários do TR | ✅ **Encerrada neste escopo (15/10/2026)** — Fase 1 e evidências atuais concluídas; caminho-base aprovado; modelo-alvo aprovado; matriz de fornecimento aprovada; 🔵 preparação técnica (passo 11) trilha futura separada, fora desta demanda |
| SGV-12200 — Levantamento da Onda 1 de cenários de sanidade (demanda irmã independente desde 16/10/2026) | [[QA Workspace/02 Demandas/DEV/SGV-12200 - Levantamento da Onda 1 de cenários de sanidade/00 QA/00 README\|SGV-12200]] | Proposta rastreável de 20 cenários candidatos de sanidade, usando 04/05 como referência | 🔵 Rascunho da Onda 1 — pendente de aprovação do Rafael; não é seleção oficial nem CTs |

## Sequência macro da SGV-12082

A ordem abaixo é macro, verificável por etapa e com gates — não antecipa achados de domínio (atores, estados, relações), só o fluxo de trabalho.

1. **Confirmar segmentação/índice** — ✅ **concluído**: o recorte temático do TR completo (11 notas em `01 Modelo do preset/Seções do TR/`, indexadas pela [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/01 - Matriz de atores e relações|matriz]]) foi validado contra o PDF e **aprovado pelo Rafael** (08/10/2026), junto com demanda e plano de análise.
2. **Ler e registrar cobertura por nota temática** — ✅ **concluído**: todos os 11 recortes (itens 1.1–1.43) foram lidos, classificados (mapeado/não aplicável/pendente) e registrados com elementos, relações, dúvidas e fontes, com página/referência do TR, revisados e aprovados pelo Codex. **Gate cumprido:** cada recorte só avançou após a revisão do anterior; não há mais recorte pendente de leitura.
3. **Consolidar atores/elementos/estados/relações sem duplicação** — a matriz central permanece só como índice dos recortes (intervalo de itens/páginas, status, link); nenhum elemento/relação é copiado pra fora da nota temática que o registrou. **Gate:** não há consolidação de recorte que ainda não tenha sido lido.
4. **Montar o Mermaid a partir dos achados confirmados** — síntese visual no mapa geral, usando só o que já estiver confirmado nas notas temáticas. **Gate:** o mapa nunca antecipa conteúdo que as notas ainda não têm.
5. **Revisar rastreabilidade e fechar a análise (Fase 1)** — ✅ **concluído**: cobertura completa conferida (nenhum item do TR omitido), consistência entre notas temáticas e mapa revisada (ver [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/00 QA/04 - Revisão da análise|04 - Revisão da análise]]). **Gate cumprido:** a decisão tomada foi abrir a Fase 2 (passo 6) com os achados em mãos.
6. **Registrar evidências da automação atual** — ✅ **concluído**: 17 fatias revisadas individualmente (notas 02–18), distinguindo o que o seed/testes mostram hoje, suas lacunas e as incertezas. Esse levantamento informa, mas não define, o preset-alvo.
7. **Consolidar as evidências atuais** — ✅ **concluído**: ver [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/02 - Visão consolidada do preset candidato|02 - Visão consolidada do preset candidato]]. Não é uma especificação final do modelo-alvo.
8. **Selecionar o caminho inicial para o modelo-alvo** — ✅ **concluído**: o caminho-base da nota 03 foi aprovado para iniciar o modelo, preservando extensões e dúvidas como aprofundamentos posteriores. Não foi necessário declarar requisitos fora do preset nem fechar todas as questões.
9. **Construir o modelo-alvo do preset** — ✅ **concluído** (13/10/2026): atores, dados, configurações, estados e relações necessários aos cenários de sanidade do TR completo, com origem rastreável em TR/produto, revisado e aprovado em [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04 - Modelo-alvo dos dados do preset]]. Não decide canal de fornecimento.
10. **Mapear o fornecimento dos dados** — ✅ **concluído e aprovado pelo Codex** (13/10/2026): pra cada dado/estado necessário já definido no passo 9, registrado o canal candidato — `.env` individual, seed persistente, preparação no cenário de teste, ou combinação — sem confundir isso com a natureza do dado/configuração. Artefato: [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/05 - Matriz de fornecimento dos dados|05 - Matriz de fornecimento dos dados]], cobrindo C1–C6. Hipóteses de canal seguem candidatas, não decisões; nenhum CT ou código de seed foi produzido nesta etapa.
11. **Decidir a preparação técnica** — 🔵 **trilha futura e separada, não é o próximo passo corrente**: determinar persistência, reconciliação e execução por ambiente/instância a partir das hipóteses de canal do passo 10. Nenhuma arquitetura ou implementação foi iniciada, e nenhuma demanda técnica foi criada para tratar disso. A hipótese de seed persistente de alto custo permanece, junto com o fornecimento de dados pelo `.env`; arquitetura não está decidida. Com a SGV-12082 encerrada em seu escopo (passos 1–10) e a SGV-12200 em andamento como frente ativa, este passo segue aberto e desacoplado das duas, acionado só quando uma dependência concreta exigir.

```mermaid
flowchart TD
    A[Confirmar segmentacao/indice] --> B[Ler e registrar cobertura por nota tematica]
    B --> C[Consolidar atores/elementos/relacoes sem duplicacao]
    C --> D[Montar o mapa visual a partir dos achados confirmados]
    D --> E[Revisar rastreabilidade e fechar a analise - Fase 1]
    E --> F[Registrar evidencias do seed e testes atuais]
    F --> G[Consolidar evidencias atuais]
    G --> H[Selecionar caminho inicial do modelo-alvo]
    H --> I[Modelar dados necessarios a partir do TR e produto]
    I --> J[Mapear fornecimento: .env, seed ou cenario]
    J --> K[Decidir preparacao tecnica futura]
```

## Dependências e gates

- O passo 2 (ler por recorte) só começa depois do passo 1 (segmentação/índice confirmados).
- O passo 3 (consolidação dos recortes) é alimentado continuamente conforme recortes do passo 2 são concluídos — não é uma etapa única no fim, mas nunca adianta um recorte ainda não lido.
- O passo 4 (Mermaid do mapa geral) depende do que já estiver confirmado nas notas temáticas — nunca antecipa conteúdo que elas ainda não tenham.
- O passo 5 (fechamento da Fase 1) depende de todos os recortes terem passado pelo passo 2; a decisão de abrir a Fase 2 (passo 6) só aconteceu depois da revisão de rastreabilidade.
- O passo 6 está **concluído** como inventário de evidências atuais, sem impor os limites do seed ao modelo-alvo.
- O passo 7 está **concluído** como consolidação dessas evidências.
- O passo 8 está concluído como seleção do ponto de partida; não significa que todas as dúvidas ou classificações técnicas tenham sido encerradas.
- O passo 9 está **concluído**: modelo-alvo revisado e aprovado (ver [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Modelo-alvo dos dados do preset|04]]); os passos 9, 10 e 11 não implementam seed nem automação.
- O passo 10 está **concluído e aprovado pelo Codex**: mapeou, campo a campo, o canal de fornecimento (`.env`, seed persistente, cenário de teste, ou combinação) pra cada dado/estado já definido no passo 9 — sem reclassificar a natureza do dado/configuração em si; a aprovação valida a matriz como artefato, as hipóteses de canal seguem candidatas, não decisões.
- O passo 11 (decidir a preparação técnica/arquitetura por ambiente/instância) é **trilha futura e separada, não o próximo passo corrente** — nenhuma arquitetura ou implementação foi iniciada, e nenhuma demanda técnica foi criada para tratar disso. Não bloqueia a SGV-12082 (já encerrada em seu escopo) nem a SGV-12200 (frente ativa).
- Dúvidas de negócio (trilha paralela, ver "Estado atual") não bloqueiam o modelo-alvo como um todo; quando um elemento específico depender diretamente de uma delas, ele permanece marcado como pendente, sem travar o restante do modelo.

## Resultado esperado e etapa técnica futura

O resultado desta demanda é o **modelo-alvo rastreável** dos dados necessários aos cenários de sanidade do TR e a **matriz de fornecimento** que atribui cada dado a um canal candidato — ambos revisados e aprovados pelo Codex. A futura preparação reproduzível por ambiente/instância (passo 11, trilha futura e separada, sem demanda técnica própria criada) será decidida a partir desses dois artefatos quando houver dependência concreta; a etapa de preparação técnica e qualquer implementação permanecem fora do escopo atual, ainda não iniciadas.

---

Para localizar documentos, ciclos e a estrutura de pastas da iniciativa, use o [[Conhecimento/0 - SGV-11262 - Índice|Índice da SGV-11262]] — este Roadmap não duplica essa navegação.
