---
tags:
  - qa
  - evidencias
---
# Evidências

Guia único de como gravar, organizar e referenciar evidências de validação.

> [!warning] Não deixar vídeo cru pra trás
> Gravação sem renomear/mover na raiz de `Evidências/` é o primeiro sinal de fluxo quebrado — resolver no mesmo dia, antes de fechar a daily.

## Processo completo (fluxo 5)

### 1. Gravar
Gravar com o OBS — já salva direto na raiz de `Evidências/`.

### 2. Renomear
Renomear pro padrão: `<número do card> - <breve descrição>.mp4`

Ex.: `9971 - solicitar assinatura para servidor com cadastro incompleto.mp4`

#### Evidência de caso de teste

Quando a gravação é a execução de um **CT específico** (típico de melhoria/funcionalidade, onde se roda caso por caso), o padrão ganha o CT no meio:

`<número do card> - CT-<NNN> - <breve descrição>.mp4`

Uma gravação que cobre **mais de um CT** lista todos, separados por vírgula:

`9042 - CT-001, CT-005, CT-007 - conteiner exibido, assinatura pendente bloqueia e select habilita.mp4`

Ela é **embedada em cada CT** que cobre, com a nota `*Mesma gravação cobre CT-005, CT-007.*` — um arquivo só no disco, referenciado de vários lugares. Diferente do compartilhamento entre **cards**, que exige cópia (seção abaixo).

> [!warning] O número do card vem primeiro, sempre
> Gravar como `001.mp4` ou `004, 006.mp4` **não funciona**: o roteador do 🔄 procura o número do **card** no começo do nome. `002.mp4` seria lido como SGV-002 e `004, 006.mp4` não casa com padrão nenhum — os dois ficam parados na raiz. Precedente: 30/07, 11 arquivos renomeados à mão na SGV-9042.

> [!important] Renumerar CT e renomear evidência é uma operação só
> Depois que existe evidência nomeada com `CT-NNN`, **renumerar os CTs sozinho quebra o vínculo em silêncio** — o arquivo segue apontando pro número antigo e nada acusa.
>
> Renumerar **é permitido** (fila de CT com buracos e casos cancelados no meio fica ilegível), mas card e arquivos mudam **juntos, na mesma operação**. Nunca um sem o outro, e nunca no meio de uma sessão de gravação.
>
> Caso já executado e retirado do escopo **não vira buraco na numeração**: vai pra uma seção de registro no fim do card (`### G. Fora de execução`), com caso × decisão × motivo. O histórico fica, a numeração ativa segue contígua.
>
> Precedentes, os dois em 30/07 na SGV-9042: renumerei a cauda no meio da gravação e tive que reverter; depois renumerei 26 → 22 CTs **renomeando as 14 evidências no mesmo movimento**, que é a forma certa.

### 3. Mover pra subpasta do ambiente
Mover o arquivo pra subpasta correspondente:

| Ambiente | Pasta |
|---|---|
| Desenvolvimento | `Evidências/Desenvolvimento/` |
| Homologação | `Evidências/Homologação/` |
| Produção | `Evidências/Produção/` |
| Hotfix | `Evidências/Hotfix/` |
| Arquitetura | `Evidências/Arquitetura/` |
| Sem SGV/card ainda | `Evidências/Cadastrar/` |

### 4. Embedar na nota
Referenciar como embed, não como caminho em texto:
```markdown
![[9971 - solicitacao assinatura.mp4]]
```
Toca direto na nota.

## Links de atalho no título da seção Evidências

O título da seção no card de bug leva dois links de atalho:

```markdown
### Evidências [📁](file:///caminho/da/pasta/do/ambiente/) [🔍](evidencia://<número do card>)
```

- **📁**: abre a pasta do ambiente inteira no gerenciador de arquivos. Mostra todos os vídeos daquele ambiente.
- **🔍**: usa esquema de URI customizado (`evidencia://`) que abre o Nautilus em modo de busca pelo número do card. Infra: script `~/.local/bin/abrir-evidencia` + `.desktop` em `~/.local/share/applications/abrir-evidencia.desktop`. Só funciona em Linux/GNOME/Nautilus. Em outro computador, cai de volta pro link `file://`. Configuração completa: [[Sistema/Contexto/Plugins Instalados#Esquema de URI `evidencia://` (fora do Obsidian, específico desta máquina)|Plugins Instalados]].

## Mesma gravação para mais de um card

Quando uma gravação serve a mais de um card (ex.: validação que reprova uma demanda e abre um bug novo):
1. Criar uma cópia do arquivo renomeada com o número de cada card
2. Cada card embeda a sua cópia
3. Anotar o compartilhamento em **Observações** dos dois lados:
   ```
   Evidência compartilhada com SGV-XXXX — mesmo vídeo, cópia renomeada.
   ```

## Subpastas

```
Evidências/
├── Desenvolvimento/
├── Homologação/
├── Hotfix/
├── Produção/
├── Arquitetura/
└── Cadastrar/        ← cards sem SGV ainda
```

> [!info] Evidências não são versionadas
> A pasta `Evidências/` está no `.gitignore`. Para migrar pra outro computador: nuvem, HD externo ou cópia manual.
