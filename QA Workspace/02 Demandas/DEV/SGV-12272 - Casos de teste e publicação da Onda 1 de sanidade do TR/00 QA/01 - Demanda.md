---
prioridade: media
origem: "validação"
pontos_alocados: ""
---

# SGV-12272 — Casos de teste e publicação da Onda 1 de sanidade do TR

**Ticket de origem:** SGV-12272 (origem: Onda 1 aprovada na SGV-12200)

> [!info]- Navegação QA/DEV
> **README do card:** [[00 README|Abrir README do card]]
> **Demanda:** [[01 - Demanda]]
> **Plano de teste:** [[02 - Plano de teste]]
> **Casos de teste:** [[03 - Casos de teste]]
> **Validação:** [[04 - Validação dev]]
> **Preparação Qase:** [[05 - Preparação Qase]]
> **Origem (SGV-12200):** [[../../SGV-12200 - Levantamento da Onda 1 de cenários de sanidade/00 QA/01 - Proposta da Onda 1 (cenários candidatos e organização no Notion)|Proposta da Onda 1 (20 cenários aprovados)]]

> [!settings]- Controle da demanda
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

> [!info] Status atual
> **Próximo passo:** execução real dos 20 CTs em ambiente DEV pelo Rafael, com evidência e gate de doc (`04 - Validação dev.md`) — depois, sincronizar os CTs aprovados na Qase e publicar o catálogo funcional no Notion; nenhum dos dois foi iniciado ainda.

---

## Problema / contexto

A Onda 1 de 20 cenários candidatos de sanidade foi levantada e aprovada na SGV-12200 (19/10/2026), e os 20 CTs formais já foram redigidos (`03 - Casos de teste.md`) — mas a validação dev ainda não foi executada, nenhum caso foi sincronizado na Qase, e o catálogo funcional correspondente ainda não existe no Notion (a subpágina "Cenários de sanidade" do hub segue placeholder).

## Objetivo

Transformar os 20 cenários já aprovados em artefatos formais e reutilizáveis: CTs em Gherkin, sincronizados na Qase após validação, e um catálogo funcional publicado na subpágina "Cenários de sanidade" do hub Notion, com rastreabilidade direta ao Termo de Referência.

### Entrega desta capacidade

- 20 CTs formais em Gherkin, um por cenário aprovado, com rastreabilidade ao TR.
- Plano de teste mapeando os 20 CTs aos cenários de origem.
- Validação dev dos 20 CTs pelo fluxo existente.
- Preparação e sincronização dos CTs aprovados na Qase.
- Catálogo funcional publicado na subpágina "Cenários de sanidade" do hub Notion, sem metadados internos de QA nem links inacessíveis.

---

## Decisões de produto

- A seleção e o escopo dos 20 cenários já estão aprovados (SGV-12200, 19/10/2026) — não são reabertos nem redecididos aqui.

---

## Escopo

- Produzir os 20 CTs em Gherkin, reutilizáveis, a partir dos 20 cenários aprovados.
- Plano de teste com rastreabilidade ao TR para cada CT.
- Validação dev dos CTs pelo fluxo já existente no vault.
- Sincronizar os CTs aprovados na Qase, usando o mecanismo vigente (`Sistema/Scripts/qase-sync/`), só depois da validação.
- Publicar na subpágina "Cenários de sanidade" do hub Notion o catálogo funcional com os 20 cenários e referências diretas ao TR.

---

## Fora de escopo

- Implementação ou execução de automação.
- Decisão de arquitetura do preset/seed/.env (passo 11 da SGV-12082).
- Propor a Onda 2 de cenários.
- Alterar os documentos canônicos (Transcrição, Modelo-alvo, Matriz) já publicados.
- Reabrir ou redecidir a seleção dos 20 cenários já aprovada na SGV-12200.

---

## Critérios de aceite

Um critério por CT (C1–C20), cada um rastreável ao item exato do TR citado no cenário correspondente; critérios de processo da demanda em C21–C24.

