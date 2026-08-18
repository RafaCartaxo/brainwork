#!/usr/bin/env python3
"""
qa-atualiza.py — motor determinístico do botão "🔄 Atualizar" da Dashboard.

Faz a parte MECÂNICA do ciclo documentado em Sistema/Skills/SKILL_INBOX.md,
sem IA nenhuma (offline, stdlib):

1. Garante a daily de hoje (cria do zero se não existir).
2. Carry-over: itens não finalizados da daily anterior entram em
   "Pendências de ontem"/"A fazer hoje" de hoje (sem duplicar).
3. Continuação de pendências concluídas COM resultado anotado entre parênteses:
   - "Cadastrar melhoria MEL-NNNN ... (SGV-XXXX)" -> renomeia card, task, 💡, checkbox da proposta
   - "Retestar/validar ... SGV-XXXX ... (aprovada|reprovada|não reproduzido)" -> frase padrão,
     card atualizado/movido na esteira, Histórico
   - "Revisar cenários ... SGV-XXXX ... (resultado)" -> linha em Atividades + Histórico
   - "Cadastrar ... [[card]] ... (SGV-XXXX)" -> preenche task e renomeia o card linkado
4. Concluído SEM anotação -> não inventa: sinaliza "aguardando resultado".
5. Registra tudo no callout recolhido "[!organizacao]- Auto-organização" da daily.

O que este script NÃO faz (fica pra IA — sessão interativa ou tarefa das 7h):
classificar anotações cruas de ## Anotações / ## Bugs encontrados.

Idempotente: linha processada ganha o sufixo " → ..." e nunca é reprocessada.
"""
import datetime
import glob
import os
import re
import sys

VAULT = os.environ.get("QA_VAULT") or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
WS = os.path.join(VAULT, "QA Workspace")
DAILY_DIR = os.path.join(WS, "01 Daily")
DEMANDAS = os.path.join(WS, "02 Demandas")

AMB_NOME = {"DEV": "DEV", "HML": "homologação", "HOTFIX": "hotfix", "PROD": "produção"}
acoes, avisos = [], []


def ler(p):
    with open(p, encoding="utf-8") as f:
        return f.read()


def gravar(p, t):
    with open(p, "w", encoding="utf-8") as f:
        f.write(t)


def daily_path(d):
    return os.path.join(DAILY_DIR, f"{d:%Y-%m}", f"{d:%d-%m}.md")


def dailies_anteriores(hoje):
    out = []
    for p in glob.glob(os.path.join(DAILY_DIR, "*", "*.md")):
        m = re.match(r"(\d{2})-(\d{2})$", os.path.splitext(os.path.basename(p))[0])
        ano = os.path.basename(os.path.dirname(p)).split("-")[0]
        if m and ano.isdigit():
            try:
                d = datetime.date(int(ano), int(m.group(2)), int(m.group(1)))
            except ValueError:
                continue
            if d < hoje:
                out.append((d, p))
    return sorted(out)


def template_daily(hoje, ontem, itens):
    call = "\n".join(f"> - {i}" for i in itens) or "> - "
    afazer = "\n".join(f"> - [ ] {i}" for i in itens) or "> - [ ] "
    origem = f"{ontem:%d/%m}" if ontem else "—"
    return f"""---
tags:
  - daily
  - qa
cssclasses:
  - qa-daily
date: {hoje:%Y-%m-%d}
---
# Daily QA — {hoje:%d/%m/%Y}

## Status — reunião
> [!abstract] Lista do que foi feito hoje
> **Fiz**
> - 
>
> **Foco de hoje**
> - 
>
> **Travas**
> - 
<!-- gerado em {hoje:%Y-%m-%d} -->

---

## Pendências de ontem
> [!info]- Carregado de {origem}
{call}

> **A fazer hoje:**
{afazer}

---

## Atividades

### Planejamento
-

### DEV
-

### HML
-

### POCs
-

## Bugs encontrados
-

## Melhorias propostas
- [ ]

## Anotações
> [!note]- Anotações do dia
> -

## Pendente para amanhã
- [ ]
"""


def itens_nao_finalizados(texto):
    """Itens '- [ ]' do A fazer hoje (callout) e do Pendente para amanhã, sem vazios.

    **Recorte por seção, de propósito.** A versão anterior varria o arquivo
    inteiro, então QUALQUER checkbox virava pendência de amanhã:

    - rascunho de CT escrito em `## Anotações` entrou na fila como item
      chamado "Não", do `- [ ] Não` do "Execução Passou?" (precedente: 30/07);
    - checkbox de `## Melhorias propostas` era recopiado todo dia, contra a
      regra explícita do 01 Daily/README ("aqui **não se recopia**" — a
      Dashboard agrega os não marcados de todas as dailies sozinha).

    O docstring já dizia "A fazer hoje e Pendente para amanhã" desde sempre; a
    implementação é que nunca respeitou o próprio contrato. Divergência
    doc × código é pior que doc ausente: dá falsa confiança na leitura.

    **Linha aninhada (defeito) NÃO entra no carry-over — de propósito.** O
    regex `^>? ?- \\[ \\]` aceita no máximo um espaço depois do `>`, então o
    filho indentado (`>     - [ ]`) não casa. Isso é o comportamento correto:
    o defeito é recriado a partir do card pelo invariante da fila viva
    (`sincroniza_demandas_ativas`), com o aninhamento certo. Se ele entrasse
    aqui, voltaria como item **de topo**, achatando a hierarquia todo dia.
    Não "consertar" este regex sem ler o aninhamento junto.
    """
    regioes = []
    m = re.search(r"> \*\*A fazer hoje:\*\*\n((?:>.*\n)*)", texto)
    if m:
        regioes.append(m.group(1))
    m = re.search(r"## Pendente para amanhã\n(.*?)(?=\n## |\n> \[!organizacao\]|\Z)",
                  texto, re.S)
    if m:
        regioes.append(m.group(1))
    out = []
    for regiao in regioes:
        for mm in re.finditer(r"^>? ?- \[ \] (.+)$", regiao, re.M):
            item = mm.group(1).strip()
            if item:
                out.append(item)
    return out


def ids_de(texto):
    return set(re.findall(r"SGV-?\d+|MEL-\d{4}", texto))


def tem_tag(texto_card, tag):
    return (re.search(rf"^tags:\n(?:  - .*\n)*  - {tag}\b", texto_card, re.M) is not None
            or f"\n  - {tag}\n" in texto_card)


def eh_defeito(texto_card):
    """Defeito = filho de uma task pai (PADROES_QA → 'Defeito × Bug').

    O campo `pai` é o dado; a tag é a convenção. Aceita os dois porque card
    migrado pode ter um sem o outro por um tempo."""
    return bool(re.search(r'^pai: *"?\d+"? *$', texto_card, re.M)) or tem_tag(texto_card, "defeito")


def pai_do_card(texto_card):
    """SGV da task pai, ou None se o card é independente."""
    m = re.search(r'^pai: *"?(\d+)"? *$', texto_card, re.M)
    return m.group(1) if m else None


def tipo_do_card(texto_card):
    """Bug é o padrão (sem prefixo na frase); outros tipos prefixam."""
    if eh_defeito(texto_card):
        return "Defeito "
    if tem_tag(texto_card, "bug"):
        return ""
    m = re.search(r"\*\*Tipo:\*\* *(\w+)", texto_card)
    if m:
        return m.group(1).capitalize() + " "
    if re.search(r'^mel:', texto_card, re.M):
        return "Melhoria "
    return "Demanda "


