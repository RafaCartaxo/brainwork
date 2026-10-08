---
tags: [qa]
task: SGV-12082
pai: SGV-11262
tipo: secao-tr
itens_tr: "1.1–1.23"
paginas_pdf: "p. 1"
status: lido
---
# 01 - Infraestrutura técnica e operacional (itens 1.1–1.23)

> [!info]- Navegação
> **Matriz/índice:** [[../01 - Matriz de atores e relações|Matriz de atores e relações]] · **Demanda:** [[../../00 QA/01 - Demanda]] · **Plano de análise:** [[../../00 QA/02 - Plano de análise]] · **Mapa geral:** [[../00 - Mapa geral]]

> [!info] Escopo deste recorte — segmentação aprovada; recorte lido em 08/10/2026, aguardando revisão do Codex
> Itens do TR: **1.1–1.23**. Página do PDF: **p. 1** de [[../../Fontes/Requisitos Sogov.pdf|Requisitos Sogov.pdf]] (fonte de autoridade; esta nota é só registro/rastreabilidade, nunca substitui o PDF). Lida diretamente por render de página (imagem), não por extração textual — a camada de texto do PDF é conhecida por corromper caracteres, então não foi usada como evidência. Todos os 23 itens deste recorte são requisitos de infraestrutura/operação técnica, sem subitens (diferente do item 1.24, que já pertence ao recorte 2 e tem subitens 1.24.1/1.24.2 na mesma página). Classificação abaixo é um primeiro passe, pendente de revisão.

## Cobertura dos itens

> Todos os itens deste recorte estão na mesma página do PDF (p. 1 — ver Escopo acima); a página não é repetida linha a linha.

| Item do TR | Situação | Justificativa ou pendência |
|---|---|---|
| 1.1 | Não aplicável | Hospedagem web, SSL, disponibilidade ≥99% — infraestrutura/hospedagem. |
| 1.2 | Não aplicável | Datacenter nacional, normas ISO/Marco Civil/LGPD — conformidade/infraestrutura. |
| 1.3 | Não aplicável | Escalabilidade automática do banco, "instâncias de banco de dados conforme demanda" — escalabilidade técnica (nota terminológica "instância" abaixo). |
| 1.4 | Não aplicável | Backup/restauração/replicação/balanceamento do banco — operação de infraestrutura. |
| 1.5 | Não aplicável | Compatibilidade com bancos relacionais (MySQL/PostgreSQL) — escolha de tecnologia. |
| 1.6 | Não aplicável | Elasticidade computacional vertical/horizontal — infraestrutura de capacidade. |
| 1.7 | Não aplicável | Rede privada/segura entre serviços, acesso público/privado — rede. |
| 1.8 | Não aplicável | Sub-redes, gateways, VPN — infraestrutura de rede. |
| 1.9 | Não aplicável | Monitoramento por ML de anomalias de desempenho/recursos — observabilidade. |
| 1.10 | Não aplicável | Envio de e-mail (até 50 mil/dia, 14/s) — capacidade técnica, não a entidade "notificação" (ver nota abaixo). |
| 1.11 | Não aplicável | Autenticação de remetente/anti-spam — infraestrutura de e-mail. |
| 1.12 | Não aplicável | Credenciais de banco, chaves de API, segredos, rotação automática — segurança operacional (nota terminológica "chaves" abaixo). |
| 1.13 | Não aplicável | Auditoria de acesso/alteração de credenciais de sistema — distinta de trilha de ação do usuário (nota abaixo). |
| 1.14 | Não aplicável | Rate limiting e proteção DDoS — segurança de infraestrutura. |
| 1.15 | Não aplicável | Armazenamento seguro de documentos/arquivos, alta disponibilidade — durabilidade de storage, não a entidade "documento" (nota abaixo). |
| 1.16 | Não aplicável | Armazenamento de grandes volumes, ciclo de vida/versionamento — infraestrutura de storage. |
| 1.17 | Não aplicável | Proteção contra SQL Injection, XSS, DDoS — segurança de aplicação. |
| 1.18 | Não aplicável | Regras de segurança personalizadas, resposta automática a ataques — segurança operacional. |
| 1.19 | Não aplicável | Fila de mensagens entre serviços (assíncrono) — infraestrutura de mensageria. |
| 1.20 | Não aplicável | Múltiplas filas com prioridade/tempo de espera — infraestrutura de mensageria. |
| 1.21 | Não aplicável | Chaves criptográficas para proteção de dados — infraestrutura de criptografia (nota terminológica "chaves" abaixo). |
| 1.22 | Não aplicável | Controle de acesso às chaves criptográficas — segurança (nota terminológica "chaves" abaixo). |
| 1.23 | Não aplicável | Rastreamento de gargalos/falhas na infraestrutura — observabilidade. |

