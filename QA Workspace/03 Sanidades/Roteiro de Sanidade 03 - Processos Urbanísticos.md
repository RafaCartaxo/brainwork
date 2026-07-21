---
title: Roteiro de Sanidade 03 — Processos Urbanísticos
tags:
  - qa
  - sanidade
  - sogov
  - processos-urbanisticos
tipo: roteiro-sanidade
revisado: 2026-07-21
fonte: https://app.notion.com/p/alfa-group/Roteiro-de-Sanidade-03-Processos-urban-sticos-2fd2aec67d3080838477f7afb819b55b
ags:
  - AGS-76
  - AGS-13
---
# Roteiro de Sanidade 03: Processos Urbanísticos

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-07-21. A página do Notion é a fonte de verdade externa; esta cópia é o acervo local pesquisável. Roteiro de execução manual (smoke test) do módulo de Licenciamento Urbanístico. Depende da instância criada em [[Roteiro de Sanidade 01 - Implantação]].

> [!abstract] Casos de teste vinculados (Notion)
> Nenhum vinculado ainda (Ciclos de testes / Casos de Testes vazios no Notion).

## Melhorias com impacto em cenários do roteiro
- [Melhoria] Permitir criação de fluxo de trabalho para módulos de Processo Urbanístico

## Bugs com impacto em cenários do roteiro
- (nenhum registrado no export)

## Roteiro

### 1. Cadastrar módulo Licenciamento Urbanístico
Acessar o ambiente **colaborador Sogo** → cadastrar módulo do cliente. Nome: `Lic. Urbanístico - SGV - 001`.

| Módulo | Abertura externa | Processos urbanísticos | Tipo | Vincula Assuntos e Serviços | Observações |
|---|---|---|---|---|---|
| Licenciamento urbanístico | Sim | Sim | Processo administrativo | Sim | Atendimento externo |

**Campos disponíveis:**
- Solicitação → texto grande, com conteúdo padrão:
  > Solicito a abertura de processo para análise e licenciamento urbanístico, conforme informações prestadas neste formulário.
  >
  > Declaro que os dados informados são verídicos e estou ciente de que poderão ser solicitadas informações ou documentos complementares no decorrer da análise.
  >
  > Aguardo o prosseguimento da solicitação pelo setor responsável.
- Endereço da Solicitação → Endereço (obrigatório)
- Pessoas → Grupo de contatos

### 2. Configurar módulo Licenciamento Urbanístico
Acessar lista de **Clientes cadastrados** → selecionar a Instância de Sanidade e **ativar contratações adicionais**:
- Processos urbanísticos → `Lic. Urbanístico - SGV - 001` → Salvar
- Fluxo de trabalho → `Lic. Urbanístico - SGV - 001` → Salvar

Acessar o módulo e finalizar o cadastro no cliente.

### 3. Finalizar configurações pendentes acessando o módulo
| Configuração | Licenciamento Urbanístico |
|---|---|
| Setores que recebem e tramitam | GP, SEFAZ, SEOURB |
| Setores criadores | GP, SEOURB |
| Setores destino | GP, SEOURB |
| Responsável | SEOURB |
| Setores disponíveis para o cidadão enviar | GP, SEFAZ, SEOURB ⚠️ (como existe setor responsável, o setor aparece **travado** para o cidadão) |
| Permite conexão com outros módulos | Sim |
| Haverão prazos? | Sim – 30 dias |
| Haverão prorrogações? | Sim – 2 de 2 dias |
| Definir numeração inicial | Sim |
| Mantém numeração sequencial após mudança de ano | Não |
| Campo de Zoneamento | Sim |

### 4. Acessar o cadastro de Assuntos e Serviços
Acesse como **Administrador** → menu **Assuntos e Serviços** → **Criar novo serviço**.

### 5. Cadastrar o assunto/serviço "Alvará de Construção"
**5.1 Dados do assunto**
- Nome: Alvará de Construção
- Descrição: solicitação para análise e emissão de alvará para execução de obra, conforme legislação urbanística vigente.
- Módulo: `Lic. Urbanístico - SGV - 00X` · Categoria: Serviços Urbanos · Subcategoria: Obras

**5.2 Natureza e Privacidade** — Permite abertura externa (herdado do módulo).

**5.3 Regras de tramitação**
| Configuração | Alvará de Construção |
|---|---|
| Setores criadores | Manter existentes e garantir SEOURB |
| Setores que recebem e tramitam | Manter existentes e garantir SEOURB, SEFAZ |
| Setores destino | SEOURB |
| Responsável | SEOURB |
| Permite conexão com outros módulos | Sim |
| Cidadão interage só na abertura | Não |
| Haverão prazos? | Sim – 20 dias (**deve sobrepor** o prazo definido a nível de módulo) |
| Haverão prorrogações? | Sim – 2 de 2 dias |
| Definir numeração inicial | Sim |
| Mantém numeração sequencial após mudança de ano | Não |

