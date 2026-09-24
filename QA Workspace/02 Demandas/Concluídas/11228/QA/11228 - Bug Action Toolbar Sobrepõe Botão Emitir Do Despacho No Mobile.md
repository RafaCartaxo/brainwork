---
tags:
  - bug
  - qa
task: "11228"
pai: ""
prioridade: media
status: aberto
data_inicio: 2026-09-01
data_fim: ""
responsavel: Rafael
cadastrado_por: ""
modulo: despacho
ambiente: HML
---
# Action toolbar sobrepõe botão Emitir do despacho no mobile (iPhone)

### Descrição

Durante validação foi identificado que, a partir do mobile (iPhone), a action toolbar do SoGov fica sobreposta ao botão **Emitir** do despacho, impossibilitando clicar nele diretamente. É como se a toolbar ficasse fixa no final do scroll e, por consequência, ficasse por cima do botão de emitir.

**Contorno encontrado**: clicar no campo de texto do despacho, abrindo o teclado, e em seguida ocultar o teclado — só então fica visível o espaço entre a action toolbar do SoGov e a barra do navegador do celular, onde é possível clicar em Emitir.

Print 1 (grifado) marca a área onde Responder/Cancelar/Emitir deveriam ficar totalmente visíveis, sem sobreposição — é a referência de como deveria aparecer. Prints 2 e 3 são frames da gravação mostrando o problema: só o botão **Responder** fica visível, Cancelar e Emitir ficam escondidos abaixo da borda da tela, cobertos pela action toolbar.

Rafael sinalizou que este é um caso de um problema mais amplo de responsividade no componente de emissão de despachos (disposição dos botões e afins) — protótipo de referência (Figma): https://www.figma.com/design/tHHe07M59ZKpOWCvwwRJUG/SOGOV---Style-Guide?node-id=13685-53035

---

### Passo a passo para reproduzir

Dado que eu acesso o SoGov pelo mobile (iPhone)
E abro um despacho pra emitir
Quando eu tento clicar no botão **Emitir**
Então verifico que o botão fica coberto pela action toolbar, impossibilitando o clique
E, ao clicar no campo de texto do despacho e depois ocultar o teclado, o botão Emitir fica acessível no espaço entre a action toolbar e o navegador — contorno que confirma a sobreposição

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evidências/Homologação/) [🔍](evidencia://11228)

![[11228 - action toolbar sobre botao emitir (grifado).png]]
*Área grifada: onde Responder/Cancelar/Emitir deveriam ficar visíveis sem sobreposição.*

![[11228 - toolbar cobrindo emitir 1.png]]
*Cancelar e Emitir cobertos pela action toolbar — só Responder aparece.*

![[11228 - toolbar cobrindo emitir 2.png]]
*Mesmo problema, outro momento da gravação.*

---

### Resultado Esperado

- No mobile, o botão Emitir do despacho fica visível e clicável, sem sobreposição da action toolbar

---

### Critérios de aceite

- [ ] No mobile (iPhone), os botões Responder, Cancelar e Emitir ficam todos visíveis e clicáveis, sem precisar do contorno (abrir/ocultar teclado)
- [ ] O botão Emitir é clicável diretamente, sem depender do espaço entre a action toolbar e o navegador

---

### Casos de Teste Básicos

#### **CT-B01 Botão Emitir acessível no mobile sem contorno**

**Dado** que eu acesso o SoGov pelo mobile (iPhone) e abro um despacho pra emitir
**Quando** eu tento clicar no botão Emitir, sem usar nenhum contorno
**Então** o botão está visível e clicável, sem sobreposição da action toolbar

**Execução Passou?**
- [ ] Sim
- [ ] Não

**Evidências de Testes:**

---

### Ambiente

- Versão:
- Ambiente: Homologação
- Dispositivo: iPhone (mobile, Safari)

---

### Informações adicionais

- Demanda relacionada:
- Observações: Rafael sinalizou que faz parte de um padrão mais amplo de problemas de responsividade no componente de emissão de despachos (disposição de botões e afins) — protótipo de referência: https://www.figma.com/design/tHHe07M59ZKpOWCvwwRJUG/SOGOV---Style-Guide?node-id=13685-53035. Não criei card separado pros outros problemas mencionados por não ter evidência/detalhe concreto ainda — se surgir achado específico, cadastrar à parte.
- Histórico:
    - 2026-09-01 - 🐛 Bug cadastrado