def achar_card(num):
    """Localiza o card de um SGV. Duas passadas, nesta ordem:

    1. **Nome do arquivo** começando com `<num> - ` — o padrão do vault.
    2. **Frontmatter `task:`** — rede pra card cujo nome não segue o padrão.
       Acontece com card nascido sem SGV (`Bug <Título>`, ver SKILL_BUGS) e
       com card antigo. Sem esta passada o roteador de evidências avisou
       "card do SGV-3413 não existe" **todos os dias por 10 dias**, com o
       card existindo em `99 Arquivo/` e afirmando "sem cópia local no
       vault" enquanto o vídeo ficava parado na raiz de `Evidências/`
       (precedente: 30/07). O nome do arquivo é convenção; o `task:` é o
       dado. Casar só pela convenção gera pendência falsa que ninguém
       consegue fechar, porque a coisa que ela pede já existe.
    """
    caminhos = [p
                for base in (DEMANDAS, os.path.join(WS, "99 Arquivo"))
                for p in glob.glob(os.path.join(base, "**", "*.md"), recursive=True)]
    for p in caminhos:
        if os.path.basename(p).startswith(f"{num} - "):
            return p
    for p in caminhos:
        if re.search(rf'^task: *"?{num}"? *$', ler(p), re.M):
            return p
    return None


def set_frontmatter(texto, campo, valor):
    if re.search(rf"^{campo}:", texto, re.M):
        return re.sub(rf"^{campo}:.*$", f'{campo}: "{valor}"', texto, count=1, flags=re.M)
    return texto.replace("---\n", f'---\n{campo}: "{valor}"\n', 1)


def add_historico(texto, frase, hoje):
    entrada = f"    - {hoje:%Y-%m-%d} - {frase}"
    if "- Histórico:" in texto:
        return texto.replace("- Histórico:", f"- Histórico:\n{entrada}", 1).replace(f"{entrada}\n", f"{entrada}\n", 1) \
            if False else re.sub(r"(- Histórico:\n(?:    - .*\n)*)", rf"\g<1>{entrada}\n", texto, count=1)
    return texto.rstrip() + f"\n- Histórico:\n{entrada}\n"


def add_atividade(daily, secao, linha):
    padrao_vazio = f"### {secao}\n- \n"
    if padrao_vazio in daily:
        return daily.replace(padrao_vazio, f"### {secao}\n- {linha}\n", 1)
    return re.sub(rf"(### {secao}\n)", rf"\g<1>- {linha}\n", daily, count=1)


def add_pendencia_afazer(daily, item):
    return re.sub(r"(> \*\*A fazer hoje:\*\*\n)", rf"\g<1>> - [ ] {item}\n", daily, count=1)


def add_pendencia(daily, item):
    if re.search(r"## Pendente para amanhã\n- \[ \] *\n", daily):
        return re.sub(r"## Pendente para amanhã\n- \[ \] *\n", f"## Pendente para amanhã\n- [ ] {item}\n", daily, count=1)
    return re.sub(r"(## Pendente para amanhã\n)", rf"\g<1>- [ ] {item}\n", daily, count=1)


def link(card_path, rotulo):
    rel = os.path.relpath(card_path, VAULT).replace(os.sep, "/")[:-3]
    return f"[[{rel}|{rotulo}]]"


def atualiza_links_globais(antigo_base, novo_base):
    for p in glob.glob(os.path.join(WS, "**", "*.md"), recursive=True):
        t = ler(p)
        if antigo_base in t:
            gravar(p, t.replace(antigo_base, novo_base))


def marca_proposta_mel(nnnn):
    for _, p in dailies_anteriores(datetime.date.today() + datetime.timedelta(days=1)):
        t = ler(p)
        novo = re.sub(rf"^- \[ \] (\*\*.*MEL-{nnnn}.*)$", r"- [x] \1", t, count=1, flags=re.M)
        if novo != t:
            gravar(p, novo)
            return True
    return False



def norm_id(tok):
    return re.sub(r"SGV-?", "SGV-", tok)


INDENT_FILHO = ">     "   # 4 espaços após o '>' — sublista dentro do callout da fila


def _itens_da_fila(texto):
    """Todos os itens de 'A fazer hoje', **de topo e aninhados**.

    O dedup precisa enxergar os dois níveis. Só o regex de topo
    (`^> - \\[ \\]`) deixaria um defeito já aninhado parecer ausente, e o
    invariante o recriaria no topo a cada execução do 🔄 — a mesma classe de
    bug de idempotência que duplicou pendência em 18/08."""
    return re.findall(r"^>(?: +)?- \[.\] (.+)$", texto, re.M)


def sincroniza_demandas_ativas(texto):
    """Invariante da fila viva: TODO card em aberto (02 Demandas fora de
    Concluídas) tem um item ativo em 'A fazer hoje' — vale pra qualquer
    estágio (a refinar, refinada, cadastrada, em validação, reaberta).
    Se a pendência está em 'Pendente para amanhã', move pra cima;
    se não existe, cria o próximo passo padrão.

    **Defeito não ganha linha de topo** (PADROES_QA → 'Defeito × Bug'): ele
    entra aninhado sob a linha da task pai, porque defeito e pai são um
    trabalho só. A 3234 sozinha ocupava 6 linhas da fila (1 pai + 5 defeitos)
    pra uma única validação. Por isso os pais são processados **primeiro** —
    a linha do pai precisa existir antes de pendurar filho nela.
    """
    cards = []
    for pasta in ("DEV", "HML", "Hotfix", "POCs"):
        cards += glob.glob(os.path.join(DEMANDAS, pasta, "*.md"))

    # pais primeiro, filhos depois — a ordem é o que garante o alvo do aninhamento
    def ordem(card):
        return (1 if eh_defeito(ler(card)) else 0, card)

    for card in sorted(cards, key=ordem):
        base = os.path.splitext(os.path.basename(card))[0]
        tcard = ler(card)
        # card SEM DONO fica fora da fila (PADROES_QA → 'responsavel').
        # A fila é a lista do que é SEU; demanda disponível pra qualquer QA
        # pegar não ocupa linha nela. Sai da fila mas NÃO some: a Dashboard
        # tem a seção "Sem dono — disponível pra pegar".
        # De propósito **sem aviso**: aviso diário sobre algo que ninguém
        # pediu pra fazer é exatamente o incômodo que esta exceção evita.
        # Seguro por construção: em 18/08 os 42 cards abertos tinham
        # `responsavel: Rafael`, nenhum vazio — a regra não tirou item nenhum
        # da fila existente. Precedente: SGV-10363.
        dono = re.search(r"^responsavel: *(.*)$", tcard, re.M)
        if not dono or not dono.group(1).strip().strip('"'):
            continue
        task = re.search(r'^task: *"?(\d+)"?\s*$', tcard, re.M)
        melm = re.search(r"MEL-(\d{4})", base)
        if task:
            rid = f"SGV-{task.group(1)}"
        elif melm:
            rid = f"MEL-{melm.group(1)}"
        else:
            continue  # card sem identificador — fora do radar automático
        titulo = base.split(" - ", 1)[1] if " - " in base else base
        if any(rid in norm_id(a) for a in _itens_da_fila(texto)):
            continue

        # --- defeito: pendura sob a pai, não cria item de topo ---
        pai = pai_do_card(tcard)
        if pai:
            rid_pai = f"SGV-{pai}"
            linha_filho = f"{INDENT_FILHO}- [ ] ↳ {rid} - Defeito ({titulo})\n"
            m_pai = None
            for m in re.finditer(r"^> - \[ \] (.+)$", texto, re.M):
                if rid_pai in norm_id(m.group(1)):
                    m_pai = m
                    break
            if m_pai:
                # insere logo abaixo da linha da pai, depois dos filhos que já existirem
                pos = m_pai.end() + 1
                while True:
                    prox = texto.find("\n", pos)
                    linha = texto[pos:prox if prox != -1 else len(texto)]
                    if not linha.startswith(INDENT_FILHO):
                        break
                    pos = (prox + 1) if prox != -1 else len(texto)
                texto = texto[:pos] + linha_filho + texto[pos:]
                acoes.append(f"{rid} → fila viva: aninhado sob {rid_pai}")
                continue
            # pai sem linha na fila (já concluída?) — não some em silêncio
            avisos.append(f"⚠️ {rid} é defeito da {rid_pai}, mas a pai não tem item na fila "
                          f"— defeito aberto com pai fora da esteira, conferir")
            continue

        # --- card normal: item de topo, como sempre ---
        movida = None
        for m in re.finditer(r"^- \[ \] (.+)$", texto, re.M):
            if "## Pendente para amanhã" not in texto[:m.start()]:
                continue
            if rid in norm_id(m.group(1)):
                movida = m.group(1)
                texto = texto[:m.start()] + texto[m.end() + 1:]
                break
        if movida is None:
            if rid.startswith("MEL"):
                movida = f"{rid} - Cadastrar melhoria no Notion"
            else:
                movida = f"{rid} - Acompanhar ({titulo})"
        texto = re.sub(r"(> \*\*A fazer hoje:\*\*\n)", rf"\g<1>> - [ ] {movida}\n", texto, count=1)
        if re.search(r"## Pendente para amanhã\n(?!- )", texto):
            texto = texto.replace("## Pendente para amanhã\n", "## Pendente para amanhã\n- [ ] \n", 1)
        acoes.append(f"{rid} → fila viva: {movida[:55]}")
    return texto


