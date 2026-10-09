---
tags: [qa]
task: "SGV-12082"
pai: "SGV-11262"
tipo: "modelo"
status: planejado
---
# Mapa geral — Modelo do preset (SGV-12082)

> [!info]- Navegação QA
> **README do card:** [[../00 QA/00 README|Abrir README do card]]
> **Demanda:** [[../00 QA/01 - Demanda]]
> **Plano de análise:** [[../00 QA/02 - Plano de análise]]
> **Matriz de atores e relações:** [[01 - Matriz de atores e relações]]
> **Revisão da análise:** [[../00 QA/04 - Revisão da análise]]

> [!info] Síntese derivada das 11 notas de recorte aprovadas (revisão de cobertura em 09/10/2026)
> Este mapa é um **resumo visual de alto nível**, derivado das 11 notas temáticas em `Seções do TR/` (ver [[01 - Matriz de atores e relações|Matriz de atores e relações]]), todas já revisadas e aprovadas pelo Codex. Ele **não substitui** essas notas nem o PDF ([[../Fontes/Termo de Referência SOGOV.pdf|Termo de Referência SOGOV.pdf]]) — ambos continuam sendo a fonte da verdade; este diagrama é só uma visão consolidada, agrupada por tema (não por recorte), para orientar a evolução do modelo do preset. As relações mostradas já estão documentadas nas notas de origem; nenhuma lacuna foi resolvida ou inferida aqui.

## Diagramas — leitura vertical por tema

Os diagramas menores seguem a hierarquia de cima para baixo. A sequência entre diagramas organiza a leitura, sem indicar dependência; relações entre temas ficam na tabela seguinte.

### 1. Órgão e níveis de acesso

```mermaid
flowchart TB
    Orgao["Órgão"] --> Setor["Setor / Subsetor"]
    Setor --> Servidor["Servidor"]
    Servidor --> NivelTR["Nível por setor (rótulos originais do TR)"]
    NivelTR --> NivelRafael["Administrador · Administrador Setorial · Especialista · Usuário básico · Somente leitura"]
```

### 2. Status funcional do servidor

```mermaid
flowchart TB
    StatusTR["Listas do TR:<br/>1.25.3: Ativo / Licença / Férias / Inativo (nega autenticação)<br/>1.27.10.1: Inativo (offline) e Suspenso<br/>1.27.11.2: Em atividade / Suspenso / Licença / Férias"] --> Interpretacao["Interpretação de trabalho de Rafael:<br/>Ativo abrange Em atividade, Licença e Férias;<br/>Inativo = Suspenso.<br/>A redação de 1.27.10.1 diverge."]
```

### 3. Presença e bloqueio de acesso

```mermaid
flowchart TB
    Servidor["Servidor"] --> Presenca["Presença Online / Offline"]
    Servidor --> Bloqueio["Bloqueio após 5 tentativas malsucedidas"]
```

### 4. Serviços, assuntos e categorias de documento

```mermaid
flowchart TB
    ServicoAssunto["Serviço / Assunto"] --> Configuracao["Cadastro e regras de atendimento/tramitação"]
    Configuracao --> CategoriaDoc["Categoria de documento"]
    CategoriaDoc --> Subtipo["Tipos específicos: Memorando, Ofício, Ouvidoria, e-SIC…"]
    Configuracao --> Campos["Campos personalizados"]
```

### 5. Zoneamento e categorias de Assuntos e Serviços

```mermaid
flowchart TB
    Zoneamento["Processo urbanístico / Zoneamento"] -.->|"(b) categoria-base?"| CategoriaDoc["Categoria de documento"]
    CategoriaAS["Categoria de Assuntos e Serviços"] -.->|"(n) relação inferida"| SubcategoriaAS["Subcategoria de Assuntos e Serviços"]
```

### 6. Modelos de documentos

```mermaid
flowchart TB
    ModeloSimples["Modelo simples"] --> Vinculo["Vínculo obrigatório com Categoria, Serviço ou Assunto"]
    DocumentoAuto["Documento automatizado"] --> Vinculo
    ModeloSimples --> UsoSimples["Texto inserido durante a tramitação"]
    DocumentoAuto --> Geracao["Gera documento independente com tramitação própria"]
```

