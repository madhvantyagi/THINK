#!/usr/bin/env python3
"""Convert one startup-research Markdown file into a styled standalone HTML file."""

from __future__ import annotations

import argparse
import html
import re
from datetime import datetime
from pathlib import Path

import markdown


HTML_TEMPLATE = """<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <style>
    :root {{
      --paper: #fffef8;
      --canvas: #f1eee4;
      --ink: #24231f;
      --muted: #716d61;
      --green: #354f3f;
      --green-soft: #667b69;
      --rust: #8a5138;
      --rule: #d8d1bf;
      --wash: #f5f0e3;
    }}
    * {{ box-sizing: border-box; }}
    html {{ scroll-behavior: smooth; }}
    body {{
      margin: 0;
      color: var(--ink);
      background:
        radial-gradient(circle at 20% 0%, rgba(255,255,255,.85), transparent 34rem),
        var(--canvas);
      font: 18px/1.78 "Iowan Old Style", "Palatino Linotype", Palatino,
            "Book Antiqua", Georgia, serif;
      text-rendering: optimizeLegibility;
    }}
    .paper {{
      width: min(1040px, calc(100% - 32px));
      min-height: 100vh;
      margin: 28px auto;
      padding: clamp(34px, 7vw, 88px);
      background: var(--paper);
      border: 1px solid rgba(122, 110, 82, .22);
      box-shadow: 0 18px 60px rgba(59, 52, 37, .10);
    }}
    .masthead {{
      margin-bottom: 54px;
      padding-bottom: 26px;
      border-bottom: 3px double var(--green);
    }}
    .eyebrow {{
      margin: 0 0 8px;
      color: var(--rust);
      font: 700 11px/1.4 Arial, sans-serif;
      letter-spacing: .22em;
      text-transform: uppercase;
    }}
    h1, h2, h3, h4 {{
      color: var(--green);
      font-family: "Avenir Next", Avenir, "Helvetica Neue", Arial, sans-serif;
      line-height: 1.25;
      text-wrap: balance;
    }}
    h1 {{ margin: 0; font-size: clamp(2.15rem, 6vw, 4.2rem); letter-spacing: -.035em; }}
    h2 {{
      margin: 4rem 0 1.2rem;
      padding-bottom: .55rem;
      border-bottom: 1px solid var(--rule);
      font-size: clamp(1.6rem, 3vw, 2.15rem);
    }}
    h3 {{ margin: 2.8rem 0 .8rem; font-size: 1.35rem; color: var(--green-soft); }}
    h4 {{ margin: 2rem 0 .6rem; font-size: 1.05rem; color: var(--rust); }}
    p {{ margin: 1rem 0; }}
    a {{ color: var(--green); text-decoration-color: #9dad9f; text-underline-offset: 3px; }}
    a:hover {{ color: var(--rust); }}
    strong {{ color: #293e32; }}
    ul, ol {{ padding-left: 1.5rem; }}
    li {{ margin: .48rem 0; }}
    blockquote {{
      margin: 1.8rem 0;
      padding: .7rem 1.4rem;
      color: #4e4a40;
      background: var(--wash);
      border-left: 4px solid var(--rust);
    }}
    code {{
      padding: .12rem .35rem;
      border-radius: 3px;
      background: #eee8d8;
      color: #713e2a;
      font: .87em "SFMono-Regular", Consolas, monospace;
    }}
    pre {{
      overflow-x: auto;
      padding: 1.2rem;
      color: #f7f2e7;
      background: #29332d;
      border-radius: 5px;
    }}
    pre code {{ padding: 0; color: inherit; background: none; }}
    table {{
      display: block;
      width: 100%;
      margin: 1.8rem 0;
      overflow-x: auto;
      border-collapse: collapse;
      font: .88rem/1.55 "Avenir Next", Arial, sans-serif;
    }}
    th {{
      padding: .7rem .8rem;
      color: #fffdf5;
      background: var(--green);
      text-align: left;
      white-space: nowrap;
    }}
    td {{ padding: .7rem .8rem; border-bottom: 1px solid var(--rule); vertical-align: top; }}
    tr:nth-child(even) td {{ background: rgba(245, 240, 227, .62); }}
    hr {{ margin: 3.5rem 0; border: 0; border-top: 1px solid var(--rule); }}
    .footer {{
      margin-top: 6rem;
      padding-top: 1.1rem;
      color: var(--muted);
      border-top: 3px double var(--rule);
      font: 12px/1.5 Arial, sans-serif;
      letter-spacing: .08em;
      text-align: center;
      text-transform: uppercase;
    }}
    @media (max-width: 680px) {{
      body {{ font-size: 16.5px; }}
      .paper {{ width: 100%; margin: 0; border: 0; box-shadow: none; }}
    }}
    @media print {{
      body {{ background: #fff; }}
      .paper {{ width: 100%; margin: 0; border: 0; box-shadow: none; }}
      a {{ color: inherit; }}
    }}
  </style>
</head>
<body>
  <main class="paper">
    <header class="masthead">
      <p class="eyebrow">Startup Research Dossier</p>
      <h1>{title}</h1>
    </header>
    <article>{body}</article>
    <footer class="footer">Generated {generated} · THINK Startup Research</footer>
  </main>
</body>
</html>
"""


def extract_title(source: str, fallback: str) -> str:
    match = re.search(r"^#\s+(.+?)\s*$", source, flags=re.MULTILINE)
    return match.group(1).strip() if match else fallback.replace("_", " ").replace("-", " ").title()


def convert(input_path: Path, output_path: Path | None = None) -> Path:
    if not input_path.exists():
        raise FileNotFoundError(f"Markdown file not found: {input_path}")
    if input_path.suffix.lower() not in {".md", ".markdown"}:
        raise ValueError("Input must be a .md or .markdown file")

    source = input_path.read_text(encoding="utf-8")
    title = extract_title(source, input_path.stem)
    body = markdown.markdown(
        source,
        extensions=["extra", "sane_lists", "smarty", "toc"],
        output_format="html5",
    )
    destination = output_path or input_path.with_suffix(".html")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(
        HTML_TEMPLATE.format(
            title=html.escape(title),
            body=body,
            generated=datetime.now().astimezone().strftime("%B %d, %Y at %I:%M %p %Z"),
        ),
        encoding="utf-8",
    )
    return destination


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert one startup research Markdown report to elegant vintage HTML."
    )
    parser.add_argument("markdown_file", type=Path, help="Path to the Markdown report")
    parser.add_argument("-o", "--output", type=Path, help="Optional HTML output path")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    result = convert(args.markdown_file.expanduser().resolve(), args.output)
    print(result)