def processa_continuacoes(daily, hoje):
    linhas = daily.split("\n")
    for i, ln in enumerate(linhas):
        m = re.match(r"^(>? ?)- \[x\] (.+)$", ln)
        if not m or "→" in ln:
            continue
        corpo = m.group(2)
        # ignora marcações antigas de conclusão pura (✅ AAAA-MM-DD sem parêntese de resultado)
        anot = re.findall(r"\(([^)]+)\)", corpo)
        anot = anot[-1].strip() if anot else None
        sgv = re.search(r"SGV-?(\d+)", corpo)
        mel = re.search(r"MEL-(\d{4})", corpo)
        res = None

        if not anot or re.fullmatch(r"reaberta.*|card refinado|.*✅.*", anot or ""):
            # sem anotação de resultado utilizável: sinaliza só se é padrão de continuação
            if (sgv or mel) and re.search(r"adastrar|etestar|alidar|evisar cen|companhar", corpo):
                avisos.append(f"⏳ aguardando resultado: {corpo[:70]}")
            continue

        # 1) cadastro de melhoria: MEL + SGV na anotação
        if mel and "adastrar" in corpo and re.search(r"SGV-?\d+", anot):
            num = re.search(r"SGV-?(\d+)", anot).group(1)
            card = None
            for p in glob.glob(os.path.join(DEMANDAS, "**", f"MEL-{mel.group(1)} - *.md"), recursive=True):
                card = p
            if not card:
                avisos.append(f"⚠️ card MEL-{mel.group(1)} não encontrado")
                continue
            t = ler(card)
            t = set_frontmatter(t, "task", num)
            t = add_historico(t, f"💡 Cadastrada no Notion como SGV-{num}", hoje)
            antigo = os.path.splitext(os.path.basename(card))[0]
            novo_base = f"{num} - " + antigo.split(" - ", 1)[1]
            novo_path = os.path.join(os.path.dirname(card), novo_base + ".md")
            gravar(card, t)
            os.rename(card, novo_path)
            atualiza_links_globais(antigo, novo_base)
            marca_proposta_mel(mel.group(1))
            linhas = [l.replace(antigo, novo_base) for l in linhas]
            ln = ln.replace(antigo, novo_base)
            res = f"cadastrada como SGV-{num}"
            frase = f"💡 {link(novo_path, f'SGV-{num}')} - Melhoria cadastrada (MEL-{mel.group(1)})"
            linhas[i] = ln + f" → {res}"
            daily = add_atividade("\n".join(linhas), "DEV", frase)
            linhas = daily.split("\n")
            acoes.append(f"MEL-{mel.group(1)} → {res}")
            continue

        # 2) revisar cenários
        if sgv and corpo.lstrip().lower().startswith("revisar cenários"):
            num = sgv.group(1)
            card = achar_card(num)
            frase = f"📋 SGV-{num} - Cenários de teste revisados ({anot})"
            if card:
                gravar(card, add_historico(ler(card), f"📋 Cenários de teste revisados ({anot})", hoje))
                frase = f"📋 {link(card, f'SGV-{num}')} - Cenários de teste revisados ({anot})"
            linhas[i] = ln + " → registrado"
            daily = add_atividade("\n".join(linhas), "DEV", frase)
            linhas = daily.split("\n")
            acoes.append(f"SGV-{num} → cenários revisados ({anot})")
            continue

        # 2.5) investigação de suspeita (confirmada / descartada)
        if re.search(r"[Ii]nvestigar suspeita", corpo):
            titulo = re.sub(r"^[Ii]nvestigar suspeita:? *", "", corpo.split("(")[0]).strip(' "')
            al = anot.lower()
            if al.startswith("descartad"):
                motivo = anot.split(":", 1)[1].strip() if ":" in anot else "não reproduz"
                frase = f"🗑️ Suspeita descartada: {titulo} (não é bug: {motivo})"
                linhas[i] = ln + " → descartada"
                daily = add_atividade("\n".join(linhas), "DEV", frase)
                linhas = daily.split("\n")
                acoes.append(f"suspeita descartada: {titulo[:40]}")
                continue
            if al.startswith("confirmad"):
                linhas[i] = ln + " → confirmada (criar card)"
                daily = add_pendencia_afazer("\n".join(linhas), f"Criar card do bug: {titulo} (via SKILL_BUGS, sessão/IA)")
                linhas = daily.split("\n")
                acoes.append(f"suspeita confirmada: {titulo[:40]} — criar card via sessão")
                continue

        # 2.6) análise/critérios levados pro Notion
        if sgv and re.search(r"[Nn]otion", corpo) and re.match(r"(feito|atualizad[oa]|registrad[oa])", anot.lower()):
            num = sgv.group(1)
            card = achar_card(num)
            if card:
                tc = ler(card)
                tipo = tipo_do_card(tc)
                verbo = (tipo + "atualizada no Notion") if tipo else "Bug atualizado no Notion"
                gravar(card, add_historico(tc, "📤 Análise/critérios registrados na task do Notion", hoje))
                frase = f"📤 {link(card, f'SGV-{num}')} - {verbo} (análise/critérios registrados na task)"
            else:
                frase = f"📤 SGV-{num} - Atualizado no Notion (análise/critérios registrados na task)"
            linhas[i] = ln + " → registrado"
            daily = add_atividade("\n".join(linhas), "DEV", frase)
            linhas = daily.split("\n")
            acoes.append(f"SGV-{num} → atualizado no Notion")
            continue

        # 3) validação (aprovada / reprovada / não reproduzido)
        chave = anot.lower()
        if sgv and re.match(r"(aprovada|reprovada|n[aã]o reproduzido)", chave):
            num = sgv.group(1)
            card = achar_card(num)
            if not card:
                # resultado de validação registrado pra demanda que ainda não tem
                # card: não se inventa card (título/CTs/módulo são julgamento — ver
                # "Fronteira com o script" no AGENTE_FILA), mas o resultado NÃO pode
                # se perder em silêncio. Vira aviso + pendência explícita.
                avisos.append(f"⚠️ SGV-{num} validado ({anot}) mas sem card no vault "
                              f"— pendência de criação enfileirada")
                pend = (f"SGV-{num} - Criar card (validação '{anot}' registrada em "
                        f"{hoje:%d/%m}, sem card no vault)")
                daily2 = "\n".join(linhas)
                if pend not in daily2:
                    # add_pendencia_afazer → fila de HOJE (o trabalho já foi feito, o
                    # card falta agora); add_pendencia joga pra "Pendente para amanhã"
                    linhas = add_pendencia_afazer(daily2, pend).split("\n")
                    acoes.append(f"fila: pendência de criar card do SGV-{num}")
                continue
            t = ler(card)
            amb = (re.search(r"^ambiente: *(\S+)", t, re.M) or [None, "HML"])[1].upper()
            amb_nome = AMB_NOME.get(amb, amb.lower())
            ja_reaberta = "🔴" in t
            secao = "DEV" if amb == "DEV" else "HML"
            tipo = tipo_do_card(t)
            if chave.startswith("aprovada"):
                # deploy pendente bloqueia o fechamento em silêncio (proposta de
                # 31/07 nº3, decidida em 18/08): o campo deploy existe justamente
                # pra dizer "este ambiente não tem o fix" — aprovação registrada
                # nessas condições não pode mover o card como se fosse válida.
                deploy_pend = re.search(r"^deploy: *pendente_(\w+)", t, re.M)
                if deploy_pend:
                    avisos.append(f"⚠️ SGV-{num} aprovada ({anot}) mas card tem "
                                  f"deploy: pendente_{deploy_pend.group(1)} — confirmar "
                                  f"que o fix subiu antes de mover o card, e remover o "
                                  f"campo do frontmatter")
                    continue
                # ambiente explícito na anotação vence o frontmatter, nos dois
                # sentidos (proposta de 31/07 nº3, decidida em 18/08): o campo
                # `ambiente` reflete a posição do card na esteira, não
                # necessariamente o último ambiente testado (PADROES_QA). Sem
                # anotação explícita, mantém o que já vinha do frontmatter.
                if re.search(r"em dev\b", chave):
                    amb, amb_nome, secao = "DEV", "DEV", "DEV"
                elif re.search(r"em (homolog|hotfix)", chave):
                    amb = "HML"
                    amb_nome = "homologação" if "homolog" in chave else "hotfix"
                    secao = "HML"
                if amb == "DEV":
                    frase_txt = tipo + (("retestada e aprovada" if tipo else "Retestada e aprovada") if ja_reaberta else ("aprovada" if tipo else "Aprovada")) + " em DEV"
                    emoji = "🔁" if ja_reaberta else "✅"
                    t = re.sub(r"^ambiente:.*$", "ambiente: HML", t, count=1, flags=re.M)
                    t = add_historico(t, f"{emoji} {frase_txt} — segue pra homologação", hoje)
                    destino = os.path.join(DEMANDAS, "HML", os.path.basename(card))
                else:
                    frase_txt = tipo + (("retestada e aprovada" if tipo else "Retestada e aprovada") if ja_reaberta else ("aprovada" if tipo else "Aprovada")) + f" em {amb_nome}"
                    emoji = "🔁" if ja_reaberta else "✅"
                    t = re.sub(r"^status:.*$", "status: resolvido", t, count=1, flags=re.M)
                    t = set_frontmatter(t, "data_fim", f"{hoje:%Y-%m-%d}")
                    t = add_historico(t, f"{emoji} {frase_txt}", hoje)
                    destino = os.path.join(DEMANDAS, "Concluídas", os.path.basename(card))
                gravar(card, t)
                if os.path.abspath(os.path.dirname(card)) != os.path.abspath(os.path.dirname(destino)):
                    os.rename(card, destino)
                    card = destino
                frase = f"{emoji} {link(card, f'SGV-{num}')} - {frase_txt}"
                res = frase_txt.lower()
            elif chave.startswith("reprovada"):
                de_novo = "novamente " if ja_reaberta else ""
                frase_txt = (f"{tipo}reaberta {de_novo}em {amb_nome}" if tipo else f"Reaberta {de_novo}em {amb_nome}").replace("  ", " ")
                t = re.sub(r"^status:.*$", "status: aberto", t, count=1, flags=re.M)
                t = add_historico(t, f"🔴 {frase_txt}", hoje)
                gravar(card, t)
                frase = f"🔴 {link(card, f'SGV-{num}')} - {frase_txt}"
                daily2 = add_pendencia("\n".join(linhas), f"Revalidar SGV-{num} (reaberta em {amb_nome})")
                linhas = daily2.split("\n")
                res = frase_txt.lower()
            else:
                frase_txt = f"{tipo}retestada, não reproduzido" if tipo else "Retestado, não reproduzido"
                gravar(card, add_historico(t, f"⚪ {frase_txt}", hoje))
                frase = f"⚪ {link(card, f'SGV-{num}')} - {frase_txt}"
                res = "não reproduzido"
            # marca a linha original (o índice i pode ter mudado com a pendência — remarca por conteúdo)
            for j, l2 in enumerate(linhas):
                if l2 == ln:
                    linhas[j] = ln + f" → {res}"
                    break
            daily = add_atividade("\n".join(linhas), secao, frase)
            linhas = daily.split("\n")
            acoes.append(f"SGV-{num} → {res}")
            continue

        # 4) cadastrar bug com card linkado
        if "adastrar" in corpo and re.search(r"SGV-?\d+", anot):
            wl = re.search(r"\[\[([^\]|]+)(?:\|[^\]]*)?\]\]", corpo)
            if not wl:
                avisos.append(f"⏳ cadastro sem card linkado (não sei qual card): {corpo[:60]}")
                continue
            num = re.search(r"SGV-?(\d+)", anot).group(1)
            alvo = os.path.join(VAULT, wl.group(1) + ".md")
            if not os.path.exists(alvo):
                avisos.append(f"⚠️ card linkado não existe: {wl.group(1)}")
                continue
            t = set_frontmatter(ler(alvo), "task", num)
            t = add_historico(t, f"🐛 Cadastrado no Notion como SGV-{num}", hoje)
            antigo = os.path.splitext(os.path.basename(alvo))[0]
            novo_base = antigo if re.match(r"^\d+ - ", antigo) else f"{num} - {antigo}"
            novo_path = os.path.join(os.path.dirname(alvo), novo_base + ".md")
            gravar(alvo, t)
            if novo_path != alvo:
                os.rename(alvo, novo_path)
                atualiza_links_globais(antigo, novo_base)
            for j, l2 in enumerate(linhas):
                if l2 == ln:
                    linhas[j] = ln + f" → cadastrado como SGV-{num}"
                    break
            frase = f"🐛 {link(novo_path, f'SGV-{num}')} - Bug cadastrado"
            daily = add_atividade("\n".join(linhas), "DEV", frase)
            linhas = daily.split("\n")
            acoes.append(f"SGV-{num} → cadastro preenchido no card")
            continue

    return "\n".join(linhas)


