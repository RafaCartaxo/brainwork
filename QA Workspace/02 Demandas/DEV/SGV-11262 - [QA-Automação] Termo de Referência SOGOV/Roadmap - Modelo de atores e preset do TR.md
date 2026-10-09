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

**Fora de escopo nesta fase:** casos de teste (CTs), sincronização com a Qase, automação e qualquer implementação de preset. Esses são trabalhos separados, a decidir depois que o modelo existir com evidência.

## Estado atual

- **Abordagem anterior:** arquivada para consulta em [[Arquivo/Abordagem anterior/Roadmap - Automação TR|Arquivo/Abordagem anterior]] — referência de consulta, **não é fluxo ativo**.
- **SGV-12082 (atual):** segmentação em 11 recortes temáticos **aprovada pelo Rafael** (08/10/2026). **Os 11 recortes (itens 1.1–1.43) foram revisados e aprovados pelo Codex**, e a revisão documental da análise foi concluída (ver [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/00 QA/04 - Revisão da análise|04 - Revisão da análise]]). As dúvidas de negócio levantadas durante o mapeamento seguem registradas em aberto, sem travar essa conclusão.
- **Piloto de especificação do preset (09/10/2026):** dezesseis fatias **revisadas e aprovadas pelo Codex** — [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/02 - Especificação do preset piloto (TR 1.24–1.27)|02 (TR 1.24–1.27)]], [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/03 - Especificação do preset piloto (TR 1.28–1.29)|03 (TR 1.28–1.29)]], [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/04 - Especificação do preset piloto (TR 1.30–1.31)|04 (TR 1.30–1.31)]], [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/05 - Especificação do preset piloto (TR 1.32, 1.36–1.37)|05 (TR 1.32, 1.36–1.37)]], [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/06 - Especificação do preset piloto (TR 1.33)|06 (TR 1.33)]], [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/07 - Especificação do preset piloto (TR 1.34)|07 (TR 1.34)]], [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/08 - Especificação do preset piloto (TR 1.35.2.2.1)|08 (TR 1.35.2.2.1)]], [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/09 - Especificação do preset piloto (TR 1.35.2.3)|09 (TR 1.35.2.3)]], [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/10 - Especificação do preset piloto (TR 1.35.2.4)|10 (TR 1.35.2.4)]], [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/11 - Especificação do preset piloto (TR 1.35.2.5)|11 (TR 1.35.2.5)]], [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/12 - Especificação do preset piloto (TR 1.35.2.6–1.35.2.7)|12 (TR 1.35.2.6–1.35.2.7)]], [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/13 - Especificação do preset piloto (TR 1.35.3)|13 (TR 1.35.3)]], [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/14 - Especificação do preset piloto (TR 1.35.4)|14 (TR 1.35.4)]] [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/15 - Especificação do preset piloto (TR 1.35.5)|15 (TR 1.35.5)]] (recorte 07 dividido por item, agora completo) [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/16 - Especificação do preset piloto (TR 1.40.2–1.40.2.1)|16 (TR 1.40.2–1.40.2.1)]] (abre o recorte 08, assinaturas) e [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/17 - Especificação do preset piloto (TR 1.40.3)|17 (TR 1.40.3)]]. Próxima fatia a definir pelo Codex. Todas são especificação, não implementação.

## Entregas existentes

| Entrega | Referência | Escopo | Status |
|---|---|---|---|
| Ciclo 1.24-1.25 | [[Arquivo/Abordagem anterior/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Arquivo/00 QA/00 README\|SGV-11971]] | Autenticação e ciclo de vida do usuário (itens 1.24–1.25) | 🗄️ Histórico arquivado |
| Entrega 01 — Baseline na instância 225 | [[Arquivo/Abordagem anterior/SGV-11971 - TR 1.24-1.25 Autenticação e Ciclo de Vida/Entrega 01 - Baseline de autenticação na instância 225/00 QA/00 README\|Entrega 01]] | Piloto de seleção da instância 225 pelo seed | 🗄️ Histórico arquivado; não executada nem validada |
| SGV-12082 — Análise do TR e preset de dados (anterior) | [[Arquivo/Abordagem anterior/SGV-12082 - Análise do TR e preset de dados/00 QA/00 README\|SGV-12082 anterior]] | Mapa do projeto de automação, cobertura do TR (DISC-001–004) e recomendação de porte | 🗄️ Histórico arquivado; concluída com recomendação registrada |
| SGV-12082 — Mapeamento de atores e modelo do preset do TR (atual) | [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/00 QA/00 README\|SGV-12082 atual]] | Modelo de atores/entidades/relações a partir do TR completo | ✅ Os 11 recortes (itens 1.1–1.43) revisados e aprovados pelo Codex; revisão documental da análise concluída; dúvidas de negócio seguem registradas em aberto |

