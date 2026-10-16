---
tags: [qa, conhecimento, automacao]
tipo: referencia
revisado: 2026-10-16
---
# Primeiros passos — automação Playwright

Setup do zero. Todo o resto (comandos do dia a dia, como uma execução funciona, regras de escrita) está em `~/Documentos/Sogov/sogov-automation-test/playwright/README.md` — ver [[00 - Índice da automação Playwright]].

## Instalação

Comandos validados de verdade nesta máquina (16/10/2026):

```bash
cd ~/Documentos/Sogov/sogov-automation-test/playwright
npm install                        # NÃO "npm ci" — não existe package-lock.json no pacote, `npm ci` falha na hora
npx playwright install chromium    # pode já estar em cache na máquina (foi instantâneo)
npm run test:infra                 # confirma a config sem tocar no ambiente — 55/55 passou
```

> [!warning] `npm ci` não funciona
> O `package-lock.json` nunca foi versionado em `playwright/`. `npm ci` falha de saída. (O README do repo ainda manda usar `npm ci` — diverge do que foi verificado aqui.) Consequência: as dependências diretas estão pinadas, mas as transitivas não são reproduzíveis entre máquinas. Vale propor ao time versionar o lockfile.

## Configuração do `.env`

Copiar `playwright/.env.example` para `playwright/.env` e preencher os valores reais. O `.env` fica fora do git.

> [!danger] Valores reais não entram no vault
> Senhas e credenciais são segredo; não documentar aqui. Para saber de onde os valores vinham historicamente (variáveis `GUI_BASE_URL`, `API_URL` etc. do lado Cypress), ver o apêndice de [[02 - Migração Cypress → Playwright]].

## Depois do setup

Seguir o `playwright/README.md`, seções 1 e 2 (comandos), e a [[00 - Índice da automação Playwright|índice]] para o resto.