def reconcilia_atividades(texto, hoje):
    """Rafael pode registrar o ciclo direto em Atividades (frases padrão à mão).
    O botão reconcilia: pra cada linha de hoje cujo card não reflete o estado
    declarado, aplica o estado — inclusive pulando etapas ("o fim implica os
    passos anteriores"), com a inferência registrada no Histórico.
    Idempotente por comparação de estado + dedupe de Histórico por data."""
    m = re.search(r"## Atividades\n(.*?)\n## ", texto, re.S)
    if not m:
        return
    for ln in m.group(1).split("\n"):
        lm = re.match(r"^- (✅|🔁|🔴|⚪|📤|🗑️) .*?SGV[- ]?(\d+).*? - (.+)$", ln)
        if not lm:
            continue
        emoji, num, frase = lm.group(1), lm.group(2), lm.group(3).strip()
        card = achar_card(num)
        if not card:
            # A daily DECLARA um estado que nenhum card reflete. Antes era `continue`
            # mudo — o 🔄 dizia "tudo em dia" e o trabalho ficava sem esteira.
            # Mas só avisa se a linha AFIRMA ter card (wikilink): SGV em texto puro é
            # a convenção documentada de "sem card local" (regra de links; precedentes
            # SGV-9633 e SGV-6136) e avisar nesses casos seria ruído em todo run.
            if "[[" in ln:
                avisos.append(f"⚠️ Atividades linka um card do SGV-{num} que não existe "
                              f"('{emoji} {frase[:40]}') — link quebrado?")
            continue
        t = ler(card)
        if f"- {hoje:%Y-%m-%d} - {emoji}" in t:
            continue  # já registrado hoje (feito pelo botão ou à mão)
        fl = frase.lower()
        if emoji in ("✅", "🔁") and re.search(r"aprovada em (homolog|hotfix)", fl):
            if "/Concluídas/" in card or f"{os.sep}Concluídas{os.sep}" in card:
                continue
            pulou = f"{os.sep}DEV{os.sep}" in card
            t = re.sub(r"^status:.*$", "status: resolvido", t, count=1, flags=re.M)
            t = re.sub(r"^ambiente:.*$", "ambiente: HML", t, count=1, flags=re.M)
            t = set_frontmatter(t, "data_fim", f"{hoje:%Y-%m-%d}")
            sufixo = " (etapas anteriores concluídas implicitamente)" if pulou else ""
            t = add_historico(t, f"{emoji} {frase}{sufixo}", hoje)
            gravar(card, t)
            destino = os.path.join(DEMANDAS, "Concluídas", os.path.basename(card))
            os.rename(card, destino)
            acoes.append(f"SGV-{num} → card sincronizado: concluído{sufixo}")
        elif emoji in ("✅", "🔁") and "aprovada em dev" in fl:
            if f"{os.sep}DEV{os.sep}" not in card:
                continue
            t = re.sub(r"^ambiente:.*$", "ambiente: HML", t, count=1, flags=re.M)
            t = add_historico(t, f"{emoji} {frase} — segue pra homologação", hoje)
            gravar(card, t)
            os.rename(card, os.path.join(DEMANDAS, "HML", os.path.basename(card)))
            acoes.append(f"SGV-{num} → card sincronizado: movido pra HML")
        elif emoji == "🔴":
            if re.search(r"^status: *aberto", t, re.M):
                continue
            t = re.sub(r"^status:.*$", "status: aberto", t, count=1, flags=re.M)
            gravar(card, add_historico(t, f"🔴 {frase}", hoje))
            acoes.append(f"SGV-{num} → card sincronizado: reaberto")
        elif emoji == "⚪":
            gravar(card, add_historico(t, f"⚪ {frase}", hoje))
            acoes.append(f"SGV-{num} → não reproduzido registrado no card")
        elif emoji == "📤":
            gravar(card, add_historico(t, "📤 Análise/critérios registrados na task do Notion", hoje))
            acoes.append(f"SGV-{num} → atualização no Notion registrada no card")
        elif emoji == "🗑️":
            if f"{os.sep}99 Arquivo{os.sep}" in card:
                continue
            t = re.sub(r"^status:.*$", "status: descartado", t, count=1, flags=re.M)
            t = add_historico(t, f"🗑️ {frase}", hoje)
            gravar(card, t)
            os.rename(card, os.path.join(WS, "99 Arquivo", os.path.basename(card)))
            acoes.append(f"SGV-{num} → card sincronizado: descartado (99 Arquivo)")