### 7. Mesa, fluxo de trabalho e despachos

```mermaid
flowchart TB
    Documento["Documento / Processo"] --> Mesa["Mesa de trabalho"]
    Fluxo["Fluxo de trabalho"] --> Etapa["Etapa"]
    Etapa --> DespachoEtapa["Despacho na etapa (1.30.2)"]
    Documento --> DespachoTramitacao["Despacho na tramitação (1.35.2.2.1)"]
    DespachoEtapa -.->|"(e) mesma funcionalidade?"| DespachoTramitacao
    Mesa -.->|"(c) reflete etapas do fluxo?"| Etapa
```

### 8. Status e documentos associados

```mermaid
flowchart TB
    Documento["Documento / Processo"] --> Etiqueta["Etiqueta"]
    Etiqueta -.->|"(d) alcance da regra por setor?"| RegraEtiqueta["Regra de visibilidade"]
    Documento --> Apensado["Documento apensado via despacho"]
    Documento --> Associado["Documento associado automaticamente"]
    Apensado -.->|"(f) mesmo mecanismo?"| Associado
    StatusResumo["Resumo inicial: Concluído (1.33.2.1)"] -.->|"(p) equivalência ou agregado?"| StatusFormal["Enum formal: Encerrado (1.33.3.6 / 1.35.2.1)"]
```

### 9. Atores externos e atendimento

```mermaid
flowchart TB
    Contato["Contato externo: cidadão / empresa"] -.->|"(a) mesma identidade?"| UsuarioExterno["Usuário externo"]
    UsuarioExterno --> Demanda["Demanda externa"]
    Central["Central de atendimento"] --> Atores["Cidadãos, empresas e entes externos"]
    Atores --> Solicitacao["Solicitações e acesso a serviços"]
```

### 10. Divulgação, assinatura e exportação

```mermaid
flowchart TB
    Divulgacao["Divulgação"] --> Mural["Mural interno"]
    Divulgacao --> Canal["Canal Oficial"]
    Canal -.->|"(g) mesmo elemento?"| Jornal["Jornal Oficial"]
    Assinatura["Assinatura"] --> Signatario["Signatário interno / externo"]
    Exportacao["Exportação / impressão"]
```

### 11. Chaves de acesso

```mermaid
flowchart TB
    Chave["Chave de acesso"] --> Historico["Histórico de documentos gerados"]
    Historico -.->|"(l) mesmo registro?"| Registro["Registro de uso"]
    Chave --> Filtros["Filtros: Ativas / Encerradas / Agendadas"]
    Chave -.->|"(i) estados formais ou filtros?"| Filtros
    Chave -.->|"(m) fluxo sem chave?"| FluxoProprio["Criação com permissão própria"]
```

### 12. Personalização e estatísticas

```mermaid
flowchart TB
    Orgao["Órgão"] --> Personalizacao["Personalização"]
    Personalizacao --> IdentidadeVisual["Cores e imagens institucionais"]
    Personalizacao --> DadosOrgao["Licenças, contrato e módulos contratados"]
    DadosOrgao -.->|"(k) leitura ou edição?"| ModoAcesso["Modo de acesso não especificado"]
    Estatisticas["Estatísticas"] --> Relatorios["Setores / Módulos / Servidores / Consumo"]
    Relatorios --> StatusServidor["Status de servidor: Ativo, Inativo, Licença, Férias (1.43.5.b)"]
```

## Relações entre grupos

As relações abaixo cruzam os grupos temáticos do diagrama e, por isso, ficam fora da área gráfica para manter a leitura vertical. Continuam sustentadas pelos recortes do TR; dúvidas permanecem identificadas como tal.

