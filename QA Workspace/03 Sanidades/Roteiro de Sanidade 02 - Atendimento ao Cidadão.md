---
title: Roteiro de Sanidade 02 — Atendimento ao Cidadão
tags:
  - qa
  - sanidade
  - sogov
  - atendimento-cidadao
tipo: roteiro-sanidade
revisado: 2026-07-21
fonte: https://app.notion.com/p/alfa-group/Roteiro-de-Sanidade-02-Atendimento-ao-Cidad-o-2fd2aec67d308085bbf2dc3448f835e7
ags:
  - AGS-76
  - AGS-12
---
# Roteiro de Sanidade 02: Atendimento ao Cidadão

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-07-21. A página do Notion é a fonte de verdade externa; esta cópia é o acervo local pesquisável. Roteiro de execução manual (smoke test) dos fluxos ponta a ponta de Atendimento ao Cidadão. Depende da instância criada em [[Roteiro de Sanidade 01 - Implantação]].

> [!abstract] Casos de teste vinculados (Notion)
> Sanidade 009, 011, 012, 013 — "Roteiro de Sanidade 02: Atendimento ao Cidadão".

## Bugs com impacto em cenários do roteiro
- [BUG] (Sanidade-003/2026) Prazo não é adicionado em documentos abertos por cidadão
- [BUG] (Sanidade-004/2026) CPF é exportado com máscara incorreta no download do documento aberto por cidadão
- [BUG] (Sanidade-007/2026) Documento criado e cancelado por cidadão permite reabertura e novo cancelamento indevidamente
- [BUG] (Sanidade-004/2026) Download de documento temporário não corresponde à versão editada
- [BUG] (Sanidade-006/2026) Tela de posicionamento de assinatura fica em loading infinito ao emitir despacho com múltiplos anexos e múltiplos signatários
- [BUG] (Sanidade-012/2026) Cidadão não é notificado quando o documento é aberto pelo Servidor
- [BUG] Os anexos de abertura não são baixados ao baixar documento como cidadão

## Roteiro

### 1. Acessar o cadastro de Assuntos e Serviços
Acesse o sistema como **Administrador** → menu **Assuntos e Serviços** → **Criar novo serviço**.

### 2. Cadastrar o assunto/serviço "Retirada de Entulho"
**Dados do assunto**
- Nome: Retirada de Entulho
- Descrição: solicitação de retirada de entulho em via pública ou residência.
- Módulo: Atendimento ao Cidadão · Categoria: Serviços Urbanos

**Natureza e Privacidade** — Permite abertura externa (herdado do módulo).

**Regras de tramitação**
- Setores criadores: manter existentes e garantir **SEOURB**
- Setores que recebem e tramitam: manter existentes e garantir **SEOURB, SEFAZ**
- Setores destino: adicionar **SEOURB** (Secretaria de Obras e Urbanismo)
- Receberá automaticamente: SEOURB · Interações externas: SEOURB

**Configurações adicionais**
- Cidadão interage só na abertura: Não
- Prazo do assunto: Sim — 20 dias úteis
- Prorrogação: Sim — 3 prorrogações de 2 dias
- Numeração inicial: Sim — 1 · Mantém sequencial após mudança de ano: Não

**Formulário do Serviço**
- Descrição do problema → texto grande (herdado do módulo)
- Telefone/WhatsApp → número (telefone)
- Ponto de referência → texto pequeno (opcional)
- Endereço do local do entulho → Endereço
- Local → Mapa
- Fotos do problema → anexo (PDF, JPG, JPEG, PNG)

Salve o assunto e serviço.