# kws = radicais que identificam a PENDÊNCIA equivalente na fila (usados só no
# teste `coberto`, contra as linhas de "A fazer hoje": "Validar", "Refinar",
# "Cadastrar"...). NÃO servem pra casar contra a copy de Atividades, que usa
# outro vocabulário ("Aprovada em homologação", "Melhoria refinada") — usar
# radicais, não palavras inteiras, senão "refinar" não casa "refinada".
LEDGER = [
    ("🚀", ("valida", "test", "início"), "{rid} - Iniciar validação (registrado)"),
    ("💭", ("propor", "proposta", "suspeita"), "{rid} - Propor (proposta registrada)"),
    ("📝", ("refin",), "{rid} - Refinar (card criado, critérios prontos)"),
    ("📤", ("notion",), "{rid} - Atualizar no Notion (análise/critérios registrados)"),
    ("💡", ("cadastr",), "{rid} - Cadastrar no Notion (feito)"),
    ("🐛", ("cadastr", "card do bug", "confirmad"), "{rid} - Cadastrar (feito)"),
    ("🗑️", ("descart", "investigar", "suspeita"), "{rid} - Descartar (feito)"),
    ("✅", ("valida", "retest", "revalida", "test", "revis", "companhar"), "{rid} - Validar (aprovada)"),
    ("🔁", ("valida", "retest", "revalida", "test", "companhar"), "{rid} - Retestar (aprovada)"),
    ("🔴", ("valida", "retest", "revalida", "test", "companhar"), "{rid} - Retestar (reprovada)"),
    ("⚪", ("valida", "retest", "revalida", "test", "companhar"), "{rid} - Retestar (não reproduzido)"),
    ("🔎", ("revis", "analis", "análise", "escopo", "cenári"), "{rid} - Revisar cenários/análise (concluída)"),
    ("📋", ("triagem", "bater"), "{rid} - Triagem (item batido)"),
    # 📚 existia no catálogo do 01 Daily/README desde sempre, mas não aqui: linha de
    # documentação importada/atualizada não gerava checkbox de ledger e o dia fechava
    # com a atividade registrada e a fila sem ela. Aviso disparado em 29/07, corrigido
    # em 30/07. `rid` aqui é o nome da doc, não um SGV — o ledger aceita os dois.
    ("📚", ("document", "doc ", "importa", "atualiz"), "{rid} - Documentar (importada/atualizada)"),
]

# Emojis reconhecidos como prefixo de linha em Atividades (ordem não importa aqui;
# usados em alternação, nunca como character class solto — 🗑️ é 2 codepoints).
# 🚀 (início de validação) e 🔧 (trabalho de ferramenta/processo) adicionados em
# 18/08 — proposta de 31/07 nº2 e nº4. 🔧 não tem entrada no LEDGER de propósito:
# é registro informativo do dia, não gera pendência de fila.
_EMOJI_ALT = "💭|📝|📤|💡|🐛|🗑️|✅|🔁|🔴|⚪|🔎|📋|📚|🚀|🔧"
# Modificadores que podem aparecer colados a um emoji da lista acima (ex.: "🔎👍",
# "🔒" sozinho) — não geram item de ledger próprio, só não podem quebrar o
# reconhecimento dos emojis "de verdade" ao lado deles na mesma linha.
_MODIFICADOR_ALT = "👍|🔒"
_PREFIXO_ALT = rf"(?:{_EMOJI_ALT}|{_MODIFICADOR_ALT})"


