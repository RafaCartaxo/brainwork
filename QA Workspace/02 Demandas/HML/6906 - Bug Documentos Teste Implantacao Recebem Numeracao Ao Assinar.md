---
tags:
  - bug
  - qa
  - assinatura
task: "6906"
prioridade: media
status: aberto
data: 2026-07-22
data_inicio: 2026-07-22
responsavel: Rafael
modulo: assinaturas
ambiente: HML
---
# Assinar documento em instância Em Implantação gera documento com numeração (escapa da limpeza da implantação)

### Descrição

Durante validação foi identificado que a assinatura de documento em instância **Em Implantação** agora é concluída com sucesso (o bug original foi resolvido), porém os documentos assinados passam a ser gerados **com numeração**. Como a implantação da prefeitura apaga apenas os documentos "Sem numeração", esses documentos de teste — criados enquanto a prefeitura ainda estava Em Implantação — permanecem na base do cliente como documentos válidos após a implantação. Comportamento incorreto.

---

### Passo a passo para reproduzir

Dado que a prefeitura esteja Em Implantação
E existam documentos de teste criados nesse período
Quando o documento é assinado
Então o documento é gerado com numeração
E ao concluir a implantação a limpeza de documentos "Sem numeração" não o alcança
E o documento de teste permanece na base do cliente como documento válido

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://6906)

![[6906 - documentos de teste da implantacao ganham numeracao reaberto em homologacao.mp4]]

---

### Resultado Esperado

Documentos de teste criados durante a implantação **não devem permanecer como válidos** após a implantação. A assinatura em instância Em Implantação não deve resultar em documentos que escapem da limpeza — os documentos de teste não devem receber numeração definitiva, ou a limpeza da implantação deve alcançá-los.

---

### Critérios de aceite

- [ ] Assinar documento em instância Em Implantação não deixa documentos de teste válidos na base após a implantação
- [ ] Documentos de teste criados durante a implantação são removidos pela limpeza (ou não recebem numeração definitiva que os torne válidos)

---

### Casos de Teste Básicos

- **CT-B01 Documento de teste assinado durante a implantação não permanece válido após implantar**
    Dado que a prefeitura esteja Em Implantação
    E um documento de teste tenha sido assinado nesse período
    Quando a implantação da prefeitura é concluída (limpeza de documentos "Sem numeração")
    Então o documento de teste não deve permanecer na base do cliente como documento válido

    - Execução Passou?
        - [ ] <span style="color:#2ecc71">Sim</span>
        - [x] <span style="color:#e74c3c">Não</span>

    - Evidências de Testes: ![[6906 - documentos de teste da implantacao ganham numeracao reaberto em homologacao.mp4]]

---

### Ambiente

- Versão:
- Ambiente: Homologação

---

### Informações adicionais

- Demanda relacionada: SGV-6906
- Observações: Reaberto em homologação. O bug original ("Não é possível assinar documento em instância Em Implantação") foi resolvido — a assinatura agora ocorre com sucesso. Novo achado: os documentos assinados ganham numeração e, por isso, escapam da limpeza de documentos "Sem numeração" da implantação, ficando como válidos na base do cliente. Gate de doc (leve): [[QA Workspace/04 Conhecimento/Módulos/Assinaturas|doc de Assinaturas]] e [[QA Workspace/04 Conhecimento/Módulos/Gerar Documento|doc de Gerar Documento]] não descrevem a regra de limpeza de documentos "Sem numeração" na implantação nem a atribuição de numeração no contexto Em Implantação — comportamento não coberto pela doc (silêncio/gap, fluxo 8), sem divergência a registrar.
- Histórico:
    - 2026-07-22 - 🔴 Reaberta em homologação (Rafael): assinatura Em Implantação OK, mas documentos de teste recebem numeração e escapam da limpeza da implantação
</content>
</invoke>