**5.4 Formulário do Serviço**
- Local → Mapa
- Tipo de obra → múltipla escolha: Residencial, Comercial, Reforma, Ampliação
- Grupo "Dados do solicitante": CPF/CNPJ (número), Telefone/WhatsApp (número), E-mail
- Grupo "Dados técnicos": Área da construção m² (número), Número de pavimentos (número), Possui responsável técnico? (Sim/Não)
  - Se **Sim**: Nome do responsável técnico, Registro (CREA/CAU)

Salve o assunto e serviço.

### 6. Cadastrar nova etiqueta
Acessar **Etiquetas** → **Nova etiqueta**:
- Nome (padrão): `SGV-001 - Sanidade`
- Cor: selecionar uma para identificação visual
- Compartilhamento: uma das opções (Não compartilhar / Apenas meus setores / Setores específicos / Todo o organograma)

Salvar.
> [!check] Resultado esperado
> Etiqueta criada; nome conforme padrão; cor aplicada; regra de compartilhamento respeitada na visualização.

### 7. Abrir processo de Alvará de Construção (Cidadão)
Como cidadão → módulo Licenciamento Urbanístico → serviço Alvará de Construção → preencher obrigatórios (Endereço, Tipo de obra, Dados do solicitante, Dados técnicos). Validar campo condicional: "Possui responsável técnico?" = **Sim** → preencher adicionais → enviar.
> [!check] Resultado esperado
> Processo criado; número gerado; prazo inicial 20 dias (regra do serviço); setor responsável = SEOURB; campo de endereço validado como obrigatório; campos condicionais exibidos corretamente.

### 8. Validar recebimento no setor responsável e aplicar etiqueta
Como servidor **SEOURB** → mesa de trabalho → localizar o processo na coluna **Em aberto** → vincular etiqueta `SGV-000 - Sanidade` → filtrar por etiqueta.
> [!check] Resultado esperado
> Processo na coluna Em aberto do SEOURB; informações do formulário corretas; prazo 20 dias; etiqueta aplicada e filtrada corretamente.

### 9. Tramitação para SEFAZ (Servidor – SEOURB)
Coluna Em aberto → despacho "Encaminhamos o processo para análise fiscal." → setor destino **SEFAZ** → emitir.
> [!check] Resultado esperado
> Processo segue Em tramitação na mesa SEOURB; aparece Em aberto na mesa SEFAZ; despacho na timeline; etiqueta permanece; prazo inalterado.

### 10. Atendimento no setor SEFAZ (Servidor – SEFAZ)
Coluna Em aberto → despacho "Processo recebido para análise fiscal." → emitir.
> [!check] Resultado esperado
> Processo permanece Em tramitação no SEFAZ; despacho registrado; evento na timeline; etiqueta visível.

### 11. Retorno do processo para SEOURB (Servidor – SEFAZ)
Coluna Em tramitação → despacho "Processo analisado. Retornando para o setor responsável." → setor destino **SEOURB** → emitir.
> [!check] Resultado esperado
> Processo segue Em tramitação no SEFAZ; aparece Em aberto no SEOURB; despacho na timeline; histórico atualizado; etiqueta permanece; nenhuma perda de dados.

### 12. Interação do cidadão no processo
Como cidadão → acessar via Notificações → resposta "Seguem documentos complementares para análise do processo." + anexar arquivo (PDF ou imagem) → enviar.
> [!check] Resultado esperado
> Resposta enviada; texto na timeline; anexo disponível; evento na timeline; setor/servidor notificado; processo mantém estado conforme regra do sistema.

## Dúvidas em aberto
- [ ] Roteiro não define ambiente-alvo (DEV/HML) — confirmar.
- [ ] Passos 6/8 divergem no nome da etiqueta (`SGV-001 - Sanidade` na criação vs. `SGV-000 - Sanidade` ao vincular/filtrar) — confirmar padrão correto.
- [ ] Roteiro não tem passo de encerramento/finalização do processo (termina na interação do cidadão) — confirmar se é intencional.

## Referências
- Notion original: https://app.notion.com/p/alfa-group/Roteiro-de-Sanidade-03-Processos-urban-sticos-2fd2aec67d3080838477f7afb819b55b
- Pré-requisito: [[Roteiro de Sanidade 01 - Implantação]]