def _chave_sem_id(resto):
    """Assunto de uma linha de Atividades que **não tem SGV/MEL** — usado como
    identificador do item de ledger.

    Pega o texto **antes do primeiro ' - '**, que na copy oficial é o assunto
    (`📚 <Doc> - Documentação importada...` → a doc). Só cai no texto depois do
    último ':' quando não há ' - ' (`🗑️ Suspeita descartada: <título>`).

    Sem isso, a linha `📚 SKILL_BUGS e SKILL_CASOS_DE_TESTE - Regra nova:
    critério de aceite...` gerava o ledger `Registrar: critério de aceite por co
    (feito)` — pega o predicado e corta no meio da palavra. Precedente: 30/07.
    """
    if " - " in resto:
        bruto = resto.split(" - ")[0]
    else:
        bruto = resto.split(":")[-1].split("(")[0]
    # wikilink vira o alias legível: [[caminho/longo|Alias]] -> Alias
    bruto = re.sub(r"\[\[[^\]|]*\|([^\]]+)\]\]", r"\1", bruto)
    bruto = re.sub(r"\[\[([^\]]+)\]\]", r"\1", bruto)
    return re.sub(r"[`*]", "", bruto).strip()[:40]


def ledger_do_dia(texto):
    """A fazer hoje = ledger completo do dia: todo estágio executado (linha em
    Atividades) aparece também como item MARCADO na fila, com o que foi feito —
    mesmo que a tarefa nunca tenha sido enfileirada antes.

    Aceita também linhas com MAIS DE UM emoji prefixado sem espaço entre eles
    (ex.: "🔎👍 SGV-9963 - ..." ou "📝🔎 SGV-7935 - ...") — cada emoji reconhecido
    na sequência gera seu próprio item de ledger, independentemente."""
    m = re.search(r"## Atividades\n(.*?)\n## ", texto, re.S)
    if not m:
        return texto
    afazer = re.findall(r"^> - \[.\] (.+)$", texto, re.M)
    for ln in m.group(1).split("\n"):
        am = re.match(rf"^- ({_PREFIXO_ALT}+) (.+)$", ln)
        if not am:
            # linha de atividade com conteúdo mas SEM emoji de status conhecido:
            # não se inventa checkbox, mas também não se engole calado — o README
            # manda toda linha de Atividades começar com o emoji do catálogo.
            solta = re.match(r"^- (?!\s*$)(?!\[)(.{6,})$", ln)
            if solta and "[!note]" not in ln:
                avisos.append(
                    f"sem checkbox de ledger (copy fora do catálogo?): {solta.group(1)[:60]}")
            continue
        emojis = re.findall(_EMOJI_ALT, am.group(1))
        resto = am.group(2)
        idm = re.search(r"SGV[- ]?\d+|MEL-\d{4}", resto)
        rid = norm_id(idm.group(0)).replace("SGV ", "SGV-") if idm else None
        chave = rid if rid else _chave_sem_id(resto)
        for emoji in emojis:
            for e2, kws, modelo in LEDGER:
                if e2 != emoji:
                    continue
                item = modelo.format(rid=rid) if rid else f"Registrar: {chave} (feito)"
                # rede contra re-adicionar o próprio item a cada execução: o
                # `coberto` abaixo exige a palavra-chave do verbo na linha, e o
                # fallback genérico "Registrar: <chave> (feito)" não tem verbo
                # nenhum. Resultado: atividade **sem SGV** ganhava uma linha de
                # ledger nova em TODA execução do 🔄 (precedente: 30/07, a
                # suspeita descartada duplicou 2x na mesma sessão). O `coberto`
                # segue valendo pra casar com pendência escrita à mão.
                if any(a.startswith(item) for a in afazer):
                    break
                coberto = any(
                    (chave.lower() in norm_id(a).lower()) and any(k in a.lower() for k in kws)
                    for a in afazer)
                if coberto:
                    break
                texto = re.sub(r"(> \*\*A fazer hoje:\*\*\n)",
                               rf"\g<1>> - [x] {item} → registrado\n", texto, count=1)
                afazer.append(item)
                acoes.append(f"ledger: [x] {item[:55]}")
                break
    return texto


def coleta_concluidos(texto):
    """Junta os itens JÁ MARCADOS da fila sob o header '✅ Concluídos hoje',
    no fim do bloco 'A fazer hoje'.

    Escopo deliberadamente estreito: NÃO agrupa por natureza (🎯/🔎/📤/👁️/📋/🚨)
    — esse agrupamento é julgamento e pertence ao AGENTE_FILA (camada de IA).
    Aqui só se mexe no que é mecânico e inequívoco: `[x]` vai pro fim, sob o
    header, preservando na ordem original tudo o que a IA escreveu (headers de
    categoria inclusive). Idempotente: rodar 2x não duplica header nem reordena.

    **Pai com filho aberto não é movido.** Levar a linha da task pai pro fim
    deixaria os defeitos aninhados órfãos no meio da fila, apontando pra nada.
    E, pela regra do gate (PADROES_QA → 'Defeito × Bug'), pai marcada com
    defeito ainda aberto é estado inconsistente — vira aviso, não movimentação
    silenciosa.
    """
    m = re.search(r"(> \*\*A fazer hoje:\*\*\n)((?:>.*\n)*)", texto)
    if not m:
        return texto
    linhas = m.group(2).rstrip("\n").split("\n")
    HEADER = "> **✅ Concluídos hoje**"

    # Agrupa em blocos: item de topo + os filhos aninhados que vêm logo abaixo.
    # Pai e filhos viajam **juntos** — mover só a linha do pai deixaria os
    # defeitos órfãos no meio da fila apontando pra nada.
    blocos = []          # [(linha_topo, [filhos])] ou (linha_avulsa, None)
    i = 0
    while i < len(linhas):
        ln = linhas[i]
        if re.match(r"^> - \[.\] ", ln):
            filhos = []
            j = i + 1
            while j < len(linhas) and linhas[j].startswith(INDENT_FILHO):
                filhos.append(linhas[j])
                j += 1
            blocos.append((ln, filhos))
            i = j
        else:
            blocos.append((ln, None))
            i += 1

    feitos, resto = [], []
    for topo, filhos in blocos:
        if filhos is None:                       # header de grupo, linha em branco
            if topo.strip() != HEADER.strip():
                resto.append(topo)
            continue
        concluido = re.match(r"^> - \[x\] ", topo) is not None
        filho_aberto = any("- [ ] " in f for f in filhos)
        if concluido and filho_aberto:
            # gate: pai fechada com defeito aberto é estado inconsistente
            rid = re.search(r"SGV-?\d+", topo)
            avisos.append(f"⚠️ {rid.group(0) if rid else 'task'} marcada como concluída com "
                          f"defeito filho ainda aberto — resolver o defeito antes de fechar a pai "
                          f"(gate do PADROES_QA), ou registrar a exceção no card")
            resto.extend([topo] + filhos)        # fica onde está, visível
        elif concluido:
            feitos.extend([topo] + filhos)       # pai e filhos descem juntos
        else:
            resto.extend([topo] + filhos)

    if not feitos:
        return texto

    # idempotência: se os concluídos já estão todos no fim, sob o header, sai
    idx = next((i for i, l in enumerate(linhas) if l.strip() == HEADER.strip()), None)
    if idx is not None:
        depois = [l for l in linhas[idx + 1:] if re.match(r"^>(?: +)?- \[.\] ", l)]
        if depois and len(depois) == len(feitos):
            return texto

    # descarta header de categoria que ficou órfão (só tinha itens concluídos)
    limpo = []
    for i, ln in enumerate(resto):
        if re.match(r"^> \*\*.+\*\*$", ln):
            prox = next((s for s in resto[i + 1:] if s.strip() not in ("", ">")), None)
            if prox is None or re.match(r"^> \*\*.+\*\*$", prox):
                continue
        limpo.append(ln)

    bloco = (m.group(1) + "\n".join(limpo).rstrip("\n")
             + "\n>\n" + HEADER + "\n" + "\n".join(feitos) + "\n")
    acoes.append(f"fila: {len(feitos)} concluído(s) agrupado(s) em '✅ Concluídos hoje'")
    return texto.replace(m.group(0), bloco)


