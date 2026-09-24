---
prioridade: media
status: analise
tipo: melhoria
etapa_atual: "QA · Casos de teste"
modulo: "Tramitação — Encerramento de documento"
plano: ""
execucao: ""
ambiente: dev
origem: repo
projeto: ""
pai: ""
data_inicio: "2026-09-24"
data_fim: ""
responsavel: ""
pontos_alocados: ""
---

# SGV-9982 — Permanecer no documento após encerrar

**Ticket de origem:** SGV-11637 (card ATV-256) · **Protótipo:** Figma "Tramitação - Concepção" → seção SGV-11637 (dialogs)

> [!info]- Navegação QA/DEV  
> **Demanda:** [[01 - Demanda]]  
> **Plano de teste:** [[02 - Plano de teste]]  
> **Casos de teste:** [[03 - Casos de teste]]  
> **Validação:** [[04 - Validação dev]]  
> **Preparação Qase:** [[05 - Preparação Qase]]

> [!settings]- Controle da demanda  
> **Prioridade:** `INPUT[inlineSelect(option(baixa),option(media),option(alta)):prioridade]`  
> **Ambiente:** `INPUT[inlineSelect(option(dev),option(hml),option(prod)):ambiente]`  
> **Origem:** `INPUT[inlineSelect(option(repo),option(observado),option(conversa),option(validação)):origem]`

> [!info] Status atual  
> **Próximo passo:** decidir a pendência do RF11 (ver Pendências) e confirmar `projeto`/`pontos_alocados` antes de rotear para o DEV.

---

## Capacidade e esforço

> [!tip]- Capacidade do ciclo  
> **Capacidade alocada:** preencher `pontos_alocados`.
>
> ```dataviewjs  
> const id = "SGV-9982";  
> const paginas = dv.pages().where(p => p.file.path.includes(id) && typeof p.pontos === "number");  
> const lista = paginas.sort(p => p.file.name);  
> const necessario = lista.array().reduce((soma, pagina) => soma + Number(pagina.pontos), 0);  
> const alocado = Number(dv.current().pontos_alocados || 0);  
> const diferenca = alocado - necessario;  
> if (lista.length > 0) {  
>   dv.table(["Etapa/artefato", "Pontos"], lista.map(p => [p.file.link, p.pontos]));  
> } else {  
>   dv.paragraph("Nenhum artefato com pontos registrado ainda.");  
> }  
> dv.paragraph(`**Esforço necessário:** ${necessario} pontos · **Capacidade alocada:** ${alocado} pontos · **${diferenca >= 0 ? "Saldo" : "Déficit"}:** ${Math.abs(diferenca)} pontos`);  
> ```

---

## Problema / contexto

Hoje, ao confirmar qualquer um dos três tipos de encerramento de tramitação (documento inteiro, setor, participação própria), o usuário é sempre redirecionado para a mesa de trabalho. O CX recebeu pedidos de usuários que preferem continuar analisando o documento depois de encerrar. Uma mudança para "permanecer no documento" chegou a ser aprovada anteriormente, mas nunca subiu — o comportamento em produção sempre foi o redirecionamento.

Como os dois perfis existem (quem quer sair e quem quer ficar), a solução é dar a escolha ao usuário sem mexer no padrão de quem não quer decidir nada.

## Objetivo

Adicionar um checkbox opcional "Permanecer no documento após encerrar" nos três dialogs de confirmação de encerramento, permitindo que o usuário escolha permanecer no documento (recarregado no estado pós-encerramento) em vez de ir para a mesa de trabalho.

### Entrega desta capacidade

Os três dialogs de encerramento ganham o checkbox; a escolha é persistida por usuário e vale para os três tipos de encerramento. Comportamento padrão (sem marcar) permanece o atual.

---

## Decisões de produto

- A preferência é por **usuário**, não por setor, perfil ou organização — é única para os três tipos de encerramento.
- Os três dialogs passam a usar o `modal` com `Type=Alert` (ícone e borda superior em laranja).
- O CTA primário dos três dialogs é padronizado como "Encerrar"; o secundário como "Cancelar".
- A preferência só é gravada no momento da confirmação — marcar o checkbox e clicar em Cancelar não altera nada.
- Nenhuma regra de tramitação muda: permissão de quem pode encerrar, efeito de cada tipo de encerramento, regras de reabertura, status do documento, histórico e notificações continuam exatamente como hoje.

---

## Escopo

- Checkbox "Permanecer no documento após encerrar" nos três dialogs de encerramento (documento inteiro, setor, participação própria).
- Persistência da escolha do usuário, valendo para os próximos encerramentos.
- Os três dialogs no formato de alerta (`modal Type=Alert`).
- CTAs primários padronizados como "Encerrar".
- Recarregamento do documento no estado pós-encerramento quando o usuário permanece.

---

## Fora de escopo

- Regras de permissão de encerramento (quem pode encerrar o quê).
- Efeito de cada tipo de encerramento sobre setores, colaboradores e o documento.
- Regras de reabertura e de retomada pelo setor dono.
- Status do documento, histórico e notificações.
- Alterar o comportamento padrão para quem não marca o checkbox (continua indo para a mesa de trabalho).

---

## Critérios de aceite

- C1. O checkbox "Permanecer no documento após encerrar" é exibido nos três dialogs de encerramento, posicionado entre a pergunta de confirmação e a linha de botões. ^c1
- C2. O checkbox é exibido desmarcado quando o usuário não possui preferência gravada. ^c2
- C3. Confirmar o encerramento com o checkbox desmarcado redireciona o usuário para a mesa de trabalho (comportamento atual preservado). ^c3
- C4. Confirmar o encerramento com o checkbox marcado mantém o usuário no documento, recarregado no estado pós-encerramento, com as ações indisponíveis já refletidas. ^c4
- C5. A preferência só é gravada na confirmação do encerramento; Cancelar ou fechar o dialog não altera a preferência nem encerra a tramitação. ^c5
- C6. A preferência é única para os três tipos de encerramento — marcar em um tipo já reflete nos outros dois. ^c6
- C7. Na abertura seguinte de qualquer um dos três dialogs, o checkbox reflete o último valor salvo pelo usuário. ^c7
- C8. Desmarcar o checkbox e confirmar o encerramento reverte a preferência para "voltar para a mesa". ^c8
- C9. Os três dialogs usam o `modal` com `Type=Alert`, CTA primário "Encerrar", CTA secundário "Cancelar", com a copy exata definida no documento de origem. ^c9

> C9 é coberto por [[03 - Casos de teste#^ct-012|CT-012]].

---

## Checklist de entrega ao DEV

- [x] Decisões e regras de negócio estão fechadas.
- [x] Escopo e fora de escopo estão claros.
- [x] Critérios de aceite são objetivos e testáveis.
- [x] Plano e casos de teste estão vinculados.
- [ ] `pontos_alocados` foi preenchido.

---

## Pendências de decisão

- **RF11** (do documento de origem): "Ocultar o checkbox e ignorar a preferência quando o encerramento for disparado fora do documento (mesa de trabalho, listagem, ação em lote)" é condicional a uma "pendência 1" citada no material capturado, sem detalhamento explícito do que essa pendência envolve. Confirmar com quem levantou a demanda se esse cenário entra nesta entrega ou fica para um próximo ciclo. Enquanto não houver decisão, `status` permanece `analise` e nenhum CT foi criado para esse requisito.
- Confirmar `projeto`, `prioridade` e `pontos_alocados` antes de rotear a demanda para o DEV.