| Origem | Relação | Destino | Evidência/estado | Recorte |
|---|---|---|---|---|
| Serviço / Assunto | vinculado a | Categoria de documento | Confirmado | [[Seções do TR/04 - Serviços, assuntos e categorias de documentos (1.28–1.29)]] |
| Modelo simples / Documento automatizado | vinculado a | Categoria, Serviço ou Assunto | Confirmado | [[Seções do TR/05 - Fluxos de trabalho e modelos de documentos (1.30–1.31)]] |
| Modelo simples | é inserido durante a tramitação de | Documento/Processo | Confirmado | [[Seções do TR/05 - Fluxos de trabalho e modelos de documentos (1.30–1.31)]] |
| Documento automatizado | gera documento independente com tramitação própria | Documento/Processo | Confirmado | [[Seções do TR/05 - Fluxos de trabalho e modelos de documentos (1.30–1.31)]] |
| Central de atendimento | oferece acesso aos | Serviços do órgão | Propósito confirmado; vínculo exato com a entidade Serviço não detalhado pelo TR | [[Seções do TR/06 - Atores externos e atendimento ao cidadão (1.32, 1.36–1.37)]] |
| Canal Oficial | está disponível na | Central de atendimento | Confirmado pelo texto do TR | [[Seções do TR/06 - Atores externos e atendimento ao cidadão (1.32, 1.36–1.37)]], [[Seções do TR/08 - Divulgação, exportação e assinaturas (1.38–1.40)]] |
| Signatário externo / contribuinte | pode corresponder a | Contato externo / Usuário externo | A confirmar para “contribuinte” | [[Seções do TR/06 - Atores externos e atendimento ao cidadão (1.32, 1.36–1.37)]], [[Seções do TR/08 - Divulgação, exportação e assinaturas (1.38–1.40)]] |
| Assinatura | é aplicada a | Documento/Processo | Confirmado | [[Seções do TR/08 - Divulgação, exportação e assinaturas (1.38–1.40)]] |
| Documento/Processo | pode ser divulgado em | Mural interno / Canal Oficial | Confirmado | [[Seções do TR/08 - Divulgação, exportação e assinaturas (1.38–1.40)]] |
| Documento/Processo | pode ser exportado como | PDF / árvore do processo | Confirmado | [[Seções do TR/08 - Divulgação, exportação e assinaturas (1.38–1.40)]] |
| Chave de acesso | é criada/concedida por (concedente) e vinculada a (convenente) | Servidor | Confirmado | [[Seções do TR/09 - Chaves de acesso e criação delegada (1.41)]] |
| Órgão | possui | Personalização | Confirmado | [[Seções do TR/10 - Personalização e identidade visual do órgão (1.42)]] |
| Estatísticas | exibem dados de | Servidores e Documentos/Processos | Confirmado | [[Seções do TR/11 - Estatísticas e indicadores (1.43)]] |
| Acesso à personalização/estatísticas | é concedido a | Níveis de usuário | Parcialmente especificado; ver lacuna (j) | [[Seções do TR/10 - Personalização e identidade visual do órgão (1.42)]], [[Seções do TR/11 - Estatísticas e indicadores (1.43)]] |
| Status estatístico de servidor | agrupa | Ativo, Inativo, Licença, Férias | Possível sobreposição em aberto; ver lacuna (o) | [[Seções do TR/03 - Estrutura organizacional e cadastro de servidores (1.26–1.27)]], [[Seções do TR/11 - Estatísticas e indicadores (1.43)]] |

## Legenda

- **Linha sólida (→):** relação confirmada — requisito explícito do TR, ou contexto de negócio **já confirmado diretamente por Rafael** (quando liga a um nó azul).
- **Linha tracejada (-.→), com código (a)–(p):** o **texto literal do TR não declara** essa relação — é uma lacuna do próprio TR, por isso a aresta permanece tracejada independentemente do que a documentação de produto diga. Algumas dessas lacunas já têm **contexto de produto documentado** (Conhecimento > Módulos) que esclarece a questão para o produto atual, sem alterar o que o TR declara ou deixa de declarar — ver a coluna "Estado no produto" na tabela abaixo e a subseção "Contexto de produto verificado em documentação" no recorte-fonte, quando existir.
- **Nó azul (classe "Rafael"):** contexto de negócio confirmado diretamente por Rafael (ex.: mapeamento de níveis canônicos, status do servidor, regra de criação de Assuntos e Serviços) — **não é texto literal do TR**. Nó branco/padrão = conceito descrito no próprio texto do TR.

### Lacunas registradas (arestas tracejadas)