EVIDENCIAS = os.path.join(WS, "Evidências")
# ambiente do card -> subpasta de Evidências (tabela do Evidências/README)
EVID_PASTA = {
    "DEV": "Desenvolvimento",
    "HML": "Homologação",
    "HOTFIX": "Hotfix",
    "PROD": "Produção",
}
EVID_EXTS = (".mp4", ".mov", ".mkv", ".webm", ".gif", ".png", ".jpg", ".jpeg")


def _slug_titulo(card):
    """Descrição curta pro nome do arquivo, a partir do H1 do card.
    Sem acento/pontuação, minúsculo — igual ao padrão já usado à mão em
    `Evidências/` (ex.: '9405 - link e qr code alinhados ...')."""
    m = re.search(r"^# (.+)$", ler(card), re.M)
    t = (m.group(1) if m else os.path.basename(card)).lower()
    t = re.sub(r"^\[[^\]]*\]\s*", "", t)          # tira prefixo tipo "[melhoria-cx]"
    for a, b in (("á", "a"), ("â", "a"), ("ã", "a"), ("à", "a"), ("é", "e"),
                 ("ê", "e"), ("í", "i"), ("ó", "o"), ("ô", "o"), ("õ", "o"),
                 ("ú", "u"), ("ü", "u"), ("ç", "c")):
        t = t.replace(a, b)
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    t = re.sub(r"\s+", " ", t).strip()
    if len(t) <= 55:
        return t
    return t[:55].rsplit(" ", 1)[0]  # corta em palavra inteira, não no meio


def roteia_evidencias():
    """Fluxo 5 (gravar → renomear → mover → embedar), na parte mecânica.

    O QA grava com o OBS já nomeando o arquivo com o número do card
    (`9405.mp4`) — é o único dado que o script precisa. A partir dele:
    renomeia pro padrão `<num> - <descrição>.mp4`, move pra subpasta do
    ambiente do card e insere o embed na seção `### Evidências` se faltar.

    Deliberadamente conservador: arquivo cujo nome NÃO começa com número de
    card não é tocado — vira aviso. Adivinhar destino de gravação sem
    identificação é como evidência se perde.
    """
    if not os.path.isdir(EVIDENCIAS):
        return
    for nome in sorted(os.listdir(EVIDENCIAS)):
        origem = os.path.join(EVIDENCIAS, nome)
        if not os.path.isfile(origem):
            continue
        base, ext = os.path.splitext(nome)
        if ext.lower() not in EVID_EXTS:
            continue
        # nome de timestamp do OBS ("2026-07-28 15-11-13") NÃO é número de card —
        # sem esta guarda o ano vira "SGV-2026" e o aviso sai enganoso
        parece_data = re.match(r"^\d{4}-\d{2}-\d{2}", base.strip())
        m = None if parece_data else re.match(r"^(\d{3,6})(?:\s*-\s*(.+))?$", base.strip())
        if not m:
            avisos.append(f"evidência sem número de card na raiz, não movida: {nome} "
                          f"— renomear pra '<SGV> - <descrição>' e rodar de novo")
            continue
        num, desc = m.group(1), (m.group(2) or "").strip()
        card = achar_card(num)
        if not card:
            avisos.append(f"evidência {nome}: card do SGV-{num} não existe ainda "
                          f"(criar card e rodar de novo)")
            continue
        t = ler(card)
        amb = (re.search(r"^ambiente: *(\S+)", t, re.M) or [None, ""])[1].upper()
        tem_task = bool((re.search(r'^task: *"?(\d+)', t, re.M)))
        sub = EVID_PASTA.get(amb) if tem_task else "Cadastrar"
        if not sub:
            avisos.append(f"evidência {nome}: ambiente '{amb or '—'}' do card não "
                          f"mapeia pra subpasta — mover à mão")
            continue
        # nome final: preserva descrição existente; senão usa o título do card
        final = f"{num} - {desc or _slug_titulo(card)}{ext}"
        destino_dir = os.path.join(EVIDENCIAS, sub)
        os.makedirs(destino_dir, exist_ok=True)
        destino = os.path.join(destino_dir, final)
        if os.path.exists(destino):
            avisos.append(f"evidência {nome}: já existe {sub}/{final} — resolver à mão")
            continue
        os.rename(origem, destino)
        acoes.append(f"evidência: {nome} → {sub}/{final}")
        # embed na seção de Evidências do card, se ainda não estiver lá
        if f"![[{final}]]" not in t:
            novo, ok = re.subn(r"(### Evidências[^\n]*\n)", rf"\g<1>\n![[{final}]]\n",
                               t, count=1)
            if ok:
                gravar(card, novo)
                acoes.append(f"evidência embedada no card do SGV-{num}")
            else:
                avisos.append(f"evidência {final} movida, mas o card do SGV-{num} "
                              f"não tem seção '### Evidências' — embedar à mão")


def sem_idade(s):
    """Texto do item sem a marca de idade — base de comparação do carry-over.
    Sem isso, envelhecer '🕐 10d' -> '🕐 11d' faz o item deixar de casar com a
    versão já presente na daily e ele entra duplicado (itens sem SGV/MEL não
    têm o dedup por ID como rede)."""
    return re.sub(r"\s*🕐\s*\d+d(?:\s*(?:⚠️|🚨))?", "", s).strip()


def sem_ledger(s):
    """Texto do item sem a marca de conclusão do ledger.

    `ledger_do_dia` fecha uma pendência escrevendo '<item> → registrado', e a
    convenção do 01 Daily/README permite anotar entre parênteses o que foi
    feito ('- [x] SGV-XXXX - Refinar (card criado) → registrado'). Sem tirar os
    dois na comparação, o item anotado não casa com a versão carregada de
    ontem e **volta como pendência nova** — a fila foi de 41 pra 42 em 30/07
    por isso. É a mesma cegueira do bug de idade, com outro gatilho, e só
    morde item **sem SGV/MEL**, que não tem o dedup por ID como rede.

    O parêntese só é descartado quando acompanhado do '→ registrado': muitas
    pendências legítimas terminam em parêntese que faz parte da identidade
    delas ('Validar em HML (aprovada em DEV, segue pra homologação)'), e
    cortá-lo sempre faria pendências distintas colidirem — aí o defeito
    deixaria de duplicar e passaria a **engolir** item, que é pior.
    """
    return re.sub(r"\s*(?:\([^()]*\))?\s*→\s*registrado\s*$", "", s).strip()


