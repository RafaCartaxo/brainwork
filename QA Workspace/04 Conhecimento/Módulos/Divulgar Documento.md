---
title: Divulgar Documento
tags:
  - qa
  - conhecimento
  - sogov
  - divulgacao
  - mural
tipo: modulo
revisado: 2026-10-13
fonte: https://app.notion.com/p/alfa-group/Divulgar-documento-18fc8a32272546db9e601b62e2a76a6d
fonte_criado: 2024-07-08 (Rafael)
fonte_ultima_edicao: 2026-05-12 (Fernando Junior)
---
# Divulgar Documento

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-10-13 — a página do Notion continua sendo a fonte de verdade externa; esta cópia é o acervo local pesquisável. Sem task própria (campo `Task` vazio no Notion). O export veio com ruído (um trecho de texto aparentemente digitado por engano, links de âncora quebrados, palavras coladas por falta de espaço) que foi limpo preservando o sentido original; na dúvida sobre o que uma frase cortada queria dizer, a lacuna foi registrada em vez de completada.

## Visão geral
- Funcionalidade que permite divulgar documentos do tipo **Documento Oficial** e **Comunicação Oficial**: no **mural** interno do órgão (servidores) e/ou no **jornal oficial** da central de atendimento (canal externo, público). Exige o módulo com o parâmetro **"Permite divulgação em canal de comunicação oficial"** ativado, com dois canais independentes:
	- **Canal interno** — documento divulgado no mural de servidores do órgão.
	- **Canal externo** — documento divulgado no jornal oficial do órgão (central de atendimento, acesso público).

## Regras de negócio

### Regras comuns aos dois canais
- Documento só pode ser **divulgado** depois de **emitido**, mas a **configuração** da divulgação pode ser feita em qualquer fase de vida: na abertura, em elaboração, em tramitação ou já encerrado (encerrado não precisa retornar à tramitação pra configurar).
- **Agendamento**: limitado a 30 dias de antecedência e nunca ultrapassando 31/12 do ano vigente — vale tanto configurando na abertura/em elaboração quanto num documento já emitido (motivo: atualização do quadro de servidores na prefeitura). O servidor retoma novos agendamentos só no ano seguinte.
	- Exemplo do export: um servidor querendo divulgar em 20/12 só pode agendar até 11 dias de antecedência, respeitando o teto de 31/12.
- Exemplos de documentos oficiais tipicamente divulgados (canal externo): Leis, Portarias, Decretos, Instruções normativas, Editais.

### Canal interno — Mural

> O mural é o quadro de avisos interno do órgão, na tela inicial de cada servidor, exibindo os documentos/comunicações configurados pra ele.

**Configurando na abertura**
- Usuário define: lista de setores setados na regra de tramitação do módulo (que podem receber e tramitar) + momento da divulgação (imediatamente após a emissão, ou X dias após).
- Ao bater os requisitos, documento é divulgado no mural dos setores e notificação é enviada — **só no momento em que a divulgação de fato acontece**, não na configuração.
- Antes de salvar/emitir, toda a configuração ainda pode ser editada ou totalmente excluída.

**Configurando/editando em elaboração**
- Com configuração existente: pode editar ou excluir totalmente.
- Sem configuração: pode criar, com as mesmas opções da abertura.

**Documento já emitido (em tramitação ou encerrado)**
- Pode editar configuração existente ou criar uma nova.
- **Editando configuração já executada** (divulgação já realizada): pode **retirar** a divulgação de um setor pré-setado — ao confirmar, o documento some do mural dos servidores daquele setor e eles perdem o acesso (sem notificação de aviso; se tentarem acessar, veem mensagem de que não têm acesso). **Exceção**: servidor de setor que já está envolvido no documento mantém acesso mesmo com a retirada.
- **Editando configuração já executada** também permite **adicionar novos setores**, com opção de divulgação imediata ou em **data futura específica** (aqui não é mais "X dias", é uma data).
- **Configuração ainda não executada** (data agendada não chegou): pode editar tudo, inclusive excluir.
- **Criando configuração nova** (documento emitido sem config ainda): mesmos dados — setores + timing (imediatamente ou data futura específica).
- Documentos divulgados no mural **não vão para a mesa dos setores** divulgados, e esses setores não entram como "envolvidos" só por causa da divulgação — por isso só recebem notificação se também estiverem envolvidos no documento por outro motivo.

