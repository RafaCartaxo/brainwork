---
prioridade: media
origem: repo
pontos_alocados: ""
---

# SGV-10735 — Criação da feature de Integrações (API e-SIC)

**Ticket de origem:** SGV-10735 no Notion ("[DEV][PARTE 2] Criação da feature de integrações"), item filho de SGV-9657 ("[Melhoria-dev] API esic - Melhorias nos dados que são disponibilizados na API...").

> [!info]- Navegação QA/DEV
> **README do card:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/00 README|Abrir README do card]]
> **Demanda:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/01 - Demanda]]
> **Plano de teste:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/02 - Plano de teste]]
> **Casos de teste:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/03 - Casos de teste]]
> **Validação:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/04 - Validação dev]]
> **Preparação Qase:** [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10735 - Criação da feature de integrações/00 QA/05 - Preparação Qase]]

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

---

## Problema / contexto

Clientes do SoGov precisam disponibilizar os dados das solicitações e-SIC para sistemas externos. Até então não havia interface para o time interno liberar esse acesso — cada habilitação dependia de intervenção manual direto no banco, sem registro de quem alterou o quê.

## Objetivo

Página de Integrações no ambiente Técnico, onde o time interno ativa a API e-SIC por cliente, obtém as credenciais de acesso, define quais módulos ficam expostos e consulta o histórico de alterações — de forma rastreável, sem alteração manual em banco.

### Entrega desta capacidade

Front-end da feature de integrações (tela de ativação, credenciais, seleção de módulos, desativação e histórico). O backend de credenciais (ativação/desativação, geração e persistência) já está implementado (MR aprovado). Uso exclusivamente interno, no ambiente Técnico.

---

## Decisões de produto

- Opção "Integrações" fica no menu de ações de cada cliente, desabilitada (mas visível) quando o cliente está inativo.
- Ativação gera duas credenciais automaticamente (identificador do cliente, chave secreta), com efeito imediato — sem passo de salvamento.
- Credenciais sobrevivem à desativação: reativar não gera credenciais novas e restaura o estado anterior.
- A integração expõe só os módulos selecionados, restritos aos módulos contratados pelo cliente; pode ficar ativa sem nenhum módulo selecionado.
- Mensagens de confirmação: ao desativar, "API e-SIC desativada."; ao reativar, "API e-SIC reativada. Credenciais mantidas."

---

## Escopo

- Opção "Integrações" no menu de ações do Gerenciador de clientes, com o brasão e nome do cliente fixos na navegação da página.
- Ativação/desativação/reativação da integração, com as mensagens de confirmação definidas.
- Exibição e cópia das credenciais (identificador do cliente, chave secreta mascarada).
- Seleção de módulos expostos, restrita aos módulos contratados, com confirmação ao salvar e ao sair com alterações pendentes.
- Histórico de alterações (ativação/desativação, inclusão/remoção de módulo, cópia de credencial), com responsável, data e hora.
- Correção da nomenclatura de `requester.type` na listagem de solicitações da API e-SIC, por extenso (herdada da Parte 1 — achado [[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-002/00 QA/00 README|10736-CT-002]]).

---

## Fora de escopo

- Backend de geração/persistência de credenciais (já entregue na Parte 1 — MR 1198).
- Correção do ranking "Sem Nome" para Pessoa Jurídica/Anônimo e correção de paginação — tratadas como achados da SGV-10736 ([[QA Workspace/02 Demandas/HML/SGV-9657 - API esic - Melhorias nos dados disponibilizados/SGV-10736 - Normalização das informações/Bugs/10736-CT-011/00 QA/00 README|10736-CT-011]]), sem critério próprio aqui ainda.
- Qualquer ambiente além do Técnico (não é tela voltada ao cliente final).

---

## Critérios de aceite

- C1. O menu de ações do cliente exibe a opção "Integrações", desabilitada (mas visível) quando o cliente está inativo. ^c1
- C2. A página de Integrações exibe o brasão e o nome do cliente durante toda a navegação. ^c2
- C3. Ativar a integração gera as duas credenciais (identificador do cliente, chave secreta) com efeito imediato, exibindo estado de carregamento enquanto gera. ^c3
- C4. Identificador do cliente e chave secreta são somente leitura; a chave secreta é exibida parcialmente mascarada. ^c4
- C5. Copiar o identificador ou a chave secreta sempre copia o valor real (nunca a versão mascarada), com confirmação visual a cada cópia. ^c5
- C6. Desativar e depois reativar a integração preserva as credenciais existentes — reativar não gera credenciais novas. ^c6
- C7. A lista de módulos disponíveis para seleção é restrita aos módulos contratados pelo cliente. ^c7
- C8. É possível manter a integração ativa sem nenhum módulo selecionado. ^c8
- C9. Alterações na seleção de módulos só valem depois de salvas; salvar exige confirmação. ^c9
- C10. Sair da página com alterações pendentes pede confirmação antes de descartar. ^c10
- C11. Desativar a integração exige confirmação e, ao concluir, exibe a mensagem "API e-SIC desativada." ^c11
- C12. Reativar a integração exibe a mensagem "API e-SIC reativada. Credenciais mantidas." ^c12
- C13. O histórico de alterações registra ativação/desativação, inclusão/remoção de módulo e cópia de credencial, com responsável, data e hora — acessível mesmo com a integração desativada. ^c13
- C14. A listagem de solicitações retorna o tipo do solicitante (pessoa física ou jurídica) por extenso, no mesmo padrão já usado pelas estatísticas. ^c14

---

## Checklist de entrega ao DEV

- [x] Decisões e regras de negócio estão fechadas.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Plano e casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.