> A coluna "Estado no produto" reflete o que a documentação de Conhecimento > Módulos esclarece hoje (09/10/2026) — não resolve nem reescreve a lacuna do TR em si, que segue registrada como aresta tracejada. Detalhe completo de cada achado está na subseção "Contexto de produto verificado em documentação" do recorte-fonte.

| Código | Lacuna do TR | Estado no produto | Recorte-fonte |
|---|---|---|---|
| (a) | Contato externo (1.32) × Usuário externo (1.37) — mesma identidade? | Esclarecido no produto — mesma entidade (Usuário Cidadão) | [[Seções do TR/06 - Atores externos e atendimento ao cidadão (1.32, 1.36–1.37)]] |
| (b) | Zoneamento (1.29.10) — categoria-base entre as 3 de 1.29.1? | Sem evidência — aguarda Rafael | [[Seções do TR/04 - Serviços, assuntos e categorias de documentos (1.28–1.29)]] |
| (c) | Mesa de trabalho × Etapa/Fluxo de trabalho — reflete etapas de um fluxo configurado? | Esclarecido no produto — mesa pode conter documentos fora do modelo de Fluxo de trabalho | [[Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)]] |
| (d) | Alcance da regra de visibilidade de etiquetas por setor — também vale para etiquetas pessoais? | Esclarecido no produto — restrição por setor só vale para compartilhadas | [[Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)]] |
| (e) | Despacho (1.30.2, Etapa) × Despacho (1.35.2.2.1, tramitação) — mesmo conceito de negócio? | Parcialmente esclarecido — mesma família/modelo funcional; identidade estrutural não confirmada | [[Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)]] |
| (f) | Documento apensado via despacho × documento associado automaticamente — mesmo mecanismo/objeto? | Parcialmente esclarecido — convergem no mesmo conceito/regra de visibilidade de documento associado, mas os gatilhos diferem (manual via despacho; automático via Gerar Documento) e a estrutura de dados persistida não está documentada | [[Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)]] |
| (g) | Canal Oficial (1.38.1.b) × Jornal Oficial (1.38.3.1) — mesmo elemento? | Sem evidência — aguarda Rafael | [[Seções do TR/08 - Divulgação, exportação e assinaturas (1.38–1.40)]] |
| (h) | Signatário externo / "contribuinte" (1.40) × Contato externo (1.32) e Usuário externo (1.37) do recorte 06 — mesma população, sem afirmar identidade | Confirmado no produto quanto a Contato/Usuário externo; "contribuinte" segue sem evidência | [[Seções do TR/08 - Divulgação, exportação e assinaturas (1.38–1.40)]] |
| (i) | Filtros de listagem da chave (Ativas/Encerradas/Agendadas) — estados formais da entidade, ou só opções de filtro? | Sem evidência — aguarda Rafael | [[Seções do TR/09 - Chaves de acesso e criação delegada (1.41)]] |
| (j) | Quais níveis acessam a área de personalização e a funcionalidade de estatísticas? | Parcialmente esclarecido — identidade visual (1.42.1.b/c) = Administrador, confirmado no produto; dados cadastrais (1.42.1.a) e estatísticas (1.43) seguem sem evidência | [[Seções do TR/10 - Personalização e identidade visual do órgão (1.42)]], [[Seções do TR/11 - Estatísticas e indicadores (1.43)]] |
| (k) | Acesso aos dados cadastrais do órgão — só leitura, ou também edição? | Sem evidência — aguarda Rafael | [[Seções do TR/10 - Personalização e identidade visual do órgão (1.42)]] |
| (l) | Histórico de documentos da chave × registro de uso da chave — mesmo registro? | Sem evidência — aguarda Rafael | [[Seções do TR/09 - Chaves de acesso e criação delegada (1.41)]] |
| (m) | Fluxo de criação de documento quando há só permissão própria (sem chave) — não especificado pelo TR | Sem evidência — aguarda Rafael | [[Seções do TR/09 - Chaves de acesso e criação delegada (1.41)]] |
| (n) | Relação hierárquica entre Categoria e Subcategoria de Assuntos e Serviços é inferida pelo nome no TR (1.27.8.2.o); estrutura exata não descrita | Sem evidência — aguarda Rafael | [[Seções do TR/04 - Serviços, assuntos e categorias de documentos (1.28–1.29)]] |
| (o) | Relatório de servidores (1.43.5.b): licença/férias são contadas também em “ativos” segundo a interpretação de trabalho confirmada por Rafael; o TR não define se as categorias estatísticas se sobrepõem | Sem decisão — aguarda Rafael | [[Seções do TR/11 - Estatísticas e indicadores (1.43)]] |
| (p) | Resumo inicial “Concluído” (1.33.2.1) × enum formal “Encerrado” (1.33.3.6/1.35.2.1): equivalência ou agregação não especificada | Sem evidência — aguarda Rafael | [[Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)]] |

