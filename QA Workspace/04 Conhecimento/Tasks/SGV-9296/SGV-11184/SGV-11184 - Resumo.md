---
tags:
  - qa
  - conhecimento
---
# SGV-11184 — Resumo em linguagem simples

> Parte 2 da epic [[QA Workspace/04 Conhecimento/Tasks/SGV-9296/SGV-9296 - Índice|SGV-9296]] — irmã da [[QA Workspace/02 Demandas/DEV/11083 - Funcionalidade Departamentos Para Cidadao PJ|SGV-11083 (Parte 1)]]. Detalhe técnico (RFs, critérios, CTs) fica no [[QA Workspace/02 Demandas/DEV/11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos|card]] e na [[QA Workspace/04 Conhecimento/Tasks/SGV-9296/SGV-11184/SGV-11184 - Refinamento Departamentos Encaminhar Documentos E Despachos|mesa de refinamento]]. Esta nota é só o "o que é e por quê".

## O que é

A Parte 1 (SGV-11083) criou o cadastro de **departamentos** — unidades dentro de uma empresa (Pessoa Jurídica), cada uma com nome, e-mail e participantes próprios. Só que ter o cadastro não adianta se ninguém consegue *mandar um documento pra ele*. É isso que a Parte 2 entrega: usar o departamento de verdade na tramitação.

Com esta entrega, um servidor passa a poder:
- Escolher um **departamento** (em vez de uma pessoa) como destinatário, tanto na abertura de um documento quanto num despacho.
- O departamento é avisado por e-mail quando algo chega pra ele.
- Quando alguém de fora clica no link desse e-mail, o sistema sabe registrar que aquele departamento acessou o documento — sem precisar de login pra isso.

## Problema / Problemática

Hoje, quando a prefeitura precisa mandar algo pro setor certo de uma empresa (o Financeiro, o Jurídico, uma regional), o sistema só oferece dois caminhos, e os dois são ruins:

- Mandar pro **CNPJ "raiz"** da empresa — genérico demais, ninguém sabe quem vai ver.
- Mandar pro **contato pessoal** de quem estava cuidando do assunto — funciona até a pessoa mudar de função, e aí a comunicação se perde.

O resultado prático é que boa parte dessa comunicação acaba acontecendo **fora da plataforma** (telefone, e-mail avulso, WhatsApp). Departamento resolve o problema de endereçamento; esta entrega (Parte 2) é o que faz esse endereçamento realmente funcionar no fluxo de documentos e despachos.

## Resultado esperado da entrega

- **Selecionar o departamento certo**: na abertura de um documento (campo pessoa configurado pra Pessoa Jurídica) e no destinatário de um despacho, o servidor encontra e escolhe um departamento — nunca uma pessoa específica dele. Só aparecem departamentos ativos, da mesma prefeitura/instância.
- **Sem furo de segurança na seleção**: se o departamento for excluído ou suspenso entre o servidor escolher e salvar, a operação é recusada por inteiro — nunca fica "meio salva".
- **Notificação sem barulho**: o departamento recebe um e-mail a cada encaminhamento de verdade — nunca em dobro, mesmo que o e-mail do departamento seja igual ao de um membro, e mesmo que o mesmo aviso chegue duas vezes por engano no sistema.
- **Acesso externo rastreável e seguro**: o link que vai no e-mail do departamento permite ver o documento sem exigir cadastro — mas cada acesso fica registrado (com validações reais por trás: o link é único por departamento, e só funciona se o departamento realmente estiver ligado àquele documento). O link nunca deixa a pessoa responder, assinar ou fazer qualquer coisa além de olhar — e nunca revela informação nenhuma se for adulterado ou inválido.
- **Documento e PDF mostram o departamento certo**: em vez de aparecer só um nome de pessoa, o PDF e as telas mostram "Nome do departamento — Razão social da empresa", deixando claro que a resposta é institucional, não de uma pessoa só.

## Onde isso mexe na prática

- Campo de destinatário na **abertura de documento** (quando o campo aceita Pessoa Jurídica).
- Campo de destinatário de **despacho**.
- **E-mails de notificação** que já existem hoje (reaproveitados, com o departamento no lugar da pessoa).
- **PDF** do documento e do despacho (rodapé/representação do destinatário).
- Uma tela nova de "acesso pelo link do departamento" — visualização só, sem exigir login.