- C1. Um Servidor Público com CPF e senha válidos autentica-se com sucesso e tem a sessão aberta no contexto de Servidor Público, não em outro contexto (Cidadão/Empresa). **TR:** 1.24 (regra geral de login por tipo de usuário), 1.24.1 (Servidor Público), 1.25 (validação de credenciais). Ver [[03 - Casos de teste#^ct-001|CT-001]] (ONDA1-01). ^c1
- C2. Após 5 tentativas de login malsucedidas, a conta do usuário é bloqueada. **TR:** 1.25.1. Ver [[03 - Casos de teste#^ct-002|CT-002]] (ONDA1-02). ^c2
- C3. Ao mudar o estado funcional do Servidor entre Ativo, Licença, Férias e o estado que o TR chama de Inativo, o sistema aplica o nível de restrição correspondente: em Licença (1.25.3.2), acesso restrito a funcionalidades não transacionais com modificação/aprovação suspensas; em Férias (1.25.3.3), a mesma política de quarentena com escrita/fluxos suspensos; em Inativo (1.25.3.4), negação explícita de qualquer tentativa de autenticação. **TR:** 1.25.3–1.25.3.4. Ver [[03 - Casos de teste#^ct-003|CT-003]] (ONDA1-03). ^c3
- C4. Um Servidor vinculado a mais de um Setor (TR 1.26.5) só consegue criar documento pelo Setor que tem permissão própria de criação (TR 1.26.11/1.26.11.1). O bloqueio pelo Setor sem essa permissão, testado no cenário, é regra de produto — não texto literal do TR (ver callout do CT). Ver [[03 - Casos de teste#^ct-004|CT-004]] (ONDA1-04). ^c4
- C5. Um Assunto/Serviço criado sob um Módulo herda a mesma categoria-base (Documento oficial, Comunicação oficial ou Processo administrativo) desse Módulo. **TR:** 1.28.1 (campos mínimos do serviço/assunto), 1.29.1 (3 categorias-base). Ver [[03 - Casos de teste#^ct-005|CT-005]] (ONDA1-05). ^c5
- C6. Assuntos/Serviços seguem os mesmos padrões de regras de tramitação definidos por Módulo. **TR:** 1.29 (categorias de documentos respeitam regras de tramitação definidas por módulo, seguindo os mesmos padrões usados em Assuntos e Serviços). O comportamento específico testado — um Setor removido de "Setores que recebem e tramitam" de um Assunto/Serviço deixa de receber documentos ali, sem afetar os demais Assuntos/Serviços do Módulo — é regra de produto, não texto literal do TR (ver callout do CT). Ver [[03 - Casos de teste#^ct-006|CT-006]] (ONDA1-06). ^c6
- C7. Um Cidadão/Empresa consulta, na central de atendimento, uma Zona publicada e as Categorias de uso associadas a ela. **TR:** 1.29.10.2 ("a ferramenta deve ser acessível tanto para servidores quanto para cidadãos e empresas"), 1.29.10.4.g ("quando publicado, cidadãos e empresas poderão consultar as zonas e categorias de uso diretamente na central"). Ver [[03 - Casos de teste#^ct-007|CT-007]] (ONDA1-07). ^c7
- C8. Um Cidadão/Empresa inicia um Processo urbanístico a partir de uma Zona publicada, e um Servidor com permissão revisa o Anexo desse processo, podendo aprovar/reprovar, destacar áreas e comentar. **TR:** 1.29.10.4.g (abrir processo a partir da Zona), 1.29.10.4.h ("o usuário poderá... iniciar um processo urbanístico diretamente relacionado à zona selecionada"), 1.29.10.4.i–j (anexos revisados por servidores, com aprovação/reprovação, destaque de áreas e comentários). Ver [[03 - Casos de teste#^ct-008|CT-008]] (ONDA1-08). ^c8
- C9. Um documento criado a partir de um Modelo simples com herança de dados preenche automaticamente os campos vinculados com os dados do formulário; um Modelo sem herança mantém o conteúdo estático. **TR:** 1.31.1 (modelos simples integrados ao editor de despachos), 1.31.1.1.b (definição de herança), 1.31.1.1.b.i ("o sistema preencherá esses espaços automaticamente com os dados que foram preenchidos no formulário inicial"), 1.31.1.1.b.ii ("o conteúdo desse modelo é totalmente estático"). Ver [[03 - Casos de teste#^ct-009|CT-009]] (ONDA1-09). ^c9
- C10. Uma Etapa de Fluxo configurada com despacho customizado e assinatura obrigatória bloqueia o avanço do documento até que ambos sejam concluídos. **TR:** 1.30.1.d/e (despachos e assinaturas obrigatórias configuráveis por Etapa), 1.30.2.b ("o sistema deverá permitir a inserção de solicitações de assinatura obrigatória como parte do despacho, garantindo que a tramitação só avance para uma nova etapa após a assinatura"). Ver [[03 - Casos de teste#^ct-010|CT-010]] (ONDA1-10). ^c10
- C11. Ao acessar a Mesa de trabalho, o Servidor vê o resumo de demandas (em aberto, em tramitação, concluído, assinaturas pendentes, prestes a vencer/vencidas) e consegue alternar entre os Setores aos quais está vinculado. **TR:** 1.33.1 ("deverá permitir que os usuários alternem entre diferentes setores de forma ágil, visualizando e gerenciando documentos e processos pertencentes a cada setor"), 1.33.2/1.33.2.1 ("resumo de todas as demandas" com as quantidades em: a) Em aberto, b) Em tramitação, c) Concluído, d) Assinaturas pendentes, e) Demandas prestes a vencer e/ou já vencidas). Ver [[03 - Casos de teste#^ct-011|CT-011]] (ONDA1-11). ^c11
- C12. Uma Etiqueta pessoal fica visível só para quem a criou; uma Etiqueta compartilhada fica visível para os Setores com quem foi compartilhada. **TR:** 1.34.1.a ("Etiquetas pessoais: criadas exclusivamente para o uso individual do servidor... visíveis apenas na mesa pessoal dele"), 1.34.1.b ("Etiquetas compartilhadas: criadas e compartilhadas entre setores ou hierarquias de setores, permitindo que mais servidores acessem essas etiquetas"). Ver [[03 - Casos de teste#^ct-012|CT-012]] (ONDA1-12). ^c12
- C13. Um novo Contato externo (Cidadão PF ou Empresa PJ) recebe e-mail de confirmação ao concluir o cadastro. **TR:** 1.32 ("área para cadastro e gerenciamento de contatos externos, sejam cidadãos (pessoa física) ou empresas (pessoas jurídicas)... cadastro único na plataforma"), 1.32.1 ("ao serem cadastrados... os respectivos novos contatos devem receber um email para confirmação do cadastro"). Ver [[03 - Casos de teste#^ct-013|CT-013]] (ONDA1-13). ^c13
- C14. Cidadãos, Empresas e Entes externos acessam, pela Central de atendimento, um Serviço oferecido pelo órgão através dos canais digitais. **TR:** 1.36 ("deve ser disponibilizado uma central de atendimento para que os cidadãos, empresas e entes externos possam ter acesso, através dos canais digitais do órgão, para realizar as suas solicitações e ter acesso aos serviços oferecidos pela entidade"). Ver [[03 - Casos de teste#^ct-014|CT-014]] (ONDA1-14). ^c14
- C15. Um Usuário externo abre uma Demanda e consegue acompanhá-la (notificações, andamento) no seu ambiente virtual próprio. **TR:** 1.37 ("cada usuário externo deverá ter acesso a um ambiente virtual próprio, onde poderá receber notificações e acompanhar o andamento das demandas que abriu ou solicitou... assim como, abrir novas demandas"). Ver [[03 - Casos de teste#^ct-015|CT-015]] (ONDA1-15). ^c15
- C16. Um Documento divulgado aparece no mural interno do Servidor e, quando configurado para canal externo, fica acessível publicamente no Jornal Oficial, sem necessidade de login, localizável via busca/filtros. **TR:** 1.38.1.a ("documentos e/ou comunicações oficiais sejam divulgados no mural interno, visível a todos os servidores cadastrados"), 1.38.1.b.i ("acessível por qualquer pessoa com acesso à internet, sem a necessidade de login"), 1.38.3.1 ("cidadãos possam acessar os documentos divulgados no jornal oficial por meio de uma interface pública, com funcionalidades de busca e filtros"). Ver [[03 - Casos de teste#^ct-016|CT-016]] (ONDA1-16). ^c16
- C17. Numa solicitação de assinatura sequencial com signatários internos e externos, a ordem definida é respeitada: um signatário fora da sua vez não consegue assinar antes do signatário da vez. **TR:** 1.40.3.b ("a ordem de assinaturas do documento, pelos signatários, deve ser seguida conforme foi definido na configuração. De modo que, enquanto o signatário da vez não assinar, os demais devem ficar impossibilitados de assinar"), 1.40.3.c (seleção de signatários internos e externos). Ver [[03 - Casos de teste#^ct-017|CT-017]] (ONDA1-17). ^c17
- C18. Um Servidor convenente usa uma Chave de acesso concedida por um Servidor concedente para criar um Documento dentro do limite de uso definido, e o concedente é notificado. **TR:** 1.41.1.b.ii (limite de uso da chave), 1.41.2.a (uso de chave concedida por outro servidor ao criar documento), 1.41.2.d ("sempre que um documento for gerado utilizando uma chave de acesso, o servidor que criou a chave receberá uma notificação, podendo visualizar e acompanhar o documento gerado"). Ver [[03 - Casos de teste#^ct-018|CT-018]] (ONDA1-18). ^c18
- C19. É possível editar as cores temáticas do menu principal e fazer upload/gerenciamento de imagens institucionais do órgão; um Servidor com nível diferente de Administrador é barrado ao tentar a mesma ação. **TR:** 1.42.1.b ("possibilidade de editar as cores temáticas da interface do menu principal do sistema"), 1.42.1.c ("upload e gerenciamento das imagens institucionais do órgão que serão exibidas em todo o sistema"). A exigência de nível Administrador — inclusive o bloqueio de outros níveis — é regra de produto, não texto literal do TR (ver callout do CT). Ver [[03 - Casos de teste#^ct-019|CT-019]] (ONDA1-19). ^c19
- C20. O painel de Estatísticas exibe, para os servidores cadastrados, o total de ativos/inativos e os agrupamentos por status e por nível de permissão. **TR:** 1.43.5.a ("total de servidores: ativos e inativos"), 1.43.5.b ("servidores por status: quantidade de servidores categorizados por status"), 1.43.5.c ("servidores por nível de permissão: exibição por níveis"). Ver [[03 - Casos de teste#^ct-020|CT-020]] (ONDA1-20). ^c20
- C21. O plano de teste cobre os 20 CTs com rastreabilidade TR registrada. ^c21
- C22. Os 20 CTs passaram pelo fluxo de validação dev existente. ^c22
- C23. Os CTs aprovados estão sincronizados na Qase pelo mecanismo vigente. ^c23
- C24. O catálogo funcional dos 20 cenários está publicado na subpágina "Cenários de sanidade", sem metadados internos de QA nem links inacessíveis. ^c24

---

## Checklist de entrega ao DEV

- [ ] Decisões e regras de negócio estão fechadas.
- [ ] Escopo e fora de escopo estão claros.
- [ ] Critérios de aceite são objetivos e testáveis.
- [ ] Plano e casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- Suite Qase ainda não confirmada — não assumir/criar suite sem autorização explícita (ver `Sistema/Skills/SKILL_SYNC_QASE.md`, GATE 2).
