---
title: Clientes (Instâncias)
tags:
  - qa
  - conhecimento
  - sogov
  - instancia
tipo: modulo
revisado: 2026-10-14
---
# Clientes (Instâncias)

## Visão geral

**SOGOV — Roteiro de Sanidade**

**Etapa 1 — Criação de Instância (Cliente)**

Objetivo: Criar uma nova instância no SOGOV, configurando seus dados gerais, módulo base, integrações, personalização e identidade visual.

### 0. Acesso administrativo
Pré-requisito aos passos 1–3 abaixo (login e acesso à aba Clientes): antes disso é preciso selecionar o escopo de acesso e entrar na área administrativa.
- Selecionar as bolsas (escopo) de acesso e confirmar.
- Acessar a área administrativa (/admin).

### 1. Dados Gerais
1. Acessar o ambiente de login do Colaborador SOGOV.
2. Realizar login como colaborador.
3. Acessar a aba Clientes.
4. Iniciar o cadastro de um novo cliente.
5. Selecionar o Tipo de Cliente.
6. Informar um CNPJ válido.
7. Validar o preenchimento automático da Razão Social conforme o CNPJ informado.
8. Preencher o Nome de Exibição livremente.
9. Preencher o Telefone (opcional).
10. Informar um CEP válido.
11. Validar o preenchimento automático de Estado, Cidade, Bairro e Endereço (Rua).
12. Preencher manualmente o Número do endereço.
13. Preencher manualmente o Complemento.
14. Preencher o Domínio seguindo o padrão sanidade-01, sanidade-02, sanidade-03 e assim sucessivamente.
15. Definir o Número de Licenças como 50.
16. Definir a Data de Início do Contrato como a data atual.
17. Definir a Data de Fim do Contrato para três meses após o início.

### 2. Módulo Base
18. Acessar a aba Módulo Base.
19. Clicar no campo de seleção do módulo.
20. Verificar os módulos disponíveis.
21. Selecionar um módulo base previamente cadastrado.

Resultado esperado: Os módulos existentes devem ser apresentados para seleção. Caso não existam módulos cadastrados, a lista poderá estar vazia.

### 3. Integrações
22. Localizar a integração com a plataforma Mais Transparência.
23. Validar que a integração está desativada por padrão.
24. Localizar a integração com o ecossistema Tensai.
25. Validar que a integração está desativada por padrão.
26. Localizar a integração com a Cesta de Preços.
27. Validar que a integração está desativada por padrão.

Resultado esperado: As três integrações devem estar desativadas por padrão ao iniciar o cadastro de uma nova instância.

Regra para automação: Validar o estado inicial das três integrações, sem necessidade de ativá-las.

### 4. Personalização e Tema
28. Acessar a aba Personalização e Tema.
29. Localizar o campo de seleção do tema.
30. Verificar os temas disponíveis: Padrão, Vermelho, Laranja, Roxo, Amarelo e Verde.
31. Selecionar um dos temas disponíveis.

### 5. Marca
32. Acessar a aba Marca.
33. Realizar upload do Símbolo para Fundo Claro.
34. Realizar upload do Símbolo para Fundo Escuro.
35. Realizar upload da Imagem para Tela de Login.
36. Realizar upload da Logomarca para Fundo Claro.
37. Realizar upload da Logomarca para Fundo Escuro.

### 6. Finalização
38. Conferir os dados preenchidos.
39. Clicar no botão Cadastrar.
40. Validar a conclusão do cadastro da instância.

### Regras e observações para automação

| Campo | Regra |
|---|---|
| CNPJ | Utilizar CNPJ válido |
| Razão Social | Preenchimento automático |
| Nome de Exibição | Preenchimento livre |
| Telefone | Opcional |
| CEP | Utilizar CEP válido |
| Estado, Cidade, Bairro e Rua | Preenchimento automático |
| Número e Complemento | Preenchimento manual |
| Domínio | Sequencial: sanidade-01, sanidade-02... |
| Licenças | 50 |
| Início do Contrato | Data atual |
| Fim do Contrato | Data atual + 3 meses |
| Módulo Base | Selecionar módulo existente |
| Mais Transparência | Desativada por padrão |
| Tensai | Desativada por padrão |
| Cesta de Preços | Desativada por padrão |
| Tema | Selecionar entre os disponíveis |
| Marca | Cinco campos de upload |

### Resumo do roteiro

| Seção | Passos | Descrição |
|---|---|---|
| Dados Gerais | 1–17 | Identificação, endereço, domínio e contrato |
| Módulo Base | 18–21 | Seleção do módulo |
| Integrações | 22–27 | Validação das integrações desativadas |
| Personalização e Tema | 28–31 | Configuração visual |
| Marca | 32–37 | Upload dos elementos visuais |
| Finalização | 38–40 | Cadastro da instância |

## Dúvidas em aberto

## Cards relacionados
