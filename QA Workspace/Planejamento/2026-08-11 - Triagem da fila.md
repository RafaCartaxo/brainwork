---
tags:
  - qa
  - planejamento
---
# Triagem da fila — 11/08/2026

Parecer sobre os **75 itens parados 7+ dias**, gerado cruzando cada item contra o estado real do vault: pasta e `status` de cada card, arquivos em `Evidências/`, branches do repo `sogov-automation-test`. **Nada foi aplicado na fila** — isto é material de decisão.

> [!warning] O tamanho da fila é piso estrutural, não sujeira
> O `qa-atualiza.py` (função `sincroniza_demandas_ativas`) impõe um invariante: **todo card aberto** fora de `Concluídas/` precisa ter um item ativo na fila; se não tiver, ele cria `SGV-XXXX - Acompanhar (título)`. Com 37 cards abertos, a fila **não desce disso por poda** — apagar item só faz o próximo 🔄 recriar.
> 
> **O único jeito real de encurtar a fila é fechar card.**

## Resumo

- **manter**: 38 itens
- **precisa de você**: 30 itens
- **manter (gerado)**: 5 itens
- **revisar**: 2 itens

## Parecer item a item

| # | Idade | Item | Card | Parecer | Por quê |
|---|---|---|---|---|---|
| 1 | 28d | Detalhar passo a passo de reprodução da captura "despacho sigiloso aparece mesmo com config desativa | — | **precisa de você** | captura do Inbox nunca virou card |
| 2 | 27d | SGV-9971 - Acompanhar (Bug Assinatura Servidor Não Aprovado) | 9971: HML | **manter (gerado)** | criado pelo invariante da fila viva; só some quando o card fechar |
| 3 | 27d | SGV-9977 - Acompanhar (Bug Nome Oculto Cópia Despacho) | 9977: DEV | **manter (gerado)** | criado pelo invariante da fila viva; só some quando o card fechar |
| 4 | 26d | MEL-0001 - Cadastrar melhoria no Notion | — | **precisa de você** | registro externo atrasado |
| 5 | 25d | SGV-4873 - Refinar (material em 05 Refinar/ — bloqueada: aguardando responsável validar regra de ret | 4873: **sem card** | **precisa de você** | travado em terceiro há semanas — cobrar ou aceitar que morreu |
| 6 | 25d | SGV-9036 - Confirmar critérios no Notion e revisar o MR quando disponível | 9036: **sem card** | **precisa de você** | registro externo atrasado |
| 7 | 25d | Triagem SP15 - Bater os cards com o time, ponto a ponto (44/82 batidos; decisão entre parênteses em  | — | **precisa de você** | triagem de sprint parada há semanas |
| 8 | 25d | Triagem SP15 - Reexportar a view completa do Notion (Count 75; export ainda cortou em 53 no "Load mo | — | **precisa de você** | triagem de sprint parada há semanas |
| 9 | 22d | SGV-8977 - Atualizar no Notion (levar critérios atualizados pra task; validação real de volume/timeo | 8977: DEV | **precisa de você** | registro externo atrasado |
| 10 | 12d | SGV-10511 - Validar em HML os 3 cenários (aprovada em DEV, card já em `HML/`) | 10511: HML | **manter** | esperando fix chegar em HML; confirmei que o campo `deploy` segue no card |
| 11 | 12d | SGV-9493 - Revalidar o CT-019 quando o fix do SGV-10511 subir (reprovado em DEV — o CA5 só é aprovad | 10511: HML, 9493: DEV | **manter** | bloqueado em dev — nada a fazer até o fix subir |
| 12 | 12d | SGV-9493 - Executar em DEV os 15 CTs que ficaram em aberto (CT-017 a CT-031; começar pelo grupo I, q | 9493: DEV | **manter** | execução de teste pendente |
| 13 | 12d | SGV-9633 - Revalidar (reaberta em DEV — aguardar dev corrigir; "assinatura em fluxo de trabalho não  | 9633: **sem card** | **manter** | bloqueado em dev — nada a fazer até o fix subir |
| 14 | 12d | SGV-3412 - Validar em HML (aprovada em DEV, segue pra homologação) | 3412: HML | **manter** | trabalho real: CTs passaram em DEV, homologação não foi validada |
| 15 | 12d | SGV-9610 - Validar em HML (aprovada em DEV, segue pra homologação) | 9610: HML | **manter** | trabalho real: CTs passaram em DEV, homologação não foi validada |
| 16 | 12d | SGV-6906 - Revalidar (reaberta em homologação — aguardar dev corrigir a numeração/limpeza dos docume | 6906: HML | **manter** | bloqueado em dev — nada a fazer até o fix subir |
| 17 | 12d | SGV-9963 - Validar em homologação (task de API; MR !592 revisado e aprovado pela QA; fix já disponív | 9963: DEV | **manter** | trabalho real: CTs passaram em DEV, homologação não foi validada |
| 18 | 12d | SGV-7935 - Validar em homologação (MR !608 revisado — foco manual: evento de emissão exibido na time | 7935: DEV | **manter** | esperando fix chegar em HML; confirmei que o campo `deploy` segue no card |
| 19 | 12d | SGV-9638 - Validar em homologação (MR !619 revisado — conferir data atual no preview + botão de prev | 9638: DEV | **manter** | esperando fix chegar em HML; confirmei que o campo `deploy` segue no card |
| 20 | 12d | SGV-5360 - Validar em HML (aprovada em DEV, segue pra homologação) | 5360: HML | **manter** | trabalho real: CTs passaram em DEV, homologação não foi validada |
| 21 | 12d | SGV-7829 - Revalidar (reaberta em homologação — atendimento parcial, imagem não carrega; sem bloquei | 7829: HML | **manter** | bloqueado em dev — nada a fazer até o fix subir |
| 22 | 12d | SGV-6373 - Revalidar (reaberta em DEV — setores das Regras de tramitação não mantidos ao avançar/ret | 6373: DEV | **manter** | bloqueado em dev — nada a fazer até o fix subir |
| 23 | 12d | SGV-6628 - Validar em HML (aprovada em DEV, segue pra homologação) | 6628: HML | **manter** | trabalho real: CTs passaram em DEV, homologação não foi validada |
| 24 | 12d | SGV-5103 - Revalidar (reaberta em DEV — mensagem de erro ao alternar para prefeitura onde servidor e | 5103: DEV | **manter** | bloqueado em dev — nada a fazer até o fix subir |
| 25 | 12d | SGV-9681 - Validar melhoria em HML (aprovada em DEV, segue pra homologação) | 9681: HML | **manter** | trabalho real: CTs passaram em DEV, homologação não foi validada |
| 26 | 12d | SGV-9405 - Validar em HML (aprovada em DEV, segue pra homologação) | 9405: HML | **manter** | trabalho real: CTs passaram em DEV, homologação não foi validada |
| 27 | 12d | SGV-9405 - Ao validar em HML, conferir o rodapé inteiro e nos dois cenários de paginação — não só o  | 10457: HML, 9405: HML | **manter** | execução de teste pendente |
| 28 | 12d | SGV-9493 - Acompanhar (Melhoria Adequacao Do Sogov Para Novo Formato De CNPJ) | 9493: DEV | **manter (gerado)** | criado pelo invariante da fila viva; só some quando o card fechar |
| 29 | 12d | SGV-10512 - Acompanhar correção (CNPJ anonimizado na impressão; bug pré-existente em produção) | 10512: DEV | **manter** | bloqueado em dev — nada a fazer até o fix subir |
| 30 | 12d | SGV-10517 - Acompanhar correção (busca do campo de solicitante não retorna com máscara; pré-existent | 10517: DEV | **manter** | bloqueado em dev — nada a fazer até o fix subir |
| 31 | 12d | SGV-10517 - Confirmar com o Waldemar se o defeito que ele abriu no `TC-712` (CT-016, "busca por CNPJ | 10517: DEV | **precisa de você** | depende de conversa externa — decidir se ainda vale perseguir |
| 32 | 12d | SGV-10512 - Confirmar com produto se a anonimização do CNPJ na impressão é intencional e documentar  | 10512: DEV | **precisa de você** | depende de conversa externa — decidir se ainda vale perseguir |
| 33 | 12d | SGV-10451 - Acompanhar correção (toolbar de documento encerrado sem histórico nem baixar) | 10451: HML | **manter** | bloqueado em dev — nada a fazer até o fix subir |
| 34 | 12d | SGV-10451 - Exportar a tabela de permissões de encerramento e alimentar a doc de Tramitação (posterg | 10451: HML | **precisa de você** | lacuna de documentação; não bloqueia validação hoje |
| 35 | 12d | SGV-10457 - Acompanhar correção (espaçamento do rodapé + numeração sobreposta) | 10457: HML | **manter** | bloqueado em dev — nada a fazer até o fix subir |
| 36 | 12d | SGV-10404 - Acompanhar (download de assinaturas autenticáveis ignora a página extra) | 10404: HML | **manter (gerado)** | criado pelo invariante da fila viva; só some quando o card fechar |
| 37 | 12d | SGV-6136 - Acompanhar decisão do dev (não reproduziu em homologação; ele vai verificar se sobe o fix | 6136: **sem card** | **manter** | bloqueado em dev — nada a fazer até o fix subir |
| 38 | 12d | SGV-9610 - Iniciar automação (repo `sogov-automation-test`) — plano em SGV-9610 - Plano de Automação | 9610: HML | **manter** | bloqueada no gate 2: MR !537 ainda não está em HML |
| 39 | 12d | Acompanhar [MR !24](https://gitlab.sogo.com.br/qa_sogov/sogov-automation-test/-/merge_requests/24) ( | — | **manter** | conferi no repo: as branches seguem abertas, não foram mergeadas |
| 40 | 12d | Acompanhar [MR !25](https://gitlab.sogo.com.br/qa_sogov/sogov-automation-test/-/merge_requests/25) ( | — | **manter** | conferi no repo: as branches seguem abertas, não foram mergeadas |
| 41 | 12d | SGV-4873 — avisar o responsável/time que o status do Notion ("Disponível para homologação") está des | 4873: **sem card** | **precisa de você** | depende de conversa externa — decidir se ainda vale perseguir |
| 42 | 12d | SGV-8977 — confirmar com Rafael/time o que aconteceu na reabertura ("Reaberto" no Notion) antes de s | 8977: DEV | **precisa de você** | depende de conversa externa — decidir se ainda vale perseguir |
| 43 | 12d | SGV-9464 × doc Rastrear Documento - Confirmar com Dev/Produto se a doc está desatualizada e atualiza | 9464: Concluídas | **precisa de você** | travado em terceiro há semanas — cobrar ou aceitar que morreu |
| 44 | 12d | SGV-10393 - Acompanhar (aviso de "Assinaturas digitais" ao emitir e assinar como cidadão) | 10393: DEV | **manter** | bloqueado em dev — nada a fazer até o fix subir |
| 45 | 12d | Triagem Sprint atual - Reexportar as abas `Em homologação` e `Pronto` da view do Devs workspace (o e | — | **precisa de você** | triagem de sprint parada há semanas |
| 46 | 8d | SGV-10572 - Testar com a página de assinaturas separada desativada (é o 2º critério e o que isola a  | 10572: DEV | **manter** | cenário complementar que isola a causa — trabalho seu, executável |
| 47 | 8d | SGV-10549 - Verificar as superfícies vizinhas: o servidor editando um cidadão PF, e o cidadão altera | 10549: DEV | **manter** | cenário complementar que isola a causa — trabalho seu, executável |
| 48 | 8d | SGV-10607 - Testar o mesmo cenário no download do documento, não só na impressão (a página de assina | 10607: DEV | **manter** | cenário complementar que isola a causa — trabalho seu, executável |
| 49 | 8d | SGV-10608 - Separar os dois cenários do achado 3: retificar a resposta (defeito) × retificar o princ | 10608: DEV | **manter** | cenário complementar que isola a causa — trabalho seu, executável |
| 50 | 8d | SGV-10458 - Revalidar (reaberta em DEV — cenário a reconstituir pela task no Notion) | 10458: DEV | **manter** | reabertura pendente de reteste |
| 51 | 8d | SGV-10468 - Revalidar (reaberta em DEV — cenário a reconstituir pela task no Notion) | 10468: DEV | **manter** | reabertura pendente de reteste |
| 52 | 8d | SGV-10482 - Atualizar no Notion (levar os 5 critérios de aceite pra task; o dev Washington está com  | 10482: DEV | **precisa de você** | registro externo atrasado |
| 53 | 8d | SGV-10482 - Acompanhar correção (falha na geração com 3 anexos DWG; dev Washington, previsão 11/08) | 10482: DEV | **manter** | bloqueado em dev — nada a fazer até o fix subir |
| 54 | 8d | SGV-10482 - Obter o nome do 3º arquivo DWG com quem abriu a task (a descrição fala de 3 anexos, o ex | 10482: DEV | **precisa de você** | falta insumo que só você consegue — card fica inexecutável sem isso |
| 55 | 8d | Dizer o que são as 3 gravações soltas de hoje — `herança nok.mp4` (13:56, parece achado novo de hera | — | **precisa de você** | evidência solta esperando você identificar o SGV/CT |
| 56 | 8d | SGV-9493 - Dizer qual CT cobre cada gravação (`9493 - 1.mp4` e `9493 - 3.mp4`, já em `Desenvolviment | 9493: DEV | **precisa de você** | evidência solta esperando você identificar o SGV/CT |
| 57 | 8d | SGV-10549 - Confirmar com produto se errar a senha nessa tela conta pro bloqueio de conta por 5 tent | 10549: DEV | **precisa de você** | depende de conversa externa — decidir se ainda vale perseguir |
| 58 | 8d | 📚 Importar doc do Revisor de Anexos — não existe em `04 Conhecimento/Módulos/` (fluxo 8). Escopo red | 10482: DEV, 8698: **sem card** | **precisa de você** | lacuna de documentação; não bloqueia validação hoje |
| 59 | 8d | Descobrir quais arquivos `.dwg` são válidos (tamanho, versão do formato) — a doc de Despachos diz qu | 10482: DEV | **precisa de você** | lacuna de documentação; não bloqueia validação hoje |
| 60 | 8d | Confirmar se a menção via `@` está implementada (doc de 13/05; segue como item de backlog da página  | 5152: Concluídas | **revisar** | sem regra automática — julgar no contexto |
| 61 | 8d | Dizer o que é a gravação `10505.mp4` na raiz de `Evidências/` (apareceu 31/07 16:46, nome já com núm | 10505: **sem card** | **precisa de você** | evidência solta esperando você identificar o SGV/CT |
| 62 | 8d | Decidir as 5 propostas abertas de 31/07 sobre o `qa-atualiza.py` e o FLUXOS — `"analis"` na tupla do | — | **precisa de você** | **uma delas é o teto do 🚨 — exatamente o problema de hoje** |
| 63 | 8d | SGV-10549 - Acompanhar correção (senha incorreta sem feedback na alteração de e-mail do cidadão PJ;  | 10549: DEV | **manter** | bloqueado em dev — nada a fazer até o fix subir |
| 64 | 8d | SGV-10572 - Acompanhar correção (assinatura da PJ sem o representante legal na página separada; cada | 10572: DEV | **manter** | bloqueado em dev — nada a fazer até o fix subir |
| 65 | 8d | SGV-5152 - Decidir com produto qual regra de permissão vale pra cancelar e retificar: são três formu | 5152: Concluídas | **revisar** | sem regra automática — julgar no contexto |
| 66 | 8d | Despachos - Abrir a página no Notion e ler o callout truncado no fim da seção Extensão DWG (os dois  | 10482: DEV | **precisa de você** | lacuna de documentação; não bloqueia validação hoje |
| 67 | 8d | Despachos - Expandir o "1 more…" do backlog da página antes de exportar — o 6º item segue desconheci | — | **precisa de você** | lacuna de documentação; não bloqueia validação hoje |
| 68 | 8d | SGV-5152 - Levar pra produto a divergência de permissão que sobrou, a de retificar: "apenas o criado | 5152: Concluídas | **precisa de você** | depende de conversa externa — decidir se ainda vale perseguir |
| 69 | 8d | SGV-10596 - Acompanhar (Bug Autor Nao Consegue Cancelar O Proprio Despacho) | 10596: DEV | **manter (gerado)** | criado pelo invariante da fila viva; só some quando o card fechar |
| 70 | 8d | SGV-10596 - Levar pra produto a redação da regra de permissão: pela letra, o N2 cancela despacho de  | 10596: DEV | **precisa de você** | depende de conversa externa — decidir se ainda vale perseguir |
| 71 | 8d | SGV-10607 - Acompanhar correção (assinatura de resposta retificada saindo na impressão) | 10607: DEV | **manter** | bloqueado em dev — nada a fazer até o fix subir |
| 72 | 8d | SGV-10607 - Confirmar com produto como a assinatura invalidada deve aparecer na saída do despacho re | 10607: DEV | **precisa de você** | depende de conversa externa — decidir se ainda vale perseguir |
| 73 | 8d | SGV-10608 - Acompanhar correção (3 achados da retificação: aviso, botão e copy) | 10608: DEV | **manter** | bloqueado em dev — nada a fazer até o fix subir |
| 74 | 8d | SGV-10608 - Anexar os textos literais: o aviso do achado 1, a copy do achado 3 e o que está fora do  | 10608: DEV | **precisa de você** | falta insumo que só você consegue — card fica inexecutável sem isso |
| 75 | 8d | SGV-10458 e SGV-10468 - Trazer da task o título, o cenário e o módulo dos dois — hoje os cards são s | 10458: DEV, 10468: DEV | **precisa de você** | falta insumo que só você consegue — card fica inexecutável sem isso |

## Fechado em 11/08

- ✅ *Nomear as 2 gravações de 30/07* — **provado feito**: as 15 evidências da SGV-9042 estão nomeadas em `EV-NN` e não existem mais na raiz.
- ✅ *SGV-5152 - Reexportar task com subitens* — propósito extinto com a aprovação e o encerramento da feature.
- ✏️ *Confirmar se Retificar despacho e menção `@` estão implementados* — **reescrito**, não fechado: o retificar foi respondido pela SGV-5152; sobrou só a menção `@`.
- 🏁 **SGV-9042 finalizada**, movida pra `Concluídas/` (entrega em produção).

## O que eu não fechei, e por quê

**Os 7 cards em `HML/` com 100% dos CTs verdes** — SGV-3412, 5360, 6628, 9405, 9610, 9681 e 10511.

É sinal enganoso: aqueles CTs foram executados **em DEV** (o Histórico de cada um diz *"aprovada em DEV — segue pra homologação"*) e o card está em `HML/` justamente **aguardando a validação de homologação**. Fechar por esse sinal seria dar por validado o que nunca foi testado em HML.

A única exceção era a **SGV-9042**, cujo Histórico registra validação **em homologação** com 22/22 critérios e 21/21 CTs — e essa foi finalizada.
