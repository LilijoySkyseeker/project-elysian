#!/usr/bin/env python3
"""Build an EPUB 3 and a single Markdown file from a work's chapters, for reading on a phone, an e-reader,
a computer, or in a browser (GitHub renders the Markdown).

    python3 tools/build_ebook.py offcanon/X01_equestria            # -> library/<slug>.epub and library/<slug>.md
    python3 tools/build_ebook.py offcanon/X01_equestria --out x.epub
    nix develop -c epubcheck library/<slug>.epub                    # validate

The work folder holds a `book.json` manifest:

    {
      "slug": "x01-the-mirror",
      "title": "The Mirror", "subtitle": "…", "author": "Project Elysian",
      "language": "en",
      "description": "…",
      "chapters": [ {"file": "chapters/CH01.md", "title": "The Mirror"}, … ]
    }

What it understands in a chapter file (the house Markdown, nothing more):
- a header block ending at the first line that is exactly `---`, skipped (title and POV lines);
- paragraphs separated by blank lines; `---` on its own line is a scene break;
- `*italic*`, `**bold**`, and Kin-code `*[words ~ rider]*` (which is italic);
- `# Heading` lines;
- an image on a line of its own: `![caption](images/file.png)`. It is embedded if the file exists
  (path relative to the work folder); otherwise it is skipped with a warning. The caption is optional
  and is shown small under the picture (DOC-00I: inline spot illustrations);
- `<!-- doc -->` … `<!-- /doc -->`: an in-world document (a ledger, a tab), set in its own block with
  line breaks and spacing kept;
- other HTML comments (`<!-- fig: … -->` placement notes) are dropped.

Standard library only. The zip is written with fixed timestamps so an unchanged book rebuilds byte-identical,
except for the dcterms:modified date, which is taken from book.json ("modified") if given.
"""
from __future__ import annotations

import argparse
import datetime as dt
import html
import json
import re
import sys
import uuid
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
FIXED_TIME = (2020, 1, 1, 0, 0, 0)

CSS = """
body { font-family: serif; line-height: 1.45; margin: 0 0.4em; }
h1.book { text-align: center; margin-top: 30%; font-size: 1.8em; }
p.subtitle { text-align: center; font-style: italic; }
p.author { text-align: center; margin-top: 2em; }
h2.chapter { text-align: center; margin: 2em 0 1.5em; font-size: 1.3em; }
h2.chapter span.num { display: block; font-size: 0.75em; font-weight: normal; letter-spacing: 0.1em; }
p { margin: 0; text-indent: 1.3em; }
p.first, h3 + p { text-indent: 0; }
hr.break { border: none; text-align: center; margin: 1.2em 0; height: 1em; }
hr.break::after { content: "\\2042"; }
div.doc { font-family: monospace; font-size: 0.85em; white-space: pre-wrap; margin: 1em 0.5em; line-height: 1.35; }
figure.spot { margin: 1em auto; text-align: center; page-break-inside: avoid; }
figure.spot img { max-width: 60%; max-height: 14em; }
figure.spot figcaption { font-size: 0.8em; font-style: italic; margin-top: 0.3em; }
""".strip()


