---
tags:
  - qa
  - termo-de-referencia
---
# 07 Termo de Referência

Verificação de conformidade do Sogov com os Termos de Referência — trabalho recorrente, com vida própria: casos de teste → sincronização com a Qase → automação, por faixa de itens do Termo. Não é aprendizado ad-hoc ([[../06 Estudos/README|06 Estudos]]) nem segue o ciclo DEV→HML→Concluída de card/SGV ([[../02 Demandas/README|02 Demandas]]).

## Estrutura

Uma subpasta por faixa de itens do Termo, numerada pelo próprio item (ex.: `1.24-1.25`). Cada uma segue o mesmo padrão interno — ver o `README.md` de dentro dela pra detalhes:

| Faixa | Escopo | Status |
|---|---|---|
| [[1.24-1.25/README\|1.24-1.25]] | Autenticação e ciclo de vida do usuário | Casos de teste e sincronização Qase concluídos; automação em andamento |

## Regras de uso

1. **Uma subpasta por faixa de itens do Termo**, nomeada só pela faixa (ex.: `1.26-1.27`), seguindo a mesma estrutura interna de `1.24-1.25/` (`01 Casos de Teste`, `02 Sincronização Qase`, `03 Automação`, `Histórico`, `README.md`).
2. **Atualizar a tabela acima** ao criar uma faixa nova.
3. Ver `README.md` de cada faixa pra regras específicas dela (fonte única, ordem de atualização vault→Qase, etc.).
