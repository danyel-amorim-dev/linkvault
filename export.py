from db import get_connection
import html

def export_to_html():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT category, url, title, created_at FROM links ORDER BY category, created_at DESC")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("📭 Nada para exportar.")
        return

    categories = {}
    for cat, url, title, date in rows:
        if cat not in categories:
            categories[cat] = []
        categories[cat].append((url, title, date[:10]))

    html_content = """<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>LinkVault – Meus Links</title>
    <style>
        body { font-family: monospace; max-width: 800px; margin: 2rem auto; padding: 0 1rem; }
        h2 { color: #2c3e50; border-bottom: 1px solid #eee; padding-bottom: 0.3rem; }
        ul { padding-left: 1.2rem; }
        li { margin-bottom: 0.4rem; }
        a { text-decoration: none; color: #3498db; }
        a:hover { text-decoration: underline; }
        .date { color: #7f8c8d; font-size: 0.9em; }
    </style>
</head>
<body>
    <h1>🔐 LinkVault – Meus Links</h1>
"""
    for cat, links in sorted(categories.items()):
        html_content += f"\n    <h2>📂 {html.escape(cat)}</h2>\n    <ul>\n"
        for url, title, date in links:
            safe_title = html.escape(title)
            safe_url = html.escape(url)
            html_content += f'        <li><a href="{safe_url}" target="_blank">{safe_title}</a> <span class="date">({date})</span></li>\n'
        html_content += "    </ul>\n"

    html_content += """
</body>
</html>
"""

    with open("links.html", "w", encoding="utf-8") as f:
        f.write(html_content)

    print("✅ Arquivo 'links.html' gerado com sucesso!")
