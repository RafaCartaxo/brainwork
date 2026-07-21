---
title: Rastrear Documento
tags:
  - qa
  - conhecimento
  - sogov
  - rastrear-documento
  - busca
tipo: modulo
revisado: 2026-07-20
fonte: https://app.notion.com/p/alfa-group/Rastrear-documento-2922aec67d30805fb768f15d4d1f8e12
fonte_criado: 2025-10-20 (Vinícius)
fonte_ultima_edicao: 2026-03-25 (Edu)
---
# Rastrear Documento

> [!info] Origem
> Importado do Notion (link em `fonte`) em 2026-07-20. A página do Notion continua sendo a fonte de verdade externa; esta cópia é o acervo local pesquisável. O link do Figma referenciado no export ("Ambiente Servidor — Handoff") não foi trazido — consultar o Notion/Figma pra referência visual. Ao detectar divergência com o sistema em teste, atualizar aqui e registrar em [[#Comportamentos observados em teste]].

## Visão geral

Feature de busca global de documentos, acessível a partir de um botão "Rastrear Documento" no topheader do SOGOV (disponível em qualquer área da plataforma, para usuário servidor já logado). Antes desta feature, a localização de documentos fora da Central de Atendimento (busca por código de rastreio) só era possível pela [[Mesa de trabalho]] do próprio servidor, limitada aos setores dos quais ele participava.

A busca abre em um modal (mantendo o usuário no contexto/área em que estava) e oferece dois modos alternáveis por toggle:
- **Busca padrão**: filtros avançados (texto, tipo de documento, período, escopo de setor);
- **Busca por Código de Rastreio**: campo único para busca direta e precisa.

O usuário pode definir o escopo da busca padrão entre seus próprios setores (default) ou os setores dos quais não participa.

## Regras de negócio

### Escopo e modos de busca

- **Toggle "Buscar por código de rastreio"**: desativado por padrão. Ao ativar, simplifica a interface do modal para um único campo (`input-search`, placeholder "Digite o código de rastreio"), ocultando os demais filtros;
- **Radio-buttons de escopo** (visíveis na busca padrão): "Buscar em meus setores participantes" (selecionado por padrão) ou "Buscar em setores que não participo";
- **Campo Ano**: obrigatório, aceita 4 caracteres, vem preenchido por padrão com o ano vigente;
- **Campo Mês**: vem preenchido por padrão com "Todos".

### Busca padrão (Fluxo A — meus setores)

- **Input-search**: busca ampla por CPF, CNPJ, nome de servidor ou cidadão, número ou título de documento. Requer **mínimo de 3 caracteres**;
- **Regra de máscara**: o campo deve suportar CPF/CNPJ com pontuação (pontos, traços, barras); o sistema preserva visualmente o que foi digitado/colado, mas a busca funciona independente da presença de pontuação;
- **Select "Tipo de documento"**: seleção de um ou mais tipos (módulos, serviços e assuntos);
- **Campos obrigatórios da busca padrão**: `input-search` e "Tipo de documento". Ausência de qualquer um deles bloqueia a busca com informativo de obrigatoriedade;
- Preenchimento do `input-search` com menos de 3 caracteres retorna informativo pedindo melhor descrição da busca.

### Resultados da busca padrão

- **≤ 4 resultados**: exibidos diretamente no modal, em cards clicáveis (redireciona à página do documento, se houver permissão; sem permissão, só é possível ver a existência do documento);
- **> 4 resultados**: redireciona para página de resultados dedicada, com listagem completa e paginação;
- **Ordem de apresentação** (ambos os cenários): primeiro documentos ativos (movimentação mais recente → mais antiga), depois documentos encerrados (mesma ordenação);
- **Filtro de status** (só existe no cenário de página dedicada, > 4 resultados): retorna documentos com status "Em aberto", "Em tramitação", "Pausado" ou "Encerrado". Decisão registrada no export (discussão de 10/02/2026 com Lucas Beninca, Vinícius e Edu): o status considerado pelo filtro é o do **setor dono** do documento, não do setor onde ele está no momento — decidiu-se assim pra não complexificar o rastreio de fase do documento;
- **Filtro "documentos importados"** (só na página dedicada): ao ativar, ordenação passa a priorizar a Data de Criação original (mais recente → mais antiga);
- **Botão "Novo rastreio"** (canto superior direito da página de resultados): reabre o modal de busca sem apagar ou navegar para fora da página de resultados atual — a busca recomeça do zero mantendo os resultados anteriores visíveis ao fundo.

### Busca por Código de Rastreio (Fluxo B)

- Campo único, sem os demais filtros;
- **Campo vazio** → erro "Campo obrigatório";
- **Código inválido** → erro "Código inválido";
- **Código válido + acesso permitido**: modal exibe card único com dados do documento, clicável, pode abrir em nova aba;
- **Código válido + acesso restrito**: modal exibe card informativo com dados públicos do documento e indicação "Sem acesso"; card não é clicável;
- **Documentos associados** (ver [[Associar e Desassociar]]): se o documento buscado tiver documentos associados, a existência de emissão/tramitação deles é exibida, mas só é acessível se o usuário/setor tiver permissão;
- **Usuários com permissão de visualizar mesas alheias**: mantêm essa permissão na busca (maior retorno possível de documentos acessíveis), mas continuam restritos a nível de pessoa/setor para documentos sigilosos;
- **Documentos sigilosos**: seguem a mesma regra já existente hoje para mesas (ver [[Mesa de trabalho]]) — são visíveis/buscáveis, mas só exibem a tramitação (não o conteúdo de abertura, despachos e afins), igual à regra atual de demandas sigilosas.

### Busca em setores que não participo (Fluxo C)

- Segue a mesma lógica do Fluxo A (busca padrão), mudando o radio-button de escopo;
- Resultados ordenados por atualização mais recente; documentos acessíveis aparecem primeiro, seguidos dos com status visual "Acesso Restrito" (não clicáveis);
- **Exceção 1**: se a busca é em setores que não participo, mas o documento encontrado envolveu algum setor no qual o usuário está lotado, o acesso é permitido (aplicam-se as regras de acesso desse setor);
- **Exceção 2**: se o documento pertence a outros setores mas o usuário está envolvido nele diretamente, o acesso também é permitido, aplicando-se as regras de privacidade cabíveis.

### Busca não encontrada (Fluxo D)

- Empty state: título "Nenhum resultado encontrado para sua busca" + texto de apoio "Verifique se digitou sua busca corretamente ou tente usar outros filtros";
- Link-btn "Alterar filtros e buscar novamente" retorna o modal ao estado anterior, preservando todos os filtros previamente preenchidos.

### Filtros adicionais — busca por conteúdo e documentos importados

- **Checkbox "Buscar por conteúdo do documento"**: habilita busca textual dentro do corpo/arquivo do documento, seguindo os mesmos parâmetros técnicos já estabelecidos na [[Mesa de trabalho]]. Desmarcado por padrão, não obrigatório;
- **Checkbox "Buscar apenas por documentos importados"**: restringe resultados a documentos com flag de importação, respeitando os demais filtros ativos. Desmarcado por padrão, não obrigatório;
- **Fallback**: se nenhum dos dois checkboxes estiver marcado, a busca ocorre só nas informações básicas visíveis no card/listagem;
- **Pills de feedback visual** nos resultados: "Conteúdo do documento" (quando busca interna ativa) e "Documentos importados" (quando restrição de origem ativa) — mantidos mesmo em listagens com scroll infinito/paginação;
- **Regra adicionada em 25/03/2026**: quando o usuário chega a uma listagem por um fluxo onde a origem já foi definida (ex.: via modal marcando "Buscar somente por documentos importados"), o checkbox correspondente aparece marcado e **disabled**; nesse cenário, a filtragem por status também vem disabled, já que documentos importados só possuem o estado "Encerrado".

### Especificação de interface (referência rápida)

- Botão de acesso no header: estilo `ghost`, ícone de lupa, rótulo "Rastrear Documento";
- Modal: título "Rastrear documento", subtítulo "Busque por documentos emitidos em todos os setores do seu ambiente";
- Tooltip do toggle de código de rastreio: "Você pode encontrar o código de rastreio nos e-mails de criação e movimentações do documento. Ou ao acessá-lo, poderá encontrá-lo localizado ao lado da numeração oficial, no topo do documento";
- Tooltip do input-search padrão: "Encontre qualquer documento através de seu número, solicitante (CPF/CNPJ), nome do cidadão ou servidor envolvido, ou mesmo o título do documento";
- Card de resultado mostra: Título do Documento, Tipo do Documento, Numeração Oficial, Serviço ou Assunto, Setor(es) Atual(is), Status;
- Variante "Restrito/Sem Acesso" do card: cor cinza, ícone de cadeado, `cursor: default` (não clicável). Variante padrão (acessível): interativa, `cursor: pointer`.

### Possíveis variações (registrado no export, não confirmado como regra ativa)

- Documentos divulgados para a população poderiam ser acessados por servidores mesmo sem permissão de acesso aos documentos do setor.

## Comportamentos observados em teste
<!-- O que foi aprendido validando: comportamentos não documentados, pegadinhas, efeitos colaterais -->
- 

## Dúvidas em aberto
- [ ] O export não especifica o texto exato do informativo de erro para campos obrigatórios não preenchidos na busca padrão (`input-search`/"Tipo de documento") — só descreve que "retorna o informativo da obrigatoriedade" — confirmar redação exata com dev/produto;
- [ ] Não há, no export, uma definição fechada do que conta como "acesso restrito" para fins de exibição de card (ex.: se é só permissão de setor, ou se sigilo entra na mesma lógica visual) — comportamento descrito em trechos distintos (Fluxo B e Fluxo C) sem uma regra unificada explícita;
- [ ] Seção "Possíveis variações" (documentos divulgados à população) está registrada como variação possível, não como regra confirmada de implementação — validar se foi de fato implementada;
- [ ] Sem evidência de telas/prints no export (o link do Figma "Ambiente Servidor — Handoff" não foi trazido) — consultar Figma/Notion originais antes de qualquer teste manual;
- [ ] Sem passo a passo de reprodução ou ambiente definido no export — é documentação de especificação de produto, não uma task de teste; casos de teste ainda precisam ser derivados a partir das regras acima.

## Referências
<!-- Docs do repo (caminho), cards relacionados ([[SGV-XXXX]]), links externos, leis -->
- Notion original: https://app.notion.com/p/alfa-group/Rastrear-documento-2922aec67d30805fb768f15d4d1f8e12
- Figma referenciado no export (não copiado aqui): https://www.figma.com/design/BmFazoCXyqI9NQQeQESXJ6/Ambiente-Servidor---Handoff?node-id=397-76190