**Acessando o documento pelo mural**

| Status do doc | Servidor é de setor já envolvido | Servidor não é de setor envolvido |
|---|---|---|
| Em tramitação ou pausado | Pode se envolver (se ainda não envolvido) ou interagir conforme o status (se já envolvido) | Pode se envolver — isso envolve o setor também, e o documento vai pra mesa do servidor e do setor, status Em tramitação. **Exceção**: documento com tipo de interação **Caráter informativo** — servidor de fora não pode interagir nem se envolver |
| Encerrado | Setor dono (N1 ou N2): pode **reabrir**. Setor envolvido ou N3 do setor dono: só **imprimir e ver histórico** | Só **imprimir e ver histórico** |

**Outras regras (mural)**
- Servidor ou setor que encerrou a tramitação na própria mesa pode reabrir **pra si**, desde que o setor dono ainda esteja em tramitação. Se o setor dono já encerrou, só ele pode reabrir.
- Documento com tipo de interação **Caráter informativo**: após emitido/em tramitação, setores envolvidos e dono só têm Histórico, Imprimir, Retificar, Revogar e Encerrar (cada um no seu caso) — sem as demais interações.
- Toda ação que gera notificação vai só pros setores **envolvidos** — setor setado só pra divulgação no mural precisa estar envolvido na tramitação pra também receber notificação.
- Documentos divulgados (ou com config pré-setada) devem ser identificados nos cards das mesas, tanto no modo painel quanto no modo lista.
- Precisa de **permissão extra** específica pra divulgação no mural.
- Quem pode configurar a divulgação: export cita só "Setor dono: N1" antes de listar as seções acima, sem detalhar os demais perfis — ver Dúvidas em aberto.

### Canal externo — Central de Atendimento (jornal oficial)

> Dá ciência pública aos atos de gestão do órgão. Documentos divulgados ficam na Central de Atendimento, em área própria, acessível **livremente e sem login**.

**Configurando na abertura**
- Só define o **momento** da divulgação (imediatamente após a emissão, ou X dias após) — não há lista de setores aqui, já que é divulgação pública.
- Ao bater os requisitos, documento vai pra Central de Atendimento e notificação é enviada aos setores **envolvidos no documento**, avisando da divulgação.
- Editável/excluível por completo antes de salvar/emitir.

**Configurando/editando em elaboração** — mesmo padrão do canal interno (editar/excluir se já existe; criar com as mesmas opções, se não existe).

**Documento já emitido (em tramitação ou encerrado)**
- **Editando configuração já executada**: pode retirar a divulgação da central. Se um cidadão tinha salvo o link direto e tenta acessar depois da retirada, vê mensagem de que o documento não está mais disponível.
- **Configuração ainda não executada**: pode editar tudo, inclusive excluir.
- **Criando configuração nova**: timing imediato ou data futura específica.
- **Importante**: só o **conteúdo do documento de abertura** fica disponível na central — nunca a timeline de eventos nem interações via despacho, associação de processos etc.

**Acessando na Central de Atendimento**
- Área própria, documentos divididos por **Módulo** e subdivididos por **Assunto**.
- Listagem: filtro/ordenação por Módulo e Assunto; busca por palavra-chave (Módulo, Assunto, conteúdo do documento, número do documento); ordenação mais recente↔mais antigo; filtro por data/range de data.
- Acessando um documento: só a versão de abertura, com header simplificado — Nome do módulo, Nome do assunto (se houver), Setor dono, Data/hora de emissão, Conteúdo do formulário de abertura, Assinaturas (se houver), Anexos (se houver). Opção de imprimir com a mesma informação.

