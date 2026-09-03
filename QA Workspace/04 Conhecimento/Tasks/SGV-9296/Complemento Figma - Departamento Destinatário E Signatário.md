---
tags:
  - qa
  - conhecimento
tipo: referencia
data_recebido: 2026-09-03
---
# Referência: Complemento Figma — departamento como destinatário e signatário

Material recebido de Rafael em 03/09/2026 (`~/Documentos/Complemento 11184.txt`, extraído do Figma), cruzado contra os 22 CTs da [[QA Workspace/02 Demandas/DEV/11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos|SGV-11184]]. Parte do conteúdo já foi incorporada lá (ver Histórico do card e da mesa); esta nota preserva **o que não entrou**, pra não se perder, e serve de contexto de apoio pra epic [[QA Workspace/04 Conhecimento/Tasks/SGV-9296/0 - SGV-9296 - Índice|SGV-9296]] como um todo.

> [!info] Não é fonte de critério de aceite da 11184
> Nada aqui vira CT sem confirmação de Rafael. É registro do que o Figma descreve, pra quando (e se) virar escopo de trabalho — desta ou de uma parte futura da epic.

## O que já foi incorporado à SGV-11184 (não repetido aqui)

Formato de exibição (parênteses), busca a partir de 3 caracteres, resultado expandido com cluster aninhado sob a PJ, CPF anonimizado, área de clique do accordion, regra de truncate. Ver CTs da 11184 e a Análise da mesa.

## 1. Seleção de membro individual do departamento como destinatário direto — **status: aguardando Rafael conferir**

O requisito técnico original da 11184 é explícito: *"a seleção direta de um membro do departamento não faz parte desta entrega"* — e os CTs de hoje testam justamente que isso **não** acontece (CT-010, por exemplo). O Figma descreve o oposto: um fluxo completo de selecionar um usuário lotado num departamento diretamente como destinatário (de despacho), com:

- Notificação direcionada só a essa pessoa, não ao departamento inteiro
- String de exibição própria: `$nome_exibição ($nome_cargo) - ($Nome_depto - $RazaoSocial)`
- Validação por token **liberada** nesse caso (diferente da solicitação pro departamento inteiro, onde token fica bloqueado)
- Múltiplos departamentos selecionados agrupam destinatários no accordion correspondente, mesma regra já existente na plataforma

**Pendência**: confirmar com Rafael se isso é (a) mudança de escopo da própria 11184, (b) conteúdo de uma parte futura da epic (ainda sem SGV), ou (c) não deveria estar em consideração agora.

## 2. Departamento como signatário de solicitação de assinatura — **status: fora do escopo desta entrega**

O requisito original da 11184 cobre só documento/despacho como **destinatário de tramitação** — não assinatura. O Figma traz um bloco extenso e estruturalmente separado ("Impacto em assinaturas") descrevendo:

- Departamento inteiro pode ser selecionado como signatário; todos os colaboradores lotados nele ficam aptos a assinar o local solicitado
- Header do componente de signatário muda quando o alvo é um departamento inteiro (não um signatário específico)
- Validação por token **bloqueada** quando o signatário é o departamento inteiro (mas liberada quando é um participante específico do departamento — item 1)
- Fluxo de posicionar selo só aparece se "Documentos possuem página de assinaturas separada" estiver desabilitado
- Strings de notificação completas por combinação de evento (solo doc, seq doc + anexos, doc + despacho, despacho + anexos, etc.), todas no padrão `$Assinatura_textual ($Cargo) $Sigla solicitou a assinatura de $Nome_depto (Representando $RazaoSocial) [...]`
- Conteúdo do selo aplicado: quando a solicitação é pro departamento — razão social, nome do departamento, papel; quando já assinado — razão social, departamento, nome de exibição (cargo), CNPJ, data/hora (GMT)
- Histórico ganha tratamento novo pro header de PJ com departamentos e participantes
- Mesmas regras de accordion/agrupamento de despacho valem pra assinatura (múltiplos departamentos agrupados no accordion correspondente)

Rafael confirmou (03/09/2026): fica só como material de contexto da epic — não entra na validação da 11184 nesta rodada. Foco desta entrega é só o requisito de tramitação já fechado.

## Fonte completa

Texto integral preservado em `~/Documentos/Complemento 11184.txt` (não copiado aqui verbatim pra não duplicar 160 linhas — esta nota resume o que importa pra decisão de escopo).