## Rastreabilidade por grupo

| Grupo no diagrama | Recortes-fonte |
|---|---|
| Órgão, setores, servidores e níveis | [[Seções do TR/02 - Autenticação e ciclo de vida da identidade (1.24–1.25)]], [[Seções do TR/03 - Estrutura organizacional e cadastro de servidores (1.26–1.27)]] |
| Assuntos, serviços, documentos e modelos | [[Seções do TR/04 - Serviços, assuntos e categorias de documentos (1.28–1.29)]], [[Seções do TR/05 - Fluxos de trabalho e modelos de documentos (1.30–1.31)]] (item 1.31) |
| Documento/processo, mesa, status, prazos, etiquetas, tramitação | [[Seções do TR/05 - Fluxos de trabalho e modelos de documentos (1.30–1.31)]] (item 1.30), [[Seções do TR/07 - Mesa de trabalho, etiquetas e tramitação (1.33–1.35)]] |
| Usuário externo e atendimento | [[Seções do TR/06 - Atores externos e atendimento ao cidadão (1.32, 1.36–1.37)]] |
| Assinatura, publicação e exportação | [[Seções do TR/08 - Divulgação, exportação e assinaturas (1.38–1.40)]] |
| Chave de acesso | [[Seções do TR/09 - Chaves de acesso e criação delegada (1.41)]] |
| Personalização e estatísticas | [[Seções do TR/10 - Personalização e identidade visual do órgão (1.42)]], [[Seções do TR/11 - Estatísticas e indicadores (1.43)]] |
| (infraestrutura técnica — sem elementos de negócio no diagrama) | [[Seções do TR/01 - Infraestrutura técnica e operacional (1.1–1.23)]] |

## Notas

- Este mapa é só uma síntese visual de alto nível; cobertura item a item, evidência (Confirmado/Inferido/A confirmar) e o texto completo de cada dúvida estão nas notas de recorte listadas acima — não duplicados aqui.
- Em 09/10/2026, uma rodada read-only verificou as dúvidas abertas contra a documentação de Conhecimento > Módulos vigente; os recortes 06, 07, 08 e 10 agora trazem, cada um, uma subseção "Contexto de produto verificado em documentação" com o que foi esclarecido, parcialmente esclarecido, ou segue sem evidência — sem alterar o texto literal do TR nem a classificação de cobertura.
- As lacunas (a), (c) e (d) têm contexto de produto que as esclarece para o produto atual e não exigem mais decisão de Rafael; (e), (f) e (j) seguem parcialmente esclarecidas — (f) converge no conceito/regra de visibilidade de documento associado, mas gatilhos diferentes e estrutura de dados persistida não documentada (detalhe técnico, não pendência de decisão de Rafael). As lacunas (b), (g), (h quanto a "contribuinte"), (i), (k), (l), (m), (n), (o) e (p) seguem sem decisão/evidência suficiente — a pergunta sobre a categoria-base do Zoneamento (b) continua sendo a primeira pendente na sequência de esclarecimentos.
- **Conflito textual de status de servidor:** o TR 1.27.10.1 define “Inativo” como offline e lista “Suspenso” à parte, enquanto 1.25.3.4 usa “Inativo” para negar autenticação. O mapa mantém as duas redações e identifica a leitura de trabalho confirmada por Rafael; não as trata como equivalência literal do TR. Ver [[Seções do TR/03 - Estrutura organizacional e cadastro de servidores (1.26–1.27)]].
