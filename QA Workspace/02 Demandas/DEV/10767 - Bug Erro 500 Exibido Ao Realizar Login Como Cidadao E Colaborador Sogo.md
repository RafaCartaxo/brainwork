---
tags:
  - bug
  - qa
  - login
task: "10767"
prioridade: media
status: aberto
data_inicio: 2026-08-11
data_fim: ""
responsavel: Rafael
cadastrado_por: Rafael
modulo: login
ambiente: DEV
---
# Erro 500 exibido ao realizar login como cidadão e colaborador Sogo

### Descrição

Durante validação foi identificado que, ao realizar o login, é exibida a **tela de erro 500** e, em seguida, o redirecionamento acontece normalmente.

O comportamento ocorre nos **dois ambientes**: no ambiente **cidadão**, logando como cidadão; e no ambiente **Sogo**, logando como colaborador. O login **não é bloqueado** — a tela de erro aparece e o fluxo se completa em seguida.

Identificado na **sanidade da HotfixRelease 12.38.43.2**, em homologação.

---

### Passo a passo para reproduzir

Dado que estou na tela de login do **ambiente cidadão**
Quando realizo o login como **cidadão**
Então verifico que é exibida a **tela de erro 500** e, em seguida, o redirecionamento acontece normalmente

E o mesmo ocorre no **ambiente Sogo**, logando como **colaborador**.

---

### Evidências [📁](file:///home/sogov-rafael-cartaxo/Documentos/Sogov/Obsidian/BrainWork/QA%20Workspace/Evid%C3%AAncias/Desenvolvimento/) [🔍](evidencia://10767)

![[10767 - erro 500 no login como cidadao e colaborador.mp4]]

---

### Resultado Esperado

- O login é concluído **sem exibir tela de erro 500**, com o redirecionamento acontecendo direto

---

### Critérios de aceite

- [ ] O login como **cidadão**, no ambiente cidadão, não exibe a tela de erro 500
- [ ] O login como **colaborador**, no ambiente Sogo, não exibe a tela de erro 500
- [ ] O redirecionamento pós-login acontece **direto**, sem tela intermediária de erro

---

### Casos de Teste Básicos

#### **CT-B01 Login como cidadão não exibe erro 500**

**Dado** que estou na tela de login do ambiente **cidadão**
**Quando** realizo o login como **cidadão**
**Então** verifico que o login é concluído sem exibir a tela de erro 500, com redirecionamento direto

**Execução Passou?**
- [ ] Sim
- [x] Não

**Evidências de Testes:**

![[10767 - erro 500 no login como cidadao e colaborador.mp4]]

---

#### **CT-B02 Login como colaborador não exibe erro 500**

**Dado** que estou na tela de login do ambiente **Sogo**
**Quando** realizo o login como **colaborador**
**Então** verifico que o login é concluído sem exibir a tela de erro 500, com redirecionamento direto

**Execução Passou?**
- [ ] Sim
- [x] Não

**Evidências de Testes:**

![[10767 - erro 500 no login como cidadao e colaborador.mp4]]
*Mesma gravação cobre CT-B01 e CT-B02.*

---

### Ambiente

- Versão: **12.38.43.2** (HotfixRelease)
- Ambiente: Desenvolvimento — **posição na esteira de correção**. O defeito foi **identificado em homologação**, na sanidade da HotfixRelease 12.38.43.2; o card nasce em `DEV/` por ser bug novo ainda não corrigido em nenhum ambiente ([[Sistema/Contexto/PADROES_QA#Organização de Bugs|PADROES_QA]]).

---

### Informações adicionais

- Demanda relacionada:
- Observações:
    - **Não bloqueia o login** — a tela de erro 500 aparece e o fluxo se completa em seguida. O impacto é de percepção: é a primeira tela do produto e atinge tanto **cidadão** quanto **colaborador**.
    - Atinge **duas superfícies distintas** (ambiente cidadão e ambiente Sogo), o que sugere causa comum na etapa de autenticação/redirecionamento e não em uma tela específica — vale o dev checar antes de tratar como dois defeitos.
    - Encontrado em **sanidade de release de hotfix**, não em validação de demanda. Não foi apurado nesta sessão se o erro **foi introduzido pela** 12.38.43.2 ou se já existia antes — vale confirmar, porque muda a urgência.
- Histórico:
    - 2026-08-11 - 🐛 Bug cadastrado (identificado na sanidade da HotfixRelease 12.38.43.2, em homologação)