def inline(text: str) -> str:
    t = html.escape(text, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", t)
    return t


def strip_header(lines: list[str]) -> list[str]:
    for i, ln in enumerate(lines[:12]):
        if ln.strip() == "---":
            return lines[i + 1:]
    return lines


def blocks(lines: list[str]):
    """Yield (kind, payload) in reading order."""
    buf: list[str] = []
    doc: list[str] | None = None
    for raw in lines + [""]:
        ln = raw.rstrip("\n")
        if doc is not None:
            if ln.strip() == "<!-- /doc -->":
                yield "doc", doc
                doc = None
            else:
                doc.append(ln)
            continue
        if ln.strip() == "<!-- doc -->":
            if buf:
                yield "para", buf
                buf = []
            doc = []
            continue
        if ln.strip() == "":
            if buf:
                yield "para", buf
                buf = []
            continue
        buf.append(ln)
    if doc is not None:
        yield "doc", doc


def render_chapter(path: Path, work: Path, n: int, title: str, images: dict[str, Path], warn) -> str:
    lines = strip_header(path.read_text(encoding="utf-8").splitlines())
    out = [f'<h2 class="chapter"><span class="num">{n}</span>{html.escape(title)}</h2>']
    first = True
    for kind, payload in blocks(lines):
        if kind == "doc":
            body = "\n".join(inline(l) for l in payload).strip("\n")
            out.append(f'<div class="doc">{body}</div>')
            first = True
            continue
        text = " ".join(l.strip() for l in payload)
        text = re.sub(r"<!--.*?-->", "", text).strip()
        if not text:
            continue
        if text == "---":
            out.append('<hr class="break"/>')
            first = True
            continue
        m = re.fullmatch(r"!\[(.*?)\]\((.+?)\)", text)
        if m:
            cap, src = m.group(1), m.group(2)
            f = (work / src).resolve()
            if f.exists():
                name = f"img/{len(images) + 1:03d}{f.suffix.lower()}"
                images[name] = f
                capt = f"<figcaption>{inline(cap)}</figcaption>" if cap else ""
                out.append(f'<figure class="spot"><img src="{name}" alt="{html.escape(cap or "illustration")}"/>{capt}</figure>')
            else:
                warn(f"{path.name}: image not found, skipped: {src}")
            continue
        if text.startswith("#"):
            out.append(f"<h3>{inline(text.lstrip('#').strip())}</h3>")
            first = True
            continue
        cls = ' class="first"' if first else ""
        out.append(f"<p{cls}>{inline(text)}</p>")
        first = False
    return "\n".join(out)


def render_markdown(meta: dict, work: Path, outdir: Path) -> str:
    """The whole book as one Markdown file: title, contents, chapters. Headers are stripped; doc blocks are
    fenced so their spacing survives; image paths are rewritten relative to the output folder."""
    import os
    title = meta["title"]
    out = [f"# {title}", ""]
    if meta.get("subtitle"):
        out += [f"*{meta['subtitle'].replace('*', '')}*", ""]
    if meta.get("author"):
        out += [meta["author"], ""]
    anchors = []
    for i, ch in enumerate(meta["chapters"], 1):
        a = re.sub(r"[^a-z0-9 -]", "", f"{i} {ch['title']}".lower()).replace(" ", "-")
        anchors.append(a)
    out += ["## Contents", ""] + [f"{i}. [{ch['title']}](#{a})" for i, (ch, a) in enumerate(zip(meta["chapters"], anchors), 1)] + [""]
    for i, ch in enumerate(meta["chapters"], 1):
        out += ["---", "", f"## {i}. {ch['title']}", ""]
        lines = strip_header((work / ch["file"]).read_text(encoding="utf-8").splitlines())
        for kind, payload in blocks(lines):
            if kind == "doc":
                body = "\n".join(payload).replace("**", "").strip("\n")
                out += ["```text", body, "```", ""]
                continue
            text = re.sub(r"<!--.*?-->", "", " ".join(l.strip() for l in payload)).strip()
            if not text:
                continue
            if text == "---":
                out += ["<p align=\"center\">⁂</p>", ""]
                continue
            m = re.fullmatch(r"!\[(.*?)\]\((.+?)\)", text)
            if m:
                f = (work / m.group(2)).resolve()
                if f.exists():
                    out += [f"![{m.group(1)}]({os.path.relpath(f, outdir.resolve())})", ""]
                continue
            out += [text, ""]
    return "\n".join(out).rstrip("\n") + "\n"


def xhtml(title: str, body: str, lang: str) -> str:
    return f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{lang}" lang="{lang}">
<head><meta charset="utf-8"/><title>{html.escape(title)}</title><link rel="stylesheet" type="text/css" href="style.css"/></head>
<body>
{body}
</body>
</html>
"""


MEDIA = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".gif": "image/gif", ".svg": "image/svg+xml",
         ".webp": "image/webp"}


def build(work: Path, out: Path | None = None) -> Path:
    meta = json.loads((work / "book.json").read_text(encoding="utf-8"))
    lang = meta.get("language", "en")
    title = meta["title"]
    slug = meta.get("slug") or re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    book_id = "urn:uuid:" + str(uuid.uuid5(uuid.NAMESPACE_URL, "project-elysian/" + slug))
    modified = meta.get("modified") or dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    warnings: list[str] = []
    images: dict[str, Path] = {}

    files: dict[str, str | bytes] = {}
    front = [f'<h1 class="book">{html.escape(title)}</h1>']
    if meta.get("subtitle"):
        front.append(f'<p class="subtitle">{inline(meta["subtitle"])}</p>')
    if meta.get("author"):
        front.append(f'<p class="author">{html.escape(meta["author"])}</p>')
    files["title.xhtml"] = xhtml(title, "\n".join(front), lang)

    toc = []
    for i, ch in enumerate(meta["chapters"], 1):
        src = work / ch["file"]
        name = f"ch{i:02d}.xhtml"
        files[name] = xhtml(ch["title"], render_chapter(src, work, i, ch["title"], images, warnings.append), lang)
        toc.append((name, f"{i}. {ch['title']}"))

    files["style.css"] = CSS
    nav_items = "\n".join(f'<li><a href="{n}">{html.escape(t)}</a></li>' for n, t in toc)
    files["nav.xhtml"] = xhtml("Contents", f'<nav epub:type="toc" id="toc"><h2>Contents</h2><ol>\n{nav_items}\n</ol></nav>', lang)
    ncx_points = "\n".join(
        f'<navPoint id="p{i}" playOrder="{i}"><navLabel><text>{html.escape(t)}</text></navLabel><content src="{n}"/></navPoint>'
        for i, (n, t) in enumerate(toc, 1))
    files["toc.ncx"] = f"""<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head><meta name="dtb:uid" content="{book_id}"/></head>
<docTitle><text>{html.escape(title)}</text></docTitle>
<navMap>
{ncx_points}
</navMap>
</ncx>
"""
    for name, path in images.items():
        files[name] = path.read_bytes()

    manifest = ['<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
                '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
                '<item id="css" href="style.css" media-type="text/css"/>',
                '<item id="title" href="title.xhtml" media-type="application/xhtml+xml"/>']
    manifest += [f'<item id="{n[:-6]}" href="{n}" media-type="application/xhtml+xml"/>' for n, _ in toc]
    manifest += [f'<item id="img{i}" href="{n}" media-type="{MEDIA.get(Path(n).suffix, "application/octet-stream")}"/>'
                 for i, n in enumerate(images, 1)]
    spine = ['<itemref idref="title"/>', '<itemref idref="nav"/>'] + [f'<itemref idref="{n[:-6]}"/>' for n, _ in toc]
    desc = f"<dc:description>{html.escape(meta['description'])}</dc:description>" if meta.get("description") else ""
    files["content.opf"] = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="{lang}">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="bookid">{book_id}</dc:identifier>
<dc:title>{html.escape(title)}</dc:title>
<dc:language>{lang}</dc:language>
<dc:creator>{html.escape(meta.get("author", "Project Elysian"))}</dc:creator>
{desc}
<meta property="dcterms:modified">{modified}</meta>
</metadata>
<manifest>
{chr(10).join(manifest)}
</manifest>
<spine toc="ncx">
{chr(10).join(spine)}
</spine>
</package>
"""
    out = out or (REPO / "library" / f"{slug}.epub")
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, "w") as z:
        def put(name: str, data, compress=zipfile.ZIP_DEFLATED):
            info = zipfile.ZipInfo(name, FIXED_TIME)
            info.compress_type = compress
            z.writestr(info, data)
        put("mimetype", "application/epub+zip", zipfile.ZIP_STORED)
        put("META-INF/container.xml", """<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>
""")
        for name, data in files.items():
            put("OEBPS/" + name, data)
    md = out.with_suffix(".md")
    md.write_text(render_markdown(meta, work, out.parent), encoding="utf-8")
    for w in warnings:
        print("warning:", w, file=sys.stderr)
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("work", help="the work's folder (holds book.json)")
    ap.add_argument("--out", help="output path (default library/<slug>.epub)")
    a = ap.parse_args(argv)
    out = build(Path(a.work), Path(a.out) if a.out else None)
    print(f"wrote {out} and {out.with_suffix('.md')}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
