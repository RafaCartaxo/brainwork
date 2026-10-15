---
title: Zoneamento Urbano — Conceitos de Planejamento
tags:
  - qa
  - conhecimento
  - referencia
  - zoneamento
  - urbanismo
tipo: referencia
revisado: 2026-10-15
---
# Zoneamento Urbano — Conceitos de Planejamento

> [!info] Origem
> Conteúdo de apoio pra aprendizagem — **não** veio do Notion nem é documentação de produto. É conhecimento geral de planejamento urbano, organizado como ponte com o módulo [[QA Workspace/04 Conhecimento/Módulos/Processos Urbanísticos|Processos Urbanísticos]] do SoGov, que implementa zoneamento mas nunca define formalmente os conceitos por trás dele (ver "Dúvidas em aberto" daquela doc — a própria fonte original tem uma nota do autor dizendo "colocar aqui uma explicação do que são as zonas e os usos", nunca preenchida). Criado em 2026-10-15 a pedido do Rafael, pra estudo.

## Resumo geral
Processos Urbanísticos é o módulo do SoGov que permite a uma prefeitura cadastrar o zoneamento da cidade — como o território é dividido em zonas e o que pode ou não ser construído em cada uma — pra que cidadãos e empresas consultem isso antes de comprar um terreno ou pedir um alvará, podendo abrir o processo direto a partir dessa consulta.

## Objetivo
Dar transparência pública sobre regras urbanísticas e conectar essa consulta com a abertura de um processo administrativo de verdade — sem o cidadão precisar ligar pra prefeitura ou adivinhar.

## O conceito real, fora do sistema

Municípios dividem o território em zonas pra controlar como a cidade cresce: densidade, tipo de atividade (morar, trabalhar, produzir), impacto ambiental, infraestrutura. Isso é definido por lei municipal — normalmente o **Plano Diretor** + a **Lei de Uso e Ocupação do Solo** (no Brasil, cidades grandes são obrigadas a ter Plano Diretor pelo Estatuto da Cidade).

Termos que valem saber:
- **Zoneamento** — divide a cidade em zonas com regras diferentes (Zona Residencial, Comercial, Industrial, de Proteção Ambiental, Mista...).
- **Uso do solo** — o que pode funcionar numa zona (residencial, comercial, industrial, institucional, misto).
- **Índices urbanísticos** — os números que definem o quanto/como pode construir:
	- **Coeficiente de Aproveitamento (CA)** — quanto se pode construir em relação ao terreno (área construída ÷ área do terreno). Ex.: CA 2,0 num terreno de 500m² permite até 1000m² construídos.
	- **Taxa de Ocupação (TO)** — % do terreno que o prédio pode ocupar no chão.
	- **Gabarito / altura máxima** — altura máxima permitida (metros ou nº de andares).
	- **Recuos** — distância mínima da construção até as divisas do terreno (frente, lateral, fundos).
	- **Taxa de permeabilidade** — % do terreno que precisa ficar sem laje, pra infiltrar água da chuva.

**Por que importa**: evita adensamento descontrolado, enchente por impermeabilização, conflito entre usos incompatíveis (indústria poluente ao lado de escola), e garante que a infraestrutura (água, esgoto, trânsito) acompanhe o que é construído.

## Como isso vira campo no SoGov (a ponte)

| Conceito real | Campo no SoGov |
|---|---|
| Zona de zoneamento (ex.: ZR-2, Centro Histórico) | **Zona** |
| Uso permitido naquela zona (residencial, comercial...) | **Categoria de uso** |
| Cada índice urbanístico (CA, TO, gabarito, recuo...) | **Parâmetro** da categoria, com unidade (número, %, metros, m², fórmula) |

**Exemplo prático**: Zona "Centro Histórico" → Categoria de uso "Comercial Restrito" → parâmetros: CA = 1,5 · TO = 70% · Gabarito = 12m · Recuo frontal = 3m.

## Como funciona na prática (fluxo no sistema)
1. A prefeitura libera "Processos Urbanísticos" pro cliente.
2. No ambiente do cliente aparece o menu **"Zoneamentos urbanos"**: o Admin cadastra zonas (manual ou importando mapa `.kmz`) e categorias de uso com seus parâmetros.
3. O Admin **publica** o zoneamento — antes disso, nada aparece pro cidadão.
4. Na Central de Atendimento (portal público), o cidadão vê a lista de zonas (lista ou mapa), clica numa e vê localidades, descrição, categorias de uso e parâmetros.
5. Dali, pode abrir direto um processo (ex.: alvará) já vinculado àquela zona/categoria.
6. Tecnicamente, um módulo de "processo administrativo" pode ganhar a característica urbanística, o que adiciona dois campos dependentes no formulário de abertura: escolhe a zona, depois (só então) a categoria de uso.

**Extra**: documentos urbanísticos têm uma função de revisão de anexos — PDFs (plantas, projetos) podem ser abertos numa ferramenta de marcação/desenho, pra quem analisa comentar e aprovar/reprovar direto em cima do arquivo.

## Pontos de atenção
- A documentação de produto do SoGov (fonte Notion) nunca define formalmente "zona" e "uso" — trata como óbvio e só descreve a tela. A seção "O conceito real, fora do sistema" acima preenche essa lacuna com conhecimento geral de planejamento urbano, **não** com algo confirmado pela SOGO/produto — na dúvida sobre terminologia oficial do sistema, a fonte é [[QA Workspace/04 Conhecimento/Módulos/Processos Urbanísticos|Processos Urbanísticos]].
- Os valores de exemplo (CA 1,5, TO 70% etc.) são ilustrativos, não refletem nenhum cliente real do SoGov.

## Referências
- [[QA Workspace/04 Conhecimento/Módulos/Processos Urbanísticos|Processos Urbanísticos]] — documentação do produto (telas, regras, API de revisão de anexos).
- Estatuto da Cidade (Lei federal 10.257/2001) e Plano Diretor municipal — base legal brasileira do zoneamento urbano (conhecimento geral, sem link específico de nenhum município).
