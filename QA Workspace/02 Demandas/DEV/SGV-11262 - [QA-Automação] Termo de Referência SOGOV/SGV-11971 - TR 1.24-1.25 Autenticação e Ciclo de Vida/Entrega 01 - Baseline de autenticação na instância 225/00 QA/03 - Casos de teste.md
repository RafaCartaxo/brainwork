---
demanda: "[[01 - Demanda]]"
plano: "[[02 - Plano de teste]]"
validacao: "[[04 - Validação dev]]"
status: planejado
pontos: ""
---

# Casos de teste — Entrega 01

> [!info]- Navegação QA
> **README:** [[00 README]]
> **Demanda:** [[01 - Demanda]]
> **Plano:** [[02 - Plano de teste]]
> **Validação:** [[04 - Validação dev]]
> **Automação funcional:** [[../01 Automação/02 - Validação automação]]

> Estes quatro casos verificam o comportamento de seleção e preparação do seed. Os CT-001–012 e CT-038 continuam definidos somente na [[../../00 QA/03 - Casos de teste|SGV-11971]]; esta nota não os copia nem renumera.

## Matriz de cobertura

| Critério | Casos |
|---|---|
| [[01 - Demanda#^c1|C1]] | [[#^ct-seed-001|SEED-001]] |
| [[01 - Demanda#^c2|C2]] | [[#^ct-seed-002|SEED-002]] |
| [[01 - Demanda#^c3|C3]] | [[#^ct-seed-003|SEED-003]] |
| [[01 - Demanda#^c4|C4]] | [[#^ct-seed-004|SEED-004]] |
| [[01 - Demanda#^c5|C5]] | CT-001–012 e CT-038 da SGV-11971, registrados em [[../01 Automação/02 - Validação automação]] |

---

## SEED-001 · Usa a instância configurada pelo ID

**Descrição:** conferir que o ID explícito resolve para a instância esperada antes da preparação.

**Pré-condições:**
- Ambiente configurado é o backend onde a instância 225 foi criada.
- A instância 225 está acessível à conta administrativa do seed.

**Dado** ID de alvo 225 e nome esperado “Termo De Referência - Sogov”
**Quando** o seed resolve a instância
**Então** obtém o registro de ID 225 e valida o nome antes de provisionar recursos.

**Resultado esperado:** manifesto registra ID 225 e nome confirmado; nenhuma outra instância é criada.

^ct-seed-001

---

## SEED-002 · Recusa alvo ausente ou divergente

**Descrição:** garantir que alvo explícito inválido não resulte em criação ou preparação noutro cliente.

**Pré-condições:** teste controlado do seletor com ID inexistente ou nome divergente; não usar alvo de produção.

**Dado** um ID explícito que não existe ou retorna nome inesperado
**Quando** o seed tenta resolver o alvo
**Então** encerra antes das chamadas de provisionamento e não usa o caminho de criação por nome.

**Resultado esperado:** falha clara; nenhuma entidade criada ou alterada.

^ct-seed-002

---

## SEED-003 · Mantém o padrão sem ID explícito

**Descrição:** proteger as execuções atuais que não selecionam uma instância dedicada.

**Pré-condições:** rodar o teste isolado do seletor; não apontar a suíte existente à instância 225.

**Dado** que PW_INSTANCE_ID não está definido
**Quando** o seed resolve seu alvo
**Então** segue o comportamento legado baseado no perfil E2E Automatic Test.

**Resultado esperado:** o alvo padrão e sua impressão digital permanecem compatíveis com as execuções atuais.

^ct-seed-003

---

## SEED-004 · Reexecução idempotente e manifesto coerente

**Descrição:** verificar a mesma instância e os mesmos dados-base após duas execuções.

**Pré-condições:** ID 225 validado; configuração do ambiente confirmada; permissões administrativas disponíveis.

**Dado** o seed executado uma primeira vez na instância 225
**Quando** for executado novamente no mesmo ambiente e configuração
**Então** reutiliza o ID 225 e reconcilia as entidades sem criar uma segunda instância nem duplicar atores-chave.

**Resultado esperado:** ambos os manifestos registram ID 225; a segunda execução conclui sem duplicações.

^ct-seed-004

