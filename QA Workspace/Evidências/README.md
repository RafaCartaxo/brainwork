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
- **🔍**: usa esquema de URI customizado (`evidencia://`) que abre o Nautilus em modo de busca pelo número do card. Infra: script `~/.local/bin/abrir-evidencia` + `.desktop` em `~/.local/share/applications/abrir-evidencia.desktop`. Só funciona em Linux/GNOME/Nautilus. Em outro computador, cai de volta pro link `file://`. Configuração completa: [[Sistema/Contexto/Plugins Instalados#Esquema de URI evidencia:// fora do Obsidian específico desta máquina|Plugins Instalados]].

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
