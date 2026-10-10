---
tags: [qa]
task: SGV-12082
pai: SGV-11262
tipo: secao-tr
itens_tr: "1.1–1.23"
paginas_pdf: "p. 1"
status: aprovado
---
# 01 - Infraestrutura técnica e operacional (itens 1.1–1.23)

> [!info]- Navegação
> **Matriz/índice:** [[../01 - Matriz de atores e relações|Matriz de atores e relações]] · **Demanda:** [[../../00 QA/01 - Demanda]] · **Plano de análise:** [[../../00 QA/02 - Plano de análise]] · **Mapa geral:** [[../00 - Mapa geral]]

> [!info] Escopo deste recorte — revisado e aprovado pelo Codex em 08/10/2026
> Itens do TR: **1.1–1.23**. Página do PDF: **p. 1** de [[../../Fontes/Termo de Referência SOGOV.pdf|Termo de Referência SOGOV.pdf]] (fonte de autoridade; esta nota é só registro/rastreabilidade, nunca substitui o PDF). Lida diretamente por render de página (imagem), não por extração textual — a camada de texto do PDF é conhecida por corromper caracteres, então não foi usada como evidência. Todos os 23 itens deste recorte são requisitos de infraestrutura/operação técnica, sem subitens. Revisão concluída: os 23 itens foram reexaminados item a item contra o objetivo estrito do modelo (atores/entidades/dados/estados/configurações/dependências de negócio do preset) — nenhum define ou sustenta um elemento desse tipo; a classificação "Não aplicável" é confirmada para todos.

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
| 1.9 | Não aplicável | Monitoramento por aprendizado de máquina (ML) de anomalias de desempenho/recursos — observabilidade. |
| 1.10 | Não aplicável | Envio de e-mail (até 50 mil/dia, 14/s) — capacidade técnica de envio. |
| 1.11 | Não aplicável | Autenticação de remetente/anti-spam — infraestrutura de e-mail. |
| 1.12 | Não aplicável | Credenciais de banco, chaves de API, segredos, rotação automática — segurança operacional (nota "chaves" abaixo). |
| 1.13 | Não aplicável | Auditoria de acesso/alteração de credenciais de sistema — infraestrutura/segurança. |
| 1.14 | Não aplicável | Limitação do volume de requisições (rate limiting) e proteção contra DDoS — segurança de infraestrutura. |
| 1.15 | Não aplicável | Armazenamento seguro de documentos/arquivos, alta disponibilidade — durabilidade de armazenamento (infraestrutura). |
| 1.16 | Não aplicável | Armazenamento de grandes volumes, ciclo de vida/versionamento — infraestrutura de armazenamento. |
| 1.17 | Não aplicável | Proteção contra SQL Injection, XSS, DDoS — segurança de aplicação. |
| 1.18 | Não aplicável | Regras de segurança personalizadas, resposta automática a ataques — segurança operacional. |
| 1.19 | Não aplicável | Fila de mensagens entre serviços (assíncrono) — infraestrutura de mensageria. |
| 1.20 | Não aplicável | Múltiplas filas com prioridade/tempo de espera — infraestrutura de mensageria. |
| 1.21 | Não aplicável | Chaves criptográficas para proteção de dados — infraestrutura de criptografia (nota "chaves" abaixo). |
| 1.22 | Não aplicável | Controle de acesso às chaves criptográficas — segurança (nota "chaves" abaixo). |
| 1.23 | Não aplicável | Rastreamento de gargalos/falhas na infraestrutura — observabilidade. |

**Resultado do recorte:** 23/23 itens considerados; **23 Não aplicáveis** ao modelo de atores/entidades/dados de negócio — todos descrevem infraestrutura, segurança operacional ou observabilidade, sem ator/entidade/estado de negócio do SOGOV. Nenhum item pendente.

## Elementos identificados

| Referência do TR | Elemento | Tipo | Papel/descrição | Dados ou atributos relevantes | Certeza/evidência |
|---|---|---|---|---|---|
| | | | | | |

Não foram identificados elementos de negócio neste recorte. Os 23 itens descrevem capacidades técnicas da plataforma (hospedagem, banco de dados, rede, segurança, mensageria, criptografia, observabilidade).

## Relações/dependências identificadas

| Origem | Relação/dependência | Destino | Referência do TR | Certeza/evidência ou pendência |
|---|---|---|---|---|
| | | | | |

Não foram identificados elementos de negócio neste recorte; portanto, não há relação/dependência de negócio a registrar.

## Notas de interpretação

- **Instância de banco de dados (1.3):** o item usa "instância" no sentido de escalabilidade técnica do banco de dados — não se refere a cliente/tenant. Distinção útil para não confundir com outros usos do termo "instância".
- **Chaves (1.12, 1.21, 1.22):** os itens usam "chave(s)" no sentido de segredo técnico/criptográfico (chave de API, chave criptográfica). Distinção útil para não confundir com outros possíveis usos de "chave".

Nenhuma destas notas altera a classificação dos itens acima.

## Fontes/evidências

- PDF: `Fontes/Termo de Referência SOGOV.pdf`, p. 1 — lida por render de página (imagem), conferida diretamente nesta sessão em 08/10/2026. Nenhum trecho textual extraído (potencialmente corrompido) foi usado como evidência.
