#!/usr/bin/env python3
"""Rebuild docs/index.html (standalone, Claude-free) from shelf-scout.html."""
src = open("shelf-scout.html").read()
head_end = src.index("</style>") + len("</style>")
head, body = src[:head_end], src[head_end:]
out = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>:root{{color-scheme:light dark}}body{{margin:0}}[hidden]{{display:none!important}}img{{max-width:100%}}</style>
{head}
</head>
<body>{body}
</body>
</html>
"""
open("docs/index.html", "w").write(out)
print("wrote docs/index.html")