## Sequência macro da SGV-12082

A ordem abaixo é macro, verificável por etapa e com gates — não antecipa achados de domínio (atores, estados, relações), só o fluxo de trabalho.

1. **Confirmar segmentação/índice** — ✅ **concluído**: o recorte temático do TR completo (11 notas em `01 Modelo do preset/Seções do TR/`, indexadas pela [[SGV-12082 - Mapeamento de atores e modelo do preset do TR/01 Modelo do preset/01 - Matriz de atores e relações|matriz]]) foi validado contra o PDF e **aprovado pelo Rafael** (08/10/2026), junto com demanda e plano de análise.
2. **Ler e registrar cobertura por nota temática** — ✅ **concluído**: todos os 11 recortes (itens 1.1–1.43) foram lidos, classificados (mapeado/não aplicável/pendente) e registrados com elementos, relações, dúvidas e fontes, com página/referência do TR, revisados e aprovados pelo Codex. **Gate cumprido:** cada recorte só avançou após a revisão do anterior; não há mais recorte pendente de leitura.
3. **Consolidar atores/elementos/estados/relações sem duplicação** — a matriz central permanece só como índice dos recortes (intervalo de itens/páginas, status, link); nenhum elemento/relação é copiado pra fora da nota temática que o registrou. **Gate:** não há consolidação de recorte que ainda não tenha sido lido.
4. **Montar o Mermaid a partir dos achados confirmados** — síntese visual no mapa geral, usando só o que já estiver confirmado nas notas temáticas. **Gate:** o mapa nunca antecipa conteúdo que as notas ainda não têm.
5. **Revisar rastreabilidade e fechar a análise** — conferir cobertura completa (nenhum item do TR omitido), consistência entre notas temáticas e mapa, e só então decidir, com os achados em mãos, se há entregáveis futuros separados (ex.: casos de teste, preset executável). **Gate:** nenhuma entrega futura é proposta antes dessa revisão.

```mermaid
flowchart TD
    A[Confirmar segmentacao/indice] --> B[Ler e registrar cobertura por nota tematica]
    B --> C[Consolidar atores/elementos/relacoes sem duplicacao]
    C --> D[Montar o mapa visual a partir dos achados confirmados]
    D --> E[Revisar rastreabilidade e fechar a analise]
    E --> F[Decidir entregaveis futuros, com achados em maos]
```

## Dependências e gates

- O passo 2 (ler por recorte) só começa depois do passo 1 (segmentação/índice confirmados).
- O passo 3 (consolidação) é alimentado continuamente conforme recortes do passo 2 são concluídos — não é uma etapa única no fim, mas nunca adianta um recorte ainda não lido.
- O passo 4 (Mermaid) depende do que já estiver confirmado nas notas temáticas — nunca antecipa conteúdo que elas ainda não tenham.
- O passo 5 (fechamento) depende de todos os recortes terem passado pelo passo 2; a decisão sobre entregáveis futuros (parte final do passo 5) só acontece depois da revisão de rastreabilidade.

## Direção futura (condicionada, sem compromisso de implementação)

Uma direção possível, **ainda futura e condicionada ao resultado desta análise**: usar o modelo de atores/relações como base para avaliar e preparar um preset de dados reproduzível por **cliente/instância** e por **ambiente**. Isso não é uma decisão de implementação — é um horizonte que só se torna concreto depois que o modelo tiver evidência suficiente (passos 1–5 acima).

---

Para localizar documentos, ciclos e a estrutura de pastas da iniciativa, use o [[Conhecimento/0 - SGV-11262 - Índice|Índice da SGV-11262]] — este Roadmap não duplica essa navegação.
