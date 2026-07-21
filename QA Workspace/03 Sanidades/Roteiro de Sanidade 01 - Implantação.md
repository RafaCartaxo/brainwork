---
title: Roteiro de Sanidade 01 — Implantação
tags:
  - qa
  - sanidade
  - sogov
  - implantacao
tipo: roteiro-sanidade
revisado: 2026-07-21
fonte: https://app.notion.com/p/alfa-group/Roteiro-de-Sanidade-01-Implanta-o-2fd2aec67d30800d9c7fca91c50e28ad
ags:
  - AGS-76
  - AGS-11
---
# Roteiro de Sanidade 01: Implantação

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-07-21. A página do Notion é a fonte de verdade externa; esta cópia é o acervo local pesquisável. Roteiro de execução manual (smoke test) do fluxo de implantação de um cliente do zero. **Pensado pra virar base de automação** — o passo 2 (dados gerais do cliente) equivale ao cenário `createInstance` do repo `sogov-automation-test` (ver [[#Automação]]).

> [!abstract] Casos de teste vinculados (Notion)
> Sanidade 005, 006, 007, 008, 010 (+ 7 outros) — "Roteiro de Sanidade 01: Implantação".

## Bugs com impacto em cenários do roteiro
- [BUG] (Sanidade-006/2026) Erro 503 ao ativar clientes com status "Em implantação" — ver [[../02 Demandas/Concluídas/6975 - Bug Erro 503 Ativar Cliente Em Implantação|SGV-6975]]
- [BUG] (Sanidade-005/2026) Documento temporário volta para "Em elaboração" após emitir em instância Em Implantação
- [BUG] (Sanidade-005/2026) Não é possível assinar documento em instância Em Implantação

## Roteiro

### 1. Acessar o cadastro de clientes
Acesse o sistema e entre na opção de cadastro de clientes.

### 2. Preencher os dados gerais do cliente
| Campo | Orientação |
|---|---|
| Tipo de cliente | Selecione uma das opções de forma aleatória |
| CNPJ | Informe um CNPJ válido. Após informar, o sistema busca automaticamente a razão social |
| Razão social | Preenchido automaticamente após validação do CNPJ. Apenas confirme |
| Nome para exibição | Informe um nome com **25 caracteres ou mais**. Padrão: `Sanidade Versão <versão vigente>` (ex.: `Sanidade Versão 11.19.24.2`) |
| CEP | Informe um CEP válido. O sistema busca o endereço automaticamente |
| Número | Número inteiro (pode ser aleatório) |
| Domínio | Formato `sgv + número do ciclo de testes` (ex.: `sgv001`, `sgv002`) |
| Licenças | Número inteiro **maior que 20** |
| Início do contrato | Data atual |
| Fim do contrato | Data atual **+ 15 dias** |
| Módulos base | **Não** selecione nenhum módulo |
| Personalização e Temas | Mantenha a opção **Padrão** |

### 3. Finalizar o cadastro
Após conferir, salve o cadastro. No menu principal, entre em **Gerenciador de Clientes**, localize o cliente e clique em **Iniciar implantação**.

### 4. Cadastrar os módulos do cliente
Para cada módulo, use o padrão de nome `Nome do Módulo - SGV - <número do ciclo>` (ex.: `Memorando - SGV - 001`).

| Módulo | Tipo | Divulgação | Caráter informativo | Vincula Assuntos e Serviços | Observações |
|---|---|---|---|---|---|
| Memorando | Documento Oficial | Apenas interno | Não | Não | Comunicação interna |
| Ofício | Documento Oficial | Apenas interno | Não | Não | Comunicação formal |
| Ato Oficial | Comunicado Oficial | Interno e externo | Sim | Não | Comunicação |
| Atend. ao Cidadão | Processo administrativo | — | — | Sim | Atendimento externo |
| Atend. ao Servidor | Processo administrativo | — | — | Sim | Atendimento interno |
| Ouvidoria | Processo administrativo | — | — | Sim | Permite sigilo |
| e-SIC | Processo administrativo | — | — | Não | Base legal obrigatória |

**Detalhe dos campos por módulo:**

- **Memorando** — Documento Oficial · Apenas interno · Não informativo · Não vincula. Campos: Assunto (texto pequeno), Descrição (texto grande).
- **Ofício** — Documento Oficial · Divulgação: Sim · Não informativo · Não vincula. Campos: Assunto (texto pequeno), Descrição (texto grande).
- **Ato Oficial** — Comunicado Oficial · Interno e externo · Informativo: Sim · Não vincula. Campos: Descrição (texto grande).
- **Atendimento ao Cidadão** — Processo administrativo · Abertura externa: Sim · Privacidade: Não · Despacho sigiloso: Não · Processos urbanísticos: Não · Vincula: Sim. Campos: Assunto (texto pequeno), Descrição (texto grande).
- **Atendimento ao Servidor** — Processo administrativo · Abertura externa: Sim · Privacidade: Não · Despacho sigiloso: Não · Processos urbanísticos: Não · Vincula: Sim. Campos: Assunto (texto pequeno), Descrição (texto grande).
- **Ouvidoria** — Processo administrativo · Abertura externa: Sim · Privacidade: Sim · Despacho sigiloso: Sim · Processos urbanísticos: Não · Vincula: Sim. Campos: Assunto (texto pequeno), Relato (texto grande).
- **e-SIC** — Processo administrativo · Abertura externa: Sim · Privacidade: Não · Despacho sigiloso: Não · Processos urbanísticos: Não · Vincula: Não. Campos: Solicitante (texto pequeno), Pedido (texto grande), Base legal (texto pequeno).

### 5. Cadastrar os órgãos do organograma
Cadastre cada órgão (nome + sigla):

| Órgão | Sigla |
|---|---|
| Gabinete do Prefeito | GP |
| Secretaria de Fazenda e Planejamento | SEFAZ |
| Secretaria de Saúde | SESAU |
| Secretaria de Educação e Cultura | SEDUC |
| Secretaria de Obras e Urbanismo | SEOURB |

### 6. Acessar o cadastro de servidores
Com o organograma cadastrado, acesse **Servidores** → **Cadastrar novo servidor**.

| Órgão | Sigla | Cargo | Permissão | Nome | CPF | E-mail | Senha |
|---|---|---|---|---|---|---|---|
| Gabinete do Prefeito | GP | Chefe de Gabinete | Administrador | Paulina das Merces Conceição | 37773178534 | paulinaconceicao@uorak.com | Teste@123 |
| Secretaria de Fazenda e Planejamento | SEFAZ | Diretor de Arrecadação | Administrador Setorial | Josepha Santos | 71404473572 | josephasantos@uorak.com | Teste@123 |
| Secretaria de Saúde | SESAU | Atendente de Recepção | Somente leitura | Maria Madalena De Souza | 59058200582 | mariadesouza@uorak.com | Teste@123 |
| Secretaria de Educação e Cultura | SEDUC | Auxiliar Administrativo | Usuário básico | Antonia Rabelo Dias | 62656066549 | antoniarabelo@uorak.com | Teste@123 |
| Secretaria de Obras e Urbanismo | SEOURB | Engenheiro Responsável | Especialista | Jose Ferreira dos Santos | 69311536504 | josesantos@uorak.com | Teste@123 |

Finalizar o cadastro por e-mail.

### 7. Vincular módulos pela configuração do cliente
Acesse **Configuração do Cliente** → **Vincular módulos à prefeitura**. Selecione **Memorando** e **e-SIC** e salve.

### 8. Finalizar configurações pendentes acessando os módulos
Após vincular, acesse cada módulo para concluir as configurações obrigatórias.

| Configuração | Memorando | e-SIC |
|---|---|---|
| Setores que recebem e tramitam | Todos os setores | Todos os setores |
| Setores criadores | Todos os setores | GP |
| Setores destino | — | GP e SEFAZ |
| Responsável | — | GP |
| Setores disponíveis para o cidadão enviar | — | GP |
| Permite conexão com outros módulos | Sim | Sim |
| Haverão prazos? | Não | Sim – 10 dias |
| Haverão prorrogações? | Não | Sim – 2 dias |
| Definir numeração inicial | Sim | Sim |
| Mantém numeração sequencial após mudança de ano | Não | Sim |

### 9. Vincular módulos nas configurações dos módulos
| Configuração | Ofício | Ato Oficial | Atend. ao Cidadão | Atend. ao Servidor | Ouvidoria |
|---|---|---|---|---|---|
| Setores que recebem e tramitam | GP | Todos os setores | Todos os setores | Todos os setores | Todos os setores |
| Setores criadores | GP | GP | GP e SESAU | Todos os setores | GP |
| Setores destino | — | — | GP e SESAU | SEFAZ | GP |
| Responsável pelo módulo | — | — | SESAU | SEFAZ | GP |
| Setores disponíveis para o cidadão enviar | — | — | SESAU e SEOURB | SEFAZ | GP |
| Interações externas | — | — | — | GP | GP |
| Sigilos | — | — | — | — | GP |
| Permite conexão com outros módulos | Sim | Não | Sim | Sim | Sim |
| Haverão prazos? | Não | Sim – 5 dias | Sim – 30 dias | Sim | Sim |
| Haverão prorrogações? | Não | Não | Sim – 3 prorrogações de 2 dias | Sim | Sim |
| Definir numeração inicial | Sim | Sim | Sim | Sim | Sim |
| Mantém numeração sequencial após mudança de ano | Não | Sim | Sim | Sim | Sim |

### 10. Vincular módulos nas configurações dos setores
Acesse **Setores** → editar um setor → **Editar setor**.

- **Ofício nos setores** — Setores criadores: Todos. Setores que recebem e tramitam: Todos.
- **Atendimento ao Cidadão nos setores** — Setores criadores: GP, SEFAZ, SEOURB e SESAU. Setores que recebem e tramitam: Todos. Setores destino: GP, SEFAZ, SEOURB e SESAU. Responsável pelo módulo: SESAU.

### 11. Cadastrar um subsetor
Acesse **Setores** → localize **SEFAZ – Secretaria de Fazenda e Planejamento** → cadastrar subsetor:
- Nome: **Departamento de Recursos Humanos** · Sigla: **RH**
- Regras de tramitação → Criar documento: **Atend. ao Servidor**

Salve.

### 12. Cadastrar Servidor

**12.1 Cadastrar servidor via link** — Envie o link de cadastro; o servidor preenche os dados; o cadastro fica pendente de aprovação.
- Setor: RH – Departamento de Recursos Humanos · Cargo: Analista de Folha de Pagamento · Permissão: Especialista

| Órgão | Sigla | Cargo | Permissão | Nome | CPF | E-mail | Senha |
|---|---|---|---|---|---|---|---|
| Departamento de Recursos Humanos | RH | Analista de Folha de Pagamento | Especialista | Jovina Maria De Jesus | 55851762500 | jovinamaria@uorak.com | Teste@123 |

**12.2 Aprovar o cadastro do servidor** — Acesse a área de aprovação, localize o cadastro pendente, confira os dados (RH / Analista de Folha de Pagamento / Especialista) e aprove.

### 13. Cadastrar assuntos

**13.1 Solicitação de Férias**
- Nome: Solicitação de Férias · Categoria: Férias · Módulo: Atend. Servidor SGV-xxx
- Descrição: serviço comum, ideal pra testar prazos, anexos (formulário de requerimento) e tramitação servidor → diretor → RH.
- Natureza/Privacidade: Abertura externa: Sim · Cidadão interage só na abertura: Sim
- Tramitação (setores criadores / recebem e tramitam / destino / interações externas): manter existentes e **adicionar RH**; Receberá automaticamente: RH
- Prazos: permite prazo do assunto — 10 dias corridos/úteis (30 dias herdado do módulo)
- Numeração/Assinaturas: página de assinaturas separada: Sim
- Campos: Período Aquisitivo (texto pequeno, ex. 2024/2025), Data de Início (data), Quantidade de Dias (numérico), Abono Pecuniário (seleção Sim/Não), Adiantamento de 13º (seleção Sim/Não), Substituto Eventual (texto pequeno)

**13.2 Progressão de Carreira**
- Nome: Progressão de Carreira · Categoria: Carreira · Subcategoria: Progressão · Módulo: Atend. Servidor SGV-xxx
- Descrição: assunto mais complexo — testa conexão com outros módulos (anexar Ato Oficial/Certificado) e prazos de análise mais longos.
- Natureza/Privacidade: Cidadão interage só na abertura: Não
- Tramitação: manter existentes e **adicionar RH**; Receberá automaticamente: RH
- Prazos: permite prazo do assunto — 10 dias úteis
- Campos: Tipo de Progressão (seleção: Titulação/Tempo de Serviço/Mérito), Nível Atual (texto pequeno), Nível Pretendido (texto pequeno), Descrição da Justificativa (texto grande), Anexo de Certificados (upload — todos), Data da Última Progressão (data)

### 14. Criar documentos
Para cada servidor, gerar **2 documentos por módulo**. Para documentos e comunicados oficiais: 1 emissão imediata + 1 salvar e emitir depois.

### 15. Finalizar implantação
**Ativar o cliente.**

## Automação
- Repo: `sogov-automation-test` ([[../../../../project_sogov_automation_repo|nota do projeto]] / GitLab).
- O **passo 2** (dados gerais do cliente) já tem infra no repo: comando `createInstance` + `getInstanceOrCreate` e factory `makeInstance` (`cypress/support/commands/api/instance.api.commands.js`), hoje usados só como setup em `support/e2e.js`, **sem spec dedicado**. Este roteiro é a fonte manual pra derivar o CT `create.instance` (happy path + negativos).
- Passos 4–13 têm comandos análogos no repo (`getSectorOrCreate`, `getModuleOrCreate`, assuntos/serviços) — candidatos a virar specs de sanidade automatizados.

## Dúvidas em aberto
- [ ] Roteiro não define ambiente-alvo da sanidade (DEV/HML) — confirmar em qual ambiente a sanidade de implantação roda.
- [ ] Nome do módulo de assunto aparece como `Atend. Servidor SGV-xxx` (placeholder) — o número real do ciclo entra em tempo de execução.

## Referências
- Notion original: https://app.notion.com/p/alfa-group/Roteiro-de-Sanidade-01-Implanta-o-2fd2aec67d30800d9c7fca91c50e28ad
- Continuação de fluxo: [[Roteiro de Sanidade 02 - Atendimento ao Cidadão]], [[Roteiro de Sanidade 03 - Processos Urbanísticos]]
