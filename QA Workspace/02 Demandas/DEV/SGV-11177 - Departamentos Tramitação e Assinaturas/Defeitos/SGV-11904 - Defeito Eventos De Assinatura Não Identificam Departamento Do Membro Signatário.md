---
tags:
  - defeito
  - qa
  - servicos-pj
task: "11904"
pai: "SGV-11177"
prioridade: media
status: aberto
data_inicio: 2026-09-29
data_fim: ""
responsavel: Rafael
aguardando:
pontos:
cadastrado_por: ""
modulo: servicos-pj
ambiente: DEV
---
# Eventos de assinatura não identificam o departamento do membro signatário

### Descrição

Durante a validação real da SGV-11177 (Parte 4 da epic SGV-9296) foi identificado que, ao solicitar assinatura de um cidadão que é membro de um departamento, o componente de eventos de assinatura mostra apenas o nome de exibição e o cargo do cidadão — sem identificar o departamento que ele representa naquela assinatura. O Figma amarra a identidade do signatário à sua lotação no departamento; hoje essa amarração se perde no evento.

---

### Passo a passo para reproduzir

**Dado** que uma assinatura é solicitada a um cidadão que é membro de um departamento
**Quando** o servidor consulta os eventos de assinatura desse documento
**Então** verifico que o evento mostra só `$Nome_exibição ($Cargo)`, sem o trecho `como $Nome_depto (Representando $RazaoSocial)`

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Desenvolvimento/) [🔍](evidencia://11904)

Pendência — nenhuma evidência (vídeo/print) anexada ainda. Rafael vai anexar depois.

---

### Resultado Esperado

O evento deve seguir a string completa definida no Figma:

`$Assinatura_textual ($Cargo) $Sigla solicitou a assinatura de $Nome_exibição ($Cargo) como $Nome_depto (Representando $RazaoSocial), neste documento.`

Ver [[01 - Demanda#^c20|C20]] e [[03 - Casos de teste#^ct-020|CT-020]].

---

### Critérios de aceite

- [ ] O evento de assinatura de um membro de departamento identifica o cidadão (nome de exibição + cargo) **e** o departamento que ele representa (nome do departamento + razão social), seguindo a string completa definida no Figma
- [ ] O comportamento é consistente em todos os eventos relacionados a essa assinatura (não só num evento isolado)

---

### Casos de Teste Básicos

#### **CT-B01 Evento de assinatura mostra cidadão e departamento juntos**

**Dado** que uma assinatura é solicitada a um cidadão membro de um departamento
**Quando** o servidor consulta o evento correspondente
**Então** o texto do evento segue o padrão `$Assinatura_textual ($Cargo) $Sigla solicitou a assinatura de $Nome_exibição ($Cargo) como $Nome_depto (Representando $RazaoSocial), neste documento`

**Execução Passou?**
- [ ] Sim
- [x] Não
- [ ] Não se aplica

**Evidências de Testes:**

Pendência — nenhuma evidência anexada ainda.

---

### Ambiente

- Versão: a definir
- Ambiente: Desenvolvimento

---

### Informações adicionais

- Demanda relacionada: [[01 - Demanda|SGV-11177]]
- Observações: achado durante a validação real do pacote QA de SGV-11177 — [[03 - Casos de teste#^ct-020|CT-020]]. Mesma causa de fundo do selo de assinatura, ver [[SGV-11905 - Defeito Selo De Assinatura Não Traz Departamento Do Membro Signatário|SGV-11905]] (defeito irmão).
- Histórico:
    - 2026-09-29 - 🐛 Defeito cadastrado (da SGV-11177)
