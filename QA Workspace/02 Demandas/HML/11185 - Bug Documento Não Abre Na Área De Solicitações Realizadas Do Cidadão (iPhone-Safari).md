---
tags:
  - bug
  - qa
task: "11185"
pai: ""
prioridade: media
status: aberto
data_inicio: 2026-08-31
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: documento
ambiente: HML
---
# Documento não abre na área de solicitações realizadas do cidadão (iPhone/Safari)

### Descrição

Durante validação foi identificado que, ao acessar um documento como cidadão na área de solicitações realizadas, o documento não abre — clicar nele diversas vezes não tem efeito nenhum. **Achado especificamente no iPhone (Safari)** — ainda não confirmado se reproduz em outros dispositivos/navegadores (ver Observações).

---

### Passo a passo para reproduzir

Dado que acesso o sistema como cidadão pelo **iPhone (Safari)**
E vou até a área de solicitações realizadas
Quando clico em um documento pra abrir
Então verifico que, mesmo clicando diversas vezes, o documento não abre

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://11185)

*Capturada pelo celular (iPhone/Safari) — ainda não está no vault. Adicionar aqui quando o Rafael passar o arquivo.*

---

### Resultado Esperado

- Documento abre normalmente ao clicar, na área de solicitações realizadas do cidadão

---

### Critérios de aceite

- [ ] No iPhone (Safari), o documento abre ao clicar, na área de solicitações realizadas do cidadão
- [ ] Confirmado se o mesmo problema reproduz (ou não) em outro dispositivo/navegador — escopo do critério acima ajusta conforme a resposta

---

### Casos de Teste Básicos

#### **CT-B01 Documento abre na área de solicitações realizadas do cidadão (iPhone/Safari)**

**Dado** que acesso o sistema como cidadão pelo iPhone (Safari)
**E** vou até a área de solicitações realizadas
**Quando** clico em um documento pra abrir
**Então** o documento abre normalmente

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

### Ambiente

- Versão:
- Ambiente: Homologação
- Dispositivo: iPhone, Safari (mobile)

---

### Informações adicionais

- Demanda relacionada:
- Observações: Achado é específico do iPhone (Safari) até onde foi observado — ainda **não testado** em desktop nem em outros navegadores/dispositivos mobile. Se confirmar que só ocorre no iPhone/Safari, é sinal de algo na camada de renderização/JS específica do Safari mobile (vale já levar essa hipótese pro dev); se reproduzir em outros lugares também, o escopo do bug é mais amplo do que o título sugere hoje.
- Histórico:
    - 2026-08-31 - 🐛 Bug cadastrado
