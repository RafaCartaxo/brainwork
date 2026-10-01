---
tags:
  - defeito
  - qa
  - servicos-pj
task: "11924"
pai: "SGV-11177"
prioridade: media
status: resolvido
data_inicio: 2026-09-29
data_fim: "2026-09-30"
responsavel: Rafael
aguardando:
pontos:
cadastrado_por: ""
modulo: servicos-pj
ambiente: DEV
---
# Assinatura bloqueada entre departamentos diferentes do mesmo cidadão PJ

### Descrição

Não é possível solicitar assinatura de departamentos diferentes do mesmo cidadão PJ — a API bloqueia a segunda solicitação achando que já perguntou pro cidadão. Contraria a regra confirmada: um documento pode ter mais de um departamento como signatário, inclusive departamentos diferentes da mesma PJ (mesma regra de destinatário de tramitação, [[QA Workspace/02 Demandas/Concluídas/11184/QA/11184 - Funcionalidade Departamentos Encaminhar Documentos E Despachos|SGV-11184]], estendida à assinatura).

**Retestado em 30/09/2026, falha novamente** — inclusive quando o cidadão já **assinou** (não só foi solicitado) pelo Departamento A: solicitar pelo Departamento B continua bloqueado/incorreto. Manifestação adicional observada no reteste: a solicitação de assinatura pro membro do departamento aparece na **lista de documentos pessoal** do cidadão, não na lista do departamento a que ele pertence — reforça que a causa raiz é o sistema escopando a solicitação pelo cidadão em si, não pelo departamento/signatário específico.

---

### Passo a passo para reproduzir

**Dado** que uma assinatura já foi solicitada a um departamento de um cidadão PJ
**Quando** o solicitante configura uma nova solicitação de assinatura a um departamento diferente do mesmo cidadão PJ
**Então** verifico que a API retorna erro, bloqueando a solicitação

Resposta da API:

```json
{
    "errors": [
        {
            "message": "system.messages.you-have-already-been-asked-once-with-sogov",
            "locations": [{"line": 2, "column": 3}],
            "path": ["createSignatures"],
            "extensions": {"code": "REDWOODJS_ERROR"}
        }
    ],
    "data": null
}
```

Toast exibido: "Você já foi solicitado assinar em alguns dos locais neste setor com assinatura SOGOV."

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://11924)

**Antes da correção:**
![[11924 - Assinatura bloqueada entre departamentos, incorreto.mp4]]

**Retestado e aprovado (30/09/2026):**
![[11924 - Assinatura entre departamentos diferentes aceita, ok.mp4]]

---

### Resultado Esperado

Solicitação de assinatura a um departamento diferente do mesmo cidadão PJ é aceita normalmente, sem bloqueio. Ver [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/01 - Demanda#^c35|C35]] e [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/03 - Casos de teste#^ct-035|CT-035]].

---

### Critérios de aceite

- [x] Solicitar assinatura a um departamento diferente do mesmo cidadão PJ não é bloqueado pela checagem "já perguntou"

---

### Casos de Teste Básicos

#### **CT-B01 Assinatura a segundo departamento da mesma PJ não é bloqueada**

**Dado** que uma assinatura já foi solicitada a um departamento de um cidadão PJ
**Quando** o solicitante configura uma nova solicitação a um departamento diferente do mesmo cidadão PJ
**Então** a solicitação é aceita, sem o erro `you-have-already-been-asked-once-with-sogov`

**Execução Passou?**
- [x] Sim
- [ ] Não
- [ ] Não se aplica

**Evidências de Testes:**

![[11924 - Assinatura entre departamentos diferentes aceita, ok.mp4]]

---

### Ambiente

- Versão: a definir
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/01 - Demanda|SGV-11177]]
- Observações: achado durante a validação da SGV-11177 — [[QA Workspace/02 Demandas/DEV/SGV-11177 - Departamentos Tramitação e Assinaturas/03 - Casos de teste#^ct-035|CT-035]] (critério C35, criado a partir deste achado). Card reaproveitado: a suspeita original registrada aqui (campo cargo preenchido com CPF, CT-025) era autofill do navegador, não bug — CT-025 confirmado aprovado. Evidência da suspeita descartada, preservada por contexto:
  ![[11924 - Cargo auto-preenchido com CPF, correto, falso cadastro.mp4]]
- Histórico:
    - 2026-09-29 - 🐛 Defeito cadastrado (suspeita original: campo cargo com CPF, CT-025)
    - 2026-09-29 - 🔁 Conteúdo do card substituído — suspeita original era autofill do navegador (CT-025 aprovado); achado real é o bloqueio entre departamentos diferentes da mesma PJ (CT-035)
    - 2026-09-30 - 🔴 Reaberto — reteste falha novamente, mesmo com assinatura já concluída (não só solicitada) pelo Departamento A. Achado adicional: solicitação pro membro aparece na lista pessoal do cidadão, não na lista do departamento (mesma causa raiz de escopo)
    - 2026-09-30 - ✅ Retestado e aprovado — assinatura a departamentos diferentes da mesma PJ aceita normalmente
