# Handouts

A printable reference for the 12 frameworks — for people who'd rather have a page on the desk than a skill in the terminal.

| File | What |
|---|---|
| [`executive-presence-frameworks.pdf`](executive-presence-frameworks.pdf) | The 12 frameworks, formatted for print |
| [`build_pdf.py`](build_pdf.py) | The script that generates it |

## Rebuilding

Only needed if you edit the frameworks and want a matching PDF.

```bash
pip install reportlab
python handouts/build_pdf.py
```

Writes `executive-presence-frameworks.pdf` to the current directory.

## Note on sync

The PDF is **generated from content inside `build_pdf.py`**, not from
[`references/frameworks.md`](../skills/executive-presence/references/frameworks.md).
There's no pipeline between them — editing the Markdown doesn't change the PDF,
and editing the script doesn't change the skill. If you change the frameworks,
change both.

The PDF is also a lightly expanded presentation of the same material rather than
a strict rendering of it, so expect wording differences. **The Markdown is
canonical** — it's what the skills actually read.