### Perguntas e respostas pós-entrega (e-mail de 03/07/2024, Figma Handoff Virtus 8)
- **"Novas citações" na central funciona como na mesa (menções, só não vistas)?** → Sim, exibe só a quantidade de menções ainda não visualizadas.
- **Data exibida no card é de divulgação ou de emissão?** → Data de **divulgação**.
- **Ordem cronológica considera qual atributo? Aparece mesmo sem documento divulgado?** → Em "Documentos Oficiais" da central só aparecem módulos com **ao menos um documento divulgado externamente**; ordenados pelo módulo com divulgação **mais recente**.
- **E quando o documento não tem texto breve?** → Exibe nome do módulo seguido do serviço/assunto, se houver.
- **Ao clicar em "visualizar", abre ou baixa o PDF?** → Abre o documento em **nova aba do navegador**.

### Atualização — Exibição do título na tabela de documentos oficiais (11/05/2026)
- Documento com algum campo configurado como **título** → exibe esse título no lugar do primeiro campo de texto breve.
- Documento sem campo de título configurado → mantém a regra atual, exibe o texto breve.

## Comportamentos observados em teste
<!-- O que foi aprendido validando: comportamentos não documentados, pegadinhas, efeitos colaterais -->
- Ainda não testado — importação é só a documentação de referência.

## Dúvidas em aberto
- [ ] A frase "A seguir estão definidos os servidores que poderão realizar a divulgação de documento — Setor dono: N1" aparece **duas vezes** no export (mural e canal externo), mas o conteúdo que segue nunca detalha os níveis além de citar "N1" — confirmar quais perfis, de fato, podem configurar divulgação (só setor dono N1? Admin também?).
- [ ] No canal externo, "Editando configurações de documentos emitidos" traz a frase **"ou seja, a já tenha sido realizada"** — comparando com a redação equivalente do mural ("ou seja, a divulgação já tenha sido realizada"), o export do canal externo parece ter perdido a palavra "divulgação" nessa frase. Tratado aqui como o mesmo sentido do mural, mas vale confirmar no Notion.
- [ ] Trecho da seção "Divulgando no mural" veio com um texto solto sem sentido no export ("DSSFSDFSEDFSE", após a definição do mural) — removido na limpeza por ser claramente ruído de digitação, não conteúdo.
- [ ] Datas inconsistentes no export da seção de atualização de título: o cabeçalho da seção diz "@May 12, 2026" (mesma data do `fonte_ultima_edicao`), o texto interno diz "Atualização em 11/05/2026" (um dia antes) e a assinatura do comentário mostra **"Bruna J C, 10/22/2025 — Adicionado @October 22, 2025"** (mais de 6 meses antes das outras duas datas). Possível artefato de exportação/comentário reaproveitado — mantido como está, sem inventar qual data é a correta.
- [ ] Dois itens do backlog do Notion vinculados a esta página (ver Cards relacionados) ainda sem SGV e sem detalhamento de escopo no export.

## Cards relacionados
<!-- SGVs validados que tocam este módulo -->
- Nenhum SGV cadastrado ainda para o módulo em si (documentação de referência desde 08/07/2024, sem task própria no Notion).
- Backlog vinculado no Notion, sem SGV:
	- **[Melhoria]** Exibir anexos dos documentos divulgados na central de atendimento.
	- **[BUG - POC Natal]** Busca por nome de documentos divulgados na central de atendimento não funciona.
- [[QA Workspace/02 Demandas/DEV/SGV-11262 - [QA-Automação] Termo de Referência SOGOV/SGV-12082 - Mapeamento de atores e modelo do preset do TR/00 QA/01 - Demanda|SGV-12082]] tem pendência em aberto desde 09/10 pra "esclarecer se Canal Oficial e Jornal Oficial são elementos distintos no produto" — esta doc responde: são o **mesmo parâmetro** (`Permite divulgação em canal de comunicação oficial`), com dois canais internos a ele — **Canal interno** (mural) e **Canal externo**, que o texto do Notion chama de "jornal oficial do órgão" (seção "Divulgando no canal externo"). Não são dois elementos distintos, e sim dois modos do mesmo canal/parâmetro.

## Referências
<!-- Docs do repo (caminho), links externos, leis -->
- Notion (fonte): ver `fonte` no frontmatter.
- Figma (Handoff Virtus 8, e-mail 03/07/2024): https://www.figma.com/design/d6dxKe1coa1U7lelm0mbJf/Handoff-Virtus-8
