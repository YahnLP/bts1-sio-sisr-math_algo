#!/usr/bin/env python3
"""Assemble docs/ressources/formulaire.md à partir des aide-mémoire de chaque séance."""
import pathlib, re
root = pathlib.Path(__file__).resolve().parent.parent
memos = sorted(root.glob("docs/phase-*/S*/04-aide-memoire.md"))
out = ["# Formulaire", "",
"Tous les aide-mémoire du cours réunis sur une seule page, dans l'ordre des séances. Utilise la recherche ou le sommaire à droite pour retrouver une formule.", "",
"> [!NOTE]", "> Chaque formule a été vérifiée par le calcul sur des exemples. Pour l'épreuve, vérifie dans le sujet ce qui est rappelé et ce qui est à connaître.", ""]
for p in memos:
    sid = p.parent.name.split("-")[0]
    txt = p.read_text(encoding="utf-8").splitlines()
    body, skip = [], True
    for ln in txt:
        if skip:
            if ln.startswith("## "): skip = False
            else: continue
        body.append(ln)
    title = txt[0].replace("# Aide-mémoire – ", "")
    out.append(f"## {sid} · {title}")
    out.append("")
    for ln in body:
        out.append(re.sub(r"^(#{2,5}) ", lambda m: "#"*(len(m.group(1))+1)+" ", ln))
    out.append("")
(root/"docs/ressources/formulaire.md").write_text("\n".join(out)+"\n", encoding="utf-8")
print(len(memos), "aide-mémoire")
