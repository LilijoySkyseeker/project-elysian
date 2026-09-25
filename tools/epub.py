#!/usr/bin/env python3
"""epub.py — build an EPUB 3 ebook from one or more Project Elysian prose files.

Standard library only.

    python3 tools/epub.py --title "Guest Slot" --author "Project Elysian" \
        --out ebooks/S026_guest_slot.epub scenes/drafts/S026_guest_slot.md

Each input file becomes one chapter. Its prose is everything after the first
`---` line that follows the header block, stopping at a `## Canon` / `## Offers`
appendix if there is one. Markdown handled: paragraphs, *italic*, **bold**, and
`---` as a section break. Everything else passes through as text.

Check the result with `epubcheck <file>` (pip install epubcheck; needs Java).
"""
import argparse, datetime, html, re, uuid, zipfile
from pathlib import Path

CSS = """\
body { margin: 0 5%; font-family: serif; line-height: 1.45; }
h1 { font-size: 1.6em; text-align: center; margin: 3em 0 0.4em; font-weight: normal; }
h2 { font-size: 1.2em; text-align: center; margin: 2em 0 1.5em; font-weight: normal; }
p { margin: 0; text-indent: 1.3em; text-align: left; }
p.first, hr + p { text-indent: 0; }
hr { border: 0; text-align: center; margin: 1.2em 0; height: 1.2em; }
hr::after { content: "\\2022\\2003\\2022\\2003\\2022"; }
.title-page { text-align: center; }
.title-page p { text-indent: 0; text-align: center; }
.byline { margin-top: 1em; font-style: italic; }
.note { margin-top: 3em; font-size: 0.85em; }
"""


def prose_of(text):
    lines = text.splitlines()
    # Skip the header block: the title line, bold metadata lines, and the first --- rule.
    start = 0
    if lines and lines[0].startswith('#'):
        for i, line in enumerate(lines):
            if line.strip() == '---':
                start = i + 1
                break
    body = []
    for line in lines[start:]:
        if re.match(r'^##\s+(Canon|Offers)', line):
            break
        body.append(line)
    return '\n'.join(body).strip()


def inline(s):
    s = html.escape(s, quote=False)
    s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
    s = re.sub(r'(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])', r'<em>\1</em>', s)
    return s


def to_xhtml_body(prose):
    out, first = [], True
    for block in re.split(r'\n\s*\n', prose):
        block = block.strip()
        if not block:
            continue
        if block == '---':
            out.append('<hr/>')
            continue
        para = ' '.join(l.strip() for l in block.splitlines())
        cls = ' class="first"' if first else ''
        out.append(f'<p{cls}>{inline(para)}</p>')
        first = False
    return '\n'.join(out)


def page(title, body, lang):
    return f"""<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xmlns:epub="http://www.idpf.org/2007/ops" xml:lang="{lang}" lang="{lang}">
<head><meta charset="utf-8"/><title>{html.escape(title)}</title><link rel="stylesheet" type="text/css" href="style.css"/></head>
<body>
{body}
</body>
</html>
"""


def build(args):
    lang = args.lang
    book_id = f'urn:uuid:{uuid.uuid5(uuid.NAMESPACE_URL, "project-elysian/" + args.title)}'
    modified = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    chapters = []
    for n, path in enumerate(args.files, 1):
        text = Path(path).read_text(encoding='utf-8')
        heading = args.chapter_titles[n - 1] if args.chapter_titles else (args.title if len(args.files) == 1 else f'{n}')
        body = f'<section epub:type="chapter"><h2>{html.escape(heading)}</h2>\n{to_xhtml_body(prose_of(text))}\n</section>'
        chapters.append((f'ch{n:02d}.xhtml', heading, page(heading, body, lang)))

    note = f'<p class="note">{inline(args.note)}</p>' if args.note else ''
    title_body = (f'<section epub:type="titlepage" class="title-page"><h1>{html.escape(args.title)}</h1>'
                  f'<p class="byline">{html.escape(args.author)}</p>{note}</section>')
    nav_items = '\n'.join(f'<li><a href="{f}">{html.escape(h)}</a></li>' for f, h, _ in chapters)
    nav_body = f'<nav epub:type="toc" id="toc"><h2>Contents</h2><ol>\n{nav_items}\n</ol></nav>'

    manifest = ['<item id="css" href="style.css" media-type="text/css"/>',
                '<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
                '<item id="title" href="title.xhtml" media-type="application/xhtml+xml"/>']
    spine = ['<itemref idref="title"/>']
    for f, _, _ in chapters:
        cid = f.split('.')[0]
        manifest.append(f'<item id="{cid}" href="{f}" media-type="application/xhtml+xml"/>')
        spine.append(f'<itemref idref="{cid}"/>')
    opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="bookid" xml:lang="{lang}">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="bookid">{book_id}</dc:identifier>
<dc:title>{html.escape(args.title)}</dc:title>
<dc:creator>{html.escape(args.author)}</dc:creator>
<dc:language>{lang}</dc:language>
<meta property="dcterms:modified">{modified}</meta>
</metadata>
<manifest>
{chr(10).join(manifest)}
</manifest>
<spine>
{chr(10).join(spine)}
</spine>
</package>
"""
    container = """<?xml version="1.0" encoding="utf-8"?>
<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">
<rootfiles><rootfile full-path="OEBPS/content.opf" media-type="application/oebps-package+xml"/></rootfiles>
</container>
"""
    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(out, 'w') as z:
        z.writestr(zipfile.ZipInfo('mimetype'), 'application/epub+zip', compress_type=zipfile.ZIP_STORED)
        z.writestr('META-INF/container.xml', container, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr('OEBPS/content.opf', opf, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr('OEBPS/style.css', CSS, compress_type=zipfile.ZIP_DEFLATED)
        z.writestr('OEBPS/nav.xhtml', page('Contents', nav_body, lang), compress_type=zipfile.ZIP_DEFLATED)
        z.writestr('OEBPS/title.xhtml', page(args.title, title_body, lang), compress_type=zipfile.ZIP_DEFLATED)
        for f, _, xhtml in chapters:
            z.writestr(f'OEBPS/{f}', xhtml, compress_type=zipfile.ZIP_DEFLATED)
    print(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('files', nargs='+', help='prose files, one chapter each, in order')
    ap.add_argument('--title', required=True)
    ap.add_argument('--author', default='Project Elysian')
    ap.add_argument('--out', required=True)
    ap.add_argument('--lang', default='en-GB')
    ap.add_argument('--note', default='', help='a line for the title page (markdown italics allowed)')
    ap.add_argument('--chapter-titles', nargs='*', help='one heading per file')
    build(ap.parse_args())


if __name__ == '__main__':
    main()