def envelhece_fila(itens, dias):
    """Incrementa a idade dos itens herdados no carry-over e reaplica os
    limiares do AGENTE_FILA: 1-2d sem marca · 3-4d '🕐 Nd' · 5-6d '🕐 Nd ⚠️'
    · 7d+ '🕐 Nd 🚨'.

    `dias` é a diferença REAL de datas entre a daily anterior e hoje — nunca um
    +1 fixo: um fim de semana sem daily vale +3 (precedente de 27/07, quando a
    sexta 24/07 emendou na segunda 27/07). Item que chega sem marca de idade é
    tratado como tendo 1 dia de fila.
    """
    def marca(n):
        if n >= 7:
            return f" 🕐 {n}d 🚨"
        if n >= 5:
            return f" 🕐 {n}d ⚠️"
        if n >= 3:
            return f" 🕐 {n}d"
        return ""

    saida, envelhecidos, zumbis = [], 0, []
    for item in itens:
        m = re.search(r"🕐\s*(\d+)d", item)
        novo = (int(m.group(1)) if m else 1) + dias
        limpo = re.sub(r"\s*🕐\s*\d+d(?:\s*(?:⚠️|🚨))?", "", item)
        # a marca de idade vive antes de eventual bloqueio ⏳ — leitura estável
        bm = re.search(r"\s(⏳.*)$", limpo)
        if bm:
            novo_item = limpo[: bm.start()] + marca(novo) + " " + bm.group(1)
        else:
            novo_item = limpo + marca(novo)
        novo_item = novo_item.strip()
        if novo >= 7 and (int(m.group(1)) if m else 1) < 7:
            zumbis.append(novo_item[:45])
        if marca(novo):
            envelhecidos += 1
        saida.append(novo_item)
    if envelhecidos:
        acoes.append(f"fila: idade recalculada (+{dias}d) em {envelhecidos} item(ns)")
    for z in zumbis:
        avisos.append(f"🚨 cruzou 7 dias de fila hoje: {z}")
    return saida


def linkifica_ids(texto):
    """Regra de links estendida: numeração citada em linha de fila (A fazer,
    Pendências, Pendente para amanhã) vira wikilink quando o card existe.
    Conservador: só toca linha sem nenhum [[link]] (evita corromper paths).

    Aceita também a **linha aninhada** do defeito (`>     - [ ] ↳ SGV-...`),
    senão o filho seria o único item da fila sem link clicável."""
    saida = []
    for ln in texto.split("\n"):
        if re.match(r"^>? *- ", ln) and "[[" not in ln:
            for tok in set(re.findall(r"SGV-?\d+|MEL-\d{4}", ln)):
                rid = norm_id(tok)
                num = rid.split("-", 1)[1]
                card = None
                if rid.startswith("SGV"):
                    card = achar_card(num)
                else:
                    for p in glob.glob(os.path.join(DEMANDAS, "**", f"MEL-{num} - *.md"), recursive=True):
                        card = p
                if card:
                    ln = ln.replace(tok, link(card, rid))
        saida.append(ln)
    return "\n".join(saida)


def bloco_registro(daily, hoje):
    """Anexa ao callout de Auto-organização o que aconteceu nesta execução.

    **Não repete linha que já está no bloco.** Aviso pendente (evidência sem
    número na raiz, card que falta criar) sai igual em toda execução — sem esta
    guarda, o bloco cresce uma linha por rodada do 🔄 e engole a daily: em
    30/07 chegou a **75 linhas com 25 únicas**, o mesmo aviso 25 vezes, porque
    o dia teve muitas execuções.

    Ação nova continua sendo registrada; o que se descarta é a **repetição
    literal**. Mesmo princípio de `sem_idade` e `sem_ledger`: o script tem que
    reconhecer o próprio trabalho anterior em vez de reescrevê-lo.
    """
    if not acoes and not avisos:
        return daily
    ja_registrado = set()
    m = re.search(r"> \[!organizacao\]- Auto-organização\n((?:>.*\n?)*)", daily)
    if m:
        ja_registrado = {l.rstrip() for l in m.group(1).splitlines() if l.startswith("> - ")}
    linhas_bloco = [f"> - {a}" for a in acoes] + [f"> - {a}" for a in avisos]
    novas = []
    for l in linhas_bloco:
        if l in ja_registrado or l in novas:
            continue
        novas.append(l)
    if not novas:
        return daily
    corpo = "\n".join(novas)
    if "[!organizacao]- Auto-organização" in daily:
        return daily.rstrip() + "\n" + corpo + "\n"
    return daily.rstrip() + f"\n\n> [!organizacao]- Auto-organização\n{corpo}\n"


def main():
    hoje = datetime.date.today()
    anteriores = dailies_anteriores(hoje)
    ontem = anteriores[-1] if anteriores else None
    hoje_p = daily_path(hoje)

    pendentes_ontem = itens_nao_finalizados(ler(ontem[1])) if ontem else []
    # intervalo REAL entre as duas dailies: fim de semana/feriado sem daily vale
    # mais de 1 dia. Envelhecer só o que de fato entra na daily de hoje — nunca
    # antes do dedup, senão a marca nova impede o item de casar com o já presente.
    dias = (hoje - ontem[0]).days if ontem else 0

    if not os.path.exists(hoje_p):
        os.makedirs(os.path.dirname(hoje_p), exist_ok=True)
        itens = envelhece_fila(pendentes_ontem, dias) if pendentes_ontem else []
        gravar(hoje_p, template_daily(hoje, ontem[0] if ontem else None, itens))
        acoes.append(f"daily de hoje criada ({len(itens)} pendência(s) carregada(s))")
    else:
        # carry-over pra daily já existente, sem duplicar (por texto exato ou por SGV/MEL)
        d = ler(hoje_p)
        existentes = re.findall(r"^>? ?- \[.\] (.+)$", d, re.M)
        existentes_norm = {sem_idade(sem_ledger(e)) for e in existentes}
        ids_hoje = set()
        for e in existentes:
            ids_hoje |= ids_de(e)
        novos = []
        for item in pendentes_ontem:
            if sem_idade(sem_ledger(item)) in existentes_norm:
                continue
            if ids_de(item) & ids_hoje:
                continue
            novos.append(item)
        novos = envelhece_fila(novos, dias) if novos else []
        if novos:
            call_novo = "\n".join(f"> - {i}" for i in novos)
            afazer_novo = "\n".join(f"> - [ ] {i}" for i in novos)
            d = re.sub(r"(> \[!info\][^\n]*\n)", rf"\g<1>{call_novo}\n", d, count=1)
            d = re.sub(r"(> \*\*A fazer hoje:\*\*\n)", rf"\g<1>{afazer_novo}\n", d, count=1)
            gravar(hoje_p, d)
            acoes.append(f"{len(novos)} pendência(s) de ontem carregada(s) pro A fazer hoje")

    roteia_evidencias()
    d = processa_continuacoes(ler(hoje_p), hoje)
    reconcilia_atividades(d, hoje)
    d = sincroniza_demandas_ativas(d)
    d = ledger_do_dia(d)
    d = coleta_concluidos(d)
    d = linkifica_ids(d)
    d = bloco_registro(d, hoje)
    gravar(hoje_p, d)

    partes = []
    if acoes:
        partes.append(f"{len(acoes)} ação(ões)")
    if avisos:
        partes.append(f"{len(avisos)} aviso(s) — precisam de você")
    if partes:
        # ⚠️ na frente quando há aviso: "nada a fazer" e "não entendi X linhas"
        # não podem sair com a mesma cara.
        print(("⚠️ " if avisos else "✅ ") + ", ".join(partes))
    else:
        print("✅ nada a fazer — tudo em dia")
    for a in acoes:
        print("  •", a)
    for a in avisos:
        print("  •", a)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"❌ erro: {e}")
        sys.exit(1)
