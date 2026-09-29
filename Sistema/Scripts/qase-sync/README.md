# Scripts de sincronização com a Qase

Ferramentas reutilizáveis que sobem casos de teste do vault (Obsidian) pro projeto `SGV` na Qase TestOps (API REST). Vivem **aqui, no vault** — não no repositório de automação (`sogov-automation-test`), que é só pro Cypress. Processo completo (mapeamento de campos, GATES, shared steps, idempotência): [[../../Skills/SKILL_SYNC_QASE|SKILL_SYNC_QASE]].

## Setup (self-contained, não depende do repo)

- **`.env`** — nesta pasta, com `QASE_TESTOPS_API_TOKEN`. Compartilhado por todas as subpastas (cada `sync.js` carrega `../.env` relativo a si mesmo).
- **`package.json`** — só `dotenv` como dependência. Rodar `npm install` aqui uma vez se `node_modules/` não existir.

## Estrutura

```
qase-sync/
├── .env                        (token, não versionado — ver .gitignore do vault)
├── package.json / package-lock.json
├── node_modules/
├── <contexto-1>/                (ex.: 9296-departamentos)
│   ├── sync.js
│   ├── corrections.json
│   └── README.md
├── <contexto-2>/                (ex.: 9982-tramitacao)
│   └── ...
└── <contexto-3>/                (ex.: 1.24-1.25)
    └── ...
```

Cada sincronização ganha sua própria subpasta, nomeada só pelo **contexto** (sem prefixo `qase-sync-` — isso já está no nome da pasta pai). Pra uma sincronização nova, copiar o `sync.js` da **versão mais recente já usada** (hoje `9296-departamentos/`, com shared steps + idempotência real — não `1.24-1.25/`, mais simples e congelada) pra uma subpasta nova com o contexto certo.

## Como rodar (de dentro da subpasta do contexto)

```bash
cd Sistema/Scripts/qase-sync/<contexto>/
node sync.js                      # dry-run: só imprime, não chama a API
node sync.js --apply --only=<id>  # teste isolado de 1 update de baixo risco
node sync.js --apply              # lote completo
node sync.js --inspect=<id>       # só leitura — confirma campo real de um caso já existente
```

## Histórico das migrações

- **25/09/2026**: scripts removidos do repo `sogov-automation-test` (nunca tinham ido pro `origin/main`) e movidos pra cá, self-contained. Motivo: ferramenta de QA que só chama a API da Qase não precisa do ambiente Cypress do repo — vivendo no vault, fica junto do resto do processo de QA e não depende de clonar/instalar o repo de automação só pra isso.
