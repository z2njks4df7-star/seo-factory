#!/usr/bin/env python3
"""
SEO 工厂 v6.0 - 头部对标版 (快速修复版)
"""
import os, json, datetime
from pathlib import Path
from urllib.parse import quote

BASE = Path.home() / "WorkBuddy" / "SEO"
DOCS = BASE / "docs"

articles = []
for f in DOCS.glob("article_*.html"):
    content = f.read_text(encoding="utf-8")
    title = f.stem.replace("article_", "").replace("-", " ").title()
    articles.append({"title": title, "slug": f.stem.replace("article_", ""), "url": f"{f.stem}.html"})

articles.sort(key=lambda x: x["title"])

# 极简高性能首页
news_items = ""
for i, a in enumerate(articles):
    news_items += f"""
    <div class="item">
        <div class="rank">#{i+1}</div>
        <h2><a href="{a['url']}">{a['title']}</a></h2>
    </div>
    """

html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>2026 技术前沿报告 | AI 深度分析</title>
<style>
:root{{--bg:#0f172a;--card:#1e293b;--text:#f8fafc;--accent:#38bdf8;--meta:#94a3b8}}
body{{font-family:system-ui,sans-serif;background:var(--bg);color:var(--text);margin:0;padding:20px}}
.container{{max-width:1000px;margin:0 auto}}
header{{border-bottom:2px solid var(--accent);padding-bottom:20px;margin-bottom:30px}}
h1{{color:var(--accent);font-size:2.5rem;margin:0}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:20px}}
.item{{background:var(--card);padding:20px;border-radius:8px;border:1px solid #334155;position:relative}}
.rank{{position:absolute;top:10px;right:10px;background:var(--accent);color:#000;padding:2px 8px;border-radius:4px;font-weight:bold}}
.item h2{{margin:0 0 10px;font-size:1.1rem}}
.item a{{color:var(--text);text-decoration:none}}
.item a:hover{{color:var(--accent)}}
footer{{text-align:center;margin-top:50px;color:var(--meta)}}
</style>
</head>
<body>
<div class="container">
<header><h1>🚀 2026 技术前沿报告</h1><p style="color:var(--meta)">AI 驱动的深度科技分析</p></header>
<div class="grid">{news_items}</div>
<footer>© 2026 SEO Factory | Generated in {len(articles)} articles</footer>
</div>
</body>
</html>"""

with open(DOCS / "index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"✅ 首页优化完成（极简高性能版）")
print(f"📊 文章数：{len(articles)}")

# 生成 sitemap
sitemap = '<?xml version="1.0"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://seo-factory.vercel.app/</loc></url>'
for a in articles:
    sitemap += f'<url><loc>https://seo-factory.vercel.app/{a["url"]}</loc></url>'
sitemap += '</urlset>'

with open(DOCS / "sitemap.xml", "w") as f:
    f.write(sitemap)

print(f"✅ sitemap.xml 生成完成")
print(f"🚀 下一步：部署！")