**Resultado do recorte:** 23/23 itens considerados; **23 Não aplicáveis** ao modelo de atores/entidades/dados de negócio — todos descrevem infraestrutura, segurança operacional ou observabilidade, sem ator/entidade/estado de negócio do SOGOV. Nenhum item pendente.

## Elementos identificados

| Referência do TR | Elemento | Tipo | Papel/descrição | Dados ou atributos relevantes | Certeza/evidência |
|---|---|---|---|---|---|
| | | | | | |

Tabela vazia — nenhum ator, entidade, configuração ou estado de negócio foi identificado neste recorte. Os 23 itens descrevem capacidades técnicas da plataforma (hospedagem, banco de dados, rede, segurança, mensageria, criptografia, observabilidade), não elementos do modelo de dados de negócio do SOGOV. Isso não é uma lacuna de leitura — é o resultado esperado para um bloco de requisitos de infraestrutura.

## Relações/dependências identificadas

| Origem | Relação/dependência | Destino | Referência do TR | Certeza/evidência ou pendência |
|---|---|---|---|---|
| | | | | |

Tabela vazia — sem elementos de negócio identificados neste recorte, não há relação/dependência de negócio a registrar.

## Dúvidas/ambiguidades

- **"Instância" (1.3):** o item fala em "diferentes instâncias de banco de dados conforme demanda", num sentido de escalabilidade técnica do banco. Isso **não é o mesmo conceito** de "instância" usado em outras partes da iniciativa (cliente/tenant, ex. a antiga instância 225) — o texto deste item, isoladamente, não sustenta a leitura de tenant/cliente. Registro aqui só para não confundir os dois sentidos em recortes futuros; não reclassifiquei o item por causa disso.
- **"Chaves" (1.12, 1.21, 1.22):** os três itens usam "chave(s)" no sentido de segredo técnico/criptográfico (chave de API, chave criptográfica) — um conceito diferente de "chave de acesso" como funcionalidade de negócio (delegação de permissão a terceiros), que é o item 1.41 (recorte 9). Mesma nota de não confundir os dois sentidos.
- **"Auditoria" (1.13):** auditoria de acesso/alteração de credenciais de infraestrutura — distinta da trilha de tramitação/linha do tempo de ações do usuário (prevista no item 1.35.1, recorte 7). Mesma nota de não confundir.
- **Armazenamento de documentos (1.15, 1.16):** tratam da durabilidade/retenção técnica do armazenamento de arquivos, não do modelo de dados do documento como entidade de negócio (categorias, metadados, tramitação — tratado nos recortes 4, 5 e 7). Mesma nota de não confundir infraestrutura de armazenamento com a entidade "documento".
- **Capacidade de notificação por e-mail (1.10):** define um limite técnico de envio (50 mil/dia, 14/s), que pode ser um parâmetro relevante quando (e se) a notificação virar elemento de negócio em recortes funcionais — não decidido aqui, só registrado como possível dependência a verificar mais adiante.

Nenhuma dessas notas altera a classificação "Não aplicável" dos itens — são só avisos de terminologia para os recortes 2–11, registrados aqui porque a ambiguidade aparece pela primeira vez neste bloco.

## Fontes/evidências

- PDF: `Fontes/Requisitos Sogov.pdf`, p. 1 — lida por render de página (imagem), conferida diretamente nesta sessão em 08/10/2026. Nenhum trecho textual extraído (potencialmente corrompido) foi usado como evidência.
