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

## Pendências de ontem
> [!info]- Carregado de {origem}
{call}

> **A fazer hoje:**
{afazer}

## Atividades

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
-

## Pendente para amanhã
- [ ]
"""


def itens_nao_finalizados(texto):
    """Itens '- [ ]' do A fazer hoje (callout) e do Pendente para amanhã, sem vazios."""
    out = []
    for m in re.finditer(r"^>? ?- \[ \] (.+)$", texto, re.M):
        item = m.group(1).strip()
        if item:
            out.append(item)
    return out


def ids_de(texto):
    return set(re.findall(r"SGV-?\d+|MEL-\d{4}", texto))


def tipo_do_card(texto_card):
    """Bug é o padrão (sem prefixo na frase); outros tipos prefixam."""
    if re.search(r"^tags:\n(?:  - .*\n)*  - bug", texto_card, re.M) or "\n  - bug\n" in texto_card:
        return ""
    m = re.search(r"\*\*Tipo:\*\* *(\w+)", texto_card)
    if m:
        return m.group(1).capitalize() + " "
    if re.search(r'^mel:', texto_card, re.M):
        return "Melhoria "
    return "Demanda "


def achar_card(num):
    for base in (DEMANDAS, os.path.join(WS, "99 Arquivo")):
        for p in glob.glob(os.path.join(base, "**", "*.md"), recursive=True):
            if os.path.basename(p).startswith(f"{num} - "):
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


def sincroniza_demandas_ativas(texto):
    """Invariante da fila viva: TODO card em aberto (02 Demandas fora de
    Concluídas) tem um item ativo em 'A fazer hoje' — vale pra qualquer
    estágio (a refinar, refinada, cadastrada, em validação, reaberta).
    Se a pendência está em 'Pendente para amanhã', move pra cima;
    se não existe, cria o próximo passo padrão."""
    cards = []
    for pasta in ("DEV", "HML", "Hotfix", "POCs"):
        cards += glob.glob(os.path.join(DEMANDAS, pasta, "*.md"))
    for card in sorted(cards):
        base = os.path.splitext(os.path.basename(card))[0]
        tcard = ler(card)
        task = re.search(r'^task: *"?(\d+)"?\s*$', tcard, re.M)
        melm = re.search(r"MEL-(\d{4})", base)
        if task:
            rid = f"SGV-{task.group(1)}"
        elif melm:
            rid = f"MEL-{melm.group(1)}"
        else:
            continue  # card sem identificador — fora do radar automático
        titulo = base.split(" - ", 1)[1] if " - " in base else base
        afazer = re.findall(r"^> - \[ \] (.+)$", texto, re.M)
        if any(rid in norm_id(a) for a in afazer):
            continue
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
                avisos.append(f"⚠️ card do SGV-{num} não encontrado")
                continue
            t = ler(card)
            amb = (re.search(r"^ambiente: *(\S+)", t, re.M) or [None, "HML"])[1].upper()
            amb_nome = AMB_NOME.get(amb, amb.lower())
            ja_reaberta = "🔴" in t
            secao = "DEV" if amb == "DEV" else "HML"
            tipo = tipo_do_card(t)
            if chave.startswith("aprovada"):
                # ambiente explícito na anotação vence a pasta do card (fast-forward)
                if amb == "DEV" and re.search(r"em (homolog|hotfix)", chave):
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


LEDGER = [
    ("💭", ("propor", "proposta", "suspeita"), "{rid} - Propor (proposta registrada)"),
    ("📝", ("refinar",), "{rid} - Refinar (card criado, critérios prontos)"),
    ("📤", ("notion",), "{rid} - Atualizar no Notion (análise/critérios registrados)"),
    ("💡", ("cadastrar",), "{rid} - Cadastrar no Notion (feito)"),
    ("🐛", ("cadastrar", "card do bug", "confirmad"), "{rid} - Cadastrar (feito)"),
    ("🗑️", ("descartar", "investigar", "suspeita"), "{rid} - Descartar (feito)"),
    ("✅", ("valida", "retest", "revalida", "test", "revis", "companhar"), "{rid} - Validar (aprovada)"),
    ("🔁", ("valida", "retest", "revalida", "test", "companhar"), "{rid} - Retestar (aprovada)"),
    ("🔴", ("valida", "retest", "revalida", "test", "companhar"), "{rid} - Retestar (reprovada)"),
    ("⚪", ("valida", "retest", "revalida", "test", "companhar"), "{rid} - Retestar (não reproduzido)"),
]


def ledger_do_dia(texto):
    """A fazer hoje = ledger completo do dia: todo estágio executado (linha em
    Atividades) aparece também como item MARCADO na fila, com o que foi feito —
    mesmo que a tarefa nunca tenha sido enfileirada antes."""
    m = re.search(r"## Atividades\n(.*?)\n## ", texto, re.S)
    if not m:
        return texto
    afazer = re.findall(r"^> - \[.\] (.+)$", texto, re.M)
    for ln in m.group(1).split("\n"):
        am = re.match(r"^- (💭|📝|📤|💡|🐛|🗑️|✅|🔁|🔴|⚪) (.+)$", ln)
        if not am:
            continue
        emoji, resto = am.group(1), am.group(2)
        idm = re.search(r"SGV[- ]?\d+|MEL-\d{4}", resto)
        rid = norm_id(idm.group(0)).replace("SGV ", "SGV-") if idm else None
        chave = rid if rid else resto.split(":")[-1].split("(")[0].strip()[:25]
        for e2, kws, modelo in LEDGER:
            if e2 != emoji:
                continue
            coberto = any(
                (chave.lower() in norm_id(a).lower()) and any(k in a.lower() for k in kws)
                for a in afazer)
            if coberto:
                break
            item = modelo.format(rid=rid) if rid else f"Registrar: {chave} (feito)"
            texto = re.sub(r"(> \*\*A fazer hoje:\*\*\n)",
                           rf"\g<1>> - [x] {item} → registrado\n", texto, count=1)
            afazer.append(item)
            acoes.append(f"ledger: [x] {item[:55]}")
            break
    return texto


def linkifica_ids(texto):
    """Regra de links estendida: numeração citada em linha de fila (A fazer,
    Pendências, Pendente para amanhã) vira wikilink quando o card existe.
    Conservador: só toca linha sem nenhum [[link]] (evita corromper paths)."""
    saida = []
    for ln in texto.split("\n"):
        if re.match(r"^>? ?- ", ln) and "[[" not in ln:
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
    if not acoes and not avisos:
        return daily
    linhas_bloco = [f"> - {a}" for a in acoes] + [f"> - {a}" for a in avisos]
    corpo = "\n".join(linhas_bloco)
    if "[!organizacao]- Auto-organização" in daily:
        return daily.rstrip() + "\n" + corpo + "\n"
    return daily.rstrip() + f"\n\n> [!organizacao]- Auto-organização\n{corpo}\n"


def main():
    hoje = datetime.date.today()
    anteriores = dailies_anteriores(hoje)
    ontem = anteriores[-1] if anteriores else None
    hoje_p = daily_path(hoje)

    pendentes_ontem = itens_nao_finalizados(ler(ontem[1])) if ontem else []

    if not os.path.exists(hoje_p):
        os.makedirs(os.path.dirname(hoje_p), exist_ok=True)
        gravar(hoje_p, template_daily(hoje, ontem[0] if ontem else None, pendentes_ontem))
        acoes.append(f"daily de hoje criada ({len(pendentes_ontem)} pendência(s) carregada(s))")
    else:
        # carry-over pra daily já existente, sem duplicar (por texto exato ou por SGV/MEL)
        d = ler(hoje_p)
        existentes = re.findall(r"^>? ?- \[.\] (.+)$", d, re.M)
        ids_hoje = set()
        for e in existentes:
            ids_hoje |= ids_de(e)
        novos = []
        for item in pendentes_ontem:
            if any(item == e for e in existentes):
                continue
            if ids_de(item) & ids_hoje:
                continue
            novos.append(item)
        if novos:
            call_novo = "\n".join(f"> - {i}" for i in novos)
            afazer_novo = "\n".join(f"> - [ ] {i}" for i in novos)
            d = re.sub(r"(> \[!info\][^\n]*\n)", rf"\g<1>{call_novo}\n", d, count=1)
            d = re.sub(r"(> \*\*A fazer hoje:\*\*\n)", rf"\g<1>{afazer_novo}\n", d, count=1)
            gravar(hoje_p, d)
            acoes.append(f"{len(novos)} pendência(s) de ontem carregada(s) pro A fazer hoje")

    d = processa_continuacoes(ler(hoje_p), hoje)
    reconcilia_atividades(d, hoje)
    d = sincroniza_demandas_ativas(d)
    d = ledger_do_dia(d)
    d = linkifica_ids(d)
    d = bloco_registro(d, hoje)
    gravar(hoje_p, d)

    cont = len([a for a in acoes if "→" in a])
    partes = []
    if acoes:
        partes.append(f"{len(acoes)} ação(ões)")
    if avisos:
        partes.append(f"{len(avisos)} aviso(s)")
    print("✅ " + (", ".join(partes) if partes else "nada a fazer — tudo em dia"))
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