### 3. Cadastrar cidadão
Acesse a **Central de Atendimento** como cidadão → **Entrar** e **Cadastrar-se**.
- Cadastro para você ou empresa? → Para mim (CPF)
- Nome de exibição: primeiro + último nome
- E-mail: usar [gerador de e-mail temporário](https://www.invertexto.com/gerador-email-temporario)
- Senha: `Teste@123`

Finalize, acesse o e-mail recebido e confirme o cadastro.

### 4. Fluxo 01 — Atendimento completo

**4.1 Abertura da solicitação (Cidadão)** — Login como cidadão na Central de Atendimento → nova solicitação `Atend. ao Cidadão → Retirada de Entulho` → preencher obrigatórios → acompanhar em **Minhas Solicitações**.
> [!check] Resultado esperado
> Solicitação criada; número do documento gerado corretamente; processo encaminhado ao SEOURB; visível em Minhas Solicitações.

**4.2 Atendimento inicial (Servidor – SEOURB)** — Login como servidor SEOURB → localizar na **Mesa de Documentos** → coluna **Em aberto** → despacho:
> Prezado(a) cidadão(ã), Recebemos sua solicitação com sucesso! Agradecemos por entrar em contato conosco. Nossa equipe de análise já está avaliando o seu pedido com atenção e cuidado, para garantir que o atendimento seja realizado com qualidade de agilidade. Agradecemos pela parceria em cuidar da cidade junto conosco.

Emitir o despacho.
> [!check] Resultado esperado
> Despacho registrado; evento na timeline; cidadão notificado.

**4.3 Resposta do cidadão (Cidadão)** — Acessar via Notificações → resposta "Entulho removido!" + anexar imagem (JPG/JPEG/PNG) → enviar.
> [!check] Resultado esperado
> Resposta enviada; texto na timeline; imagem disponível para visualização/download; setor/servidor notificado.

**4.4 Finalização do atendimento (Servidor – SEOURB)** — Acessar via Notificações → encerrar a tramitação → verificar na coluna **Encerrado**.
> [!check] Resultado esperado
> Processo encerrado; status Encerrado; evento de encerramento na timeline; cidadão notificado.

**4.5 Avaliação do atendimento (Cidadão)** — Acessar via notificação de "Tramitação encerrada" → selecionar satisfação + comentário.
> [!check] Resultado esperado
> Avaliação registrada no documento (servidor e cidadão); comentário salvo corretamente.

### 5. Fluxo 02 — Tramitação entre setores e prazos

**5.1 Abertura com foco em prazo (Cidadão)** — Nova solicitação `Retirada de Entulho`, Descrição: "Entulho é de grande porte e está obstruindo a calçada." → acompanhar em Minhas Solicitações.
> [!check] Resultado esperado
> Solicitação criada; prazo de 20 dias úteis exibido no protocolo (conforme passo 2); processo encaminhado ao SEOURB.

**5.2 Tramitação intersetorial (Servidor – SEOURB)** — Coluna Em aberto → despacho para SEFAZ: "Necessário envio de fiscal de posturas para autuar o responsável antes da retirada." → emitir.
> [!check] Resultado esperado
> Processo segue na coluna Em tramitação da mesa SEOURB; aparece Em aberto na mesa SEFAZ.

**5.3 Prorrogação de prazo (Servidor – SEFAZ)** — Coluna Em aberto → Prorrogar Prazo, motivo: "Alta demanda de fiscalização externa no período." → salvar.
> [!check] Resultado esperado
> Prazo estendido em 2 dias (conforme config); contador de prorrogações atualizado (ex.: 1 de 3); evento na timeline e cidadão notificado.

> [!warning] Observação
> A prorrogação só pode ser feita após o documento atingir seu prazo máximo — verificar formas de testar cenários envolvendo prorrogação.

**5.4 Devolução e encerramento (SEFAZ → SEOURB)** — Em SEFAZ, despacho de resposta envolvendo SEOURB + anexar arquivo (Auto de Infração fictício). Como servidor SEOURB, verificar e **encerrar**.
> [!check] Resultado esperado
> Evento do documento e despachos na timeline; anexos da SEFAZ visíveis para SEOURB/cidadão/envolvidos; status final Encerrado.

### 6. Atendimento cancelado pelo cidadão

**6.1 Abertura (Cidadão)** — Nova solicitação `Retirada de Entulho` → obrigatórios → acompanhar.
> [!check] Resultado esperado
> Solicitação criada; número gerado; encaminhada ao SEOURB; visível em Minhas Solicitações.

**6.2 Atendimento inicial (Servidor – SEOURB)** — Coluna Em aberto → despacho (mesmo texto do 4.2) + anexar arquivo (PDF/JPG/JPEG/PNG) → emitir.
> [!check] Resultado esperado
> Despacho registrado; arquivo disponível; evento na timeline; cidadão notificado.

**6.3 Resposta e cancelamento (Cidadão)** — Acessar via Notificações → resposta "Devido a demora o entulho foi removido pela comunidade." + anexar imagem → enviar → **cancelar solicitação**.
> [!check] Resultado esperado
> Resposta enviada; texto na timeline; imagem disponível; setor/servidor notificado; documento atualizado para **Encerrado** em "Situação do documento" / "Situação para mim" / "Situação no meu setor".

### 7. Atendimento cancelado pelo servidor

**7.1 Abertura (Servidor)** — Como servidor SEOURB, nova solicitação `Retirada de Entulho`, **envolver cidadão como Solicitante** → obrigatórios. Como cidadão, acompanhar em Minhas Solicitações e **baixar documento completo**.
> [!check] Resultado esperado
> Solicitação criada; número gerado; encaminhada ao SEOURB; visível em Minhas Solicitações.

**7.2 Retificação (Servidor)** — Localizar na mesa SEOURB (passo 7.1) → retificar atualizando **todos** os campos preenchidos, incluindo anexos → informar justificativa → baixar documento completo.
> [!check] Resultado esperado
> Retificação realizada; dados do documento baixado são os atuais; dados exibidos são os atuais; evento de retificação (despacho) na timeline com a justificativa.

**7.3 Atendimento inicial com modelo (Servidor – SEOURB)** — Abrir **modelos de documentos** → criar modelo simples "Resposta padrão Atendimento inicial", **sem herança de dados**, assunto "Retirada de Entulho", compartilhar com todos os setores do módulo. Texto (não copiar/colar), com formatação:
> #### (Centralizado, fonte 14)
> Prezado(a) cidadão(ã),
>
> #### (Alinhado à esquerda, fonte 10)
> Recebemos sua solicitação com sucesso! Agradecemos por entrar em contato conosco. Nossa equipe de análise avaliação já está verificando o seu pedido com atenção e cuidado, para garantir que o atendimento seja realizado com qualidade e agilidade.
>
> #### (Alinhado à direita, fonte 12)
> Agradecemos pela parceria em cuidar da cidade junto conosco.

Salvar. Acessar o processo na coluna Em tramitação (passos 7.1 e 7.2) → despacho com o modelo → baixar documento completo.
> [!check] Resultado esperado
> Despacho registrado; documento disponível; evento na timeline; cidadão notificado.

**7.4 Tramitação e cancelamento (Servidor – SEOURB)** — Criar modelo simples "Resposta cancelamento", **com herança de dados**, assunto "Retirada de Entulho", compartilhar com todos os setores. Texto (não copiar/colar):
> Prezado(a) @solicitante,
>
> Informamos que nossa equipe realizou vistoria no local indicado, porém não foi constatada a presença de entulho conforme descrito na solicitação @Número do documento emissor.
>
> Dessa forma, considerando a inexistência da situação informada no momento da verificação, a demanda será cancelada.
>
> Permanecemos à disposição para novos registros, caso a situação seja identificada posteriormente.
>
> Atenciosamente @Setor destinatário,

Salvar. Localizar na mesa SEOURB (7.1/7.2) → despacho com o modelo + anexo da vistoria em PDF → **cancelar o processo** → baixar documento completo.
> [!check] Resultado esperado
> Despacho registrado; documento disponível com tarja **sem efeito**; evento na timeline; cidadão notificado; **documento cancelado não pode ser reaberto**; documento atualizado para Encerrado em "Situação do documento" / "Situação para mim" / "Situação no meu setor".

## Dúvidas em aberto
- [ ] Roteiro não define ambiente-alvo (DEV/HML) — confirmar.
- [ ] 7.4 depende do bug (Sanidade-007/2026) "cancelado permite reabertura indevida" estar resolvido — o resultado esperado ("não pode ser reaberto") é justamente o critério do bug.

## Referências
- Notion original: https://app.notion.com/p/alfa-group/Roteiro-de-Sanidade-02-Atendimento-ao-Cidad-o-2fd2aec67d308085bbf2dc3448f835e7
- Pré-requisito: [[Roteiro de Sanidade 01 - Implantação]]
