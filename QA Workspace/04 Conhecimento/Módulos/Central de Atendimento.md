---
title: Central de Atendimento
tags:
  - qa
  - conhecimento
  - sogov
  - central-atendimento
tipo: modulo
revisado: 2026-10-20
fonte: https://app.notion.com/p/alfa-group/Central-de-atendimento-2e72aec67d308006baeedd5bdd5d2f1a
fonte_criado: 2026-01-13 (Ivo Costa)
fonte_ultima_edicao: 2026-01-13 (Ivo Costa)
---
# Central de Atendimento

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-10-20 — a página do Notion continua sendo a fonte de verdade externa; esta cópia é o acervo local pesquisável. Sem task própria (campo `Task` vazio). Export bem mais curto que o esperado pro conceito — a Central de Atendimento é citada como o portal externo em várias outras docs do vault ([[QA Workspace/04 Conhecimento/Módulos/Divulgar Documento|Divulgar Documento]], [[QA Workspace/04 Conhecimento/Módulos/Processos Urbanísticos|Processos Urbanísticos]], [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão|Usuário Cidadão]], [[QA Workspace/04 Conhecimento/Módulos/Rastrear Documento|Rastrear Documento]]), mas essa página do Notion parece cobrir só uma atualização pontual dela (botão de acessar documento na verificação de assinatura) — não a definição geral da Central. Ver Dúvidas em aberto.

## Visão geral
- A Central de Atendimento é o portal público/externo do SoGov — área acessada por cidadãos (com ou sem login, dependendo da funcionalidade) pra consultar documentos divulgados, zoneamento urbano, rastrear processos e verificar a autenticidade de assinaturas. Cada doc do vault que toca uma funcionalidade exposta nela documenta sua própria parte (ver Referências); esta nota reúne o que é específico da Central em si.

## Regras de negócio

### Botão "Acessar documento" na verificação de autenticidade de assinatura (13/01/2026)
> Contexto: ao verificar a autenticidade de uma assinatura — seja pela Central de Atendimento, seja pelo link de verificação embutido no documento assinado — o resultado passa a ter um botão **"Acessar documento"**, abrindo o documento numa nova aba do navegador.

- **Visualização**: tem que corresponder exatamente ao artefato verificado — se a verificação é de um anexo específico, o CTA abre **só aquele anexo**, não o documento inteiro.
- **Formato**: documento exibido em nova aba, em **PDF**.
- **Documentos sigilosos/anônimos**: visualização **indisponível**, independente de a parte assinada em si (ex.: o despacho específico) ser ou não sigilosa/anonimizada — basta o documento ter **qualquer** item sigiloso em algum lugar pra nada dele poder ser exibido.
	- Botão fica `disabled`, com tooltip: *"O conteúdo deste documento possui sigilo e não pode ser acessado."*
	- Quando bloqueado, o aviso aparece junto de um ícone de info, com a mesma mensagem na tooltip.
	- Vale pros dois pontos de entrada: verificação pela Central de Atendimento e verificação pelo link no PDF do documento.

## Comportamentos observados em teste
<!-- O que foi aprendido validando: comportamentos não documentados, pegadinhas, efeitos colaterais -->
- Ainda não testado — importação é só a documentação de referência.

## Dúvidas em aberto
- [ ] Esta página do Notion ("Central de atendimento") cobre só a atualização do botão de verificação de assinatura — não tem uma "Definição geral" da Central de Atendimento como um todo (permissões de acesso, estrutura de navegação, o que fica disponível sem login vs. com login). Pode haver uma doc separada no Notion, não localizada ainda.
- [ ] Existe uma página-irmã no Notion, **"Verificação de autenticidade" (também 13/01/2026)**, linkada a partir de [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]] (citada lá como não importada) — mesma data de criação desta página, provavelmente do mesmo pacote de trabalho do Ivo Costa. Ainda não importada; pode detalhar melhor a tela de verificação como um todo (hoje só o botão novo está documentado).
- [ ] Não fica claro se "a verificação de autenticidade" é algo que fica **dentro** da Central de Atendimento (uma tela acessível por ali) ou se é uma funcionalidade à parte, só mencionada nesta doc por tocar também o fluxo da Central. A estrutura de navegação da Central não veio no export.

## Cards relacionados
<!-- SGVs validados que tocam este módulo -->
- Sem SGV vinculado — documentação de referência.

## Referências
<!-- Docs do repo (caminho), links externos, leis -->
- Notion (fonte): ver `fonte` no frontmatter.
- [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|Assinaturas]] — base do fluxo de assinatura e verificação de autenticidade que esta atualização estende.
- [[QA Workspace/04 Conhecimento/Módulos/Divulgar Documento|Divulgar Documento]] — documentos oficiais divulgados, consultados na Central.
- [[QA Workspace/04 Conhecimento/Módulos/Processos Urbanísticos|Processos Urbanísticos]] — consulta de zoneamento, também na Central.
- [[QA Workspace/04 Conhecimento/Módulos/Rastrear Documento|Rastrear Documento]] — outra funcionalidade de consulta externa.
- [[QA Workspace/04 Conhecimento/Módulos/Usuário Cidadão|Usuário Cidadão]] — regras de acesso do cidadão (login, gov.br) que alimentam quem acessa a Central.
