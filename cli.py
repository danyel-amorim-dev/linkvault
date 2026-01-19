from db import get_connection
from export import export_to_html
import sys

def add_link():
    url = input("🔗 URL: ").strip().rstrip(" /")
    if not url:
        print("❌ URL não pode estar vazia.")
        return
    title = input("📌 Título (opcional): ").strip() or url
    category = input("📂 Categoria (ex: tutorial, ferramenta): ").strip() or "outros"

    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO links (url, title, category) VALUES (?, ?, ?)", (url, title, category))
    conn.commit()
    conn.close()
    print("✅ Link salvo!")

def list_links():
    category_filter = input("🔍 Filtrar por categoria? (deixe vazio para todos): ").strip()
    conn = get_connection()
    cursor = conn.cursor()
    if category_filter:
        cursor.execute("SELECT * FROM links WHERE category = ? ORDER BY created_at DESC", (category_filter,))
    else:
        cursor.execute("SELECT * FROM links ORDER BY created_at DESC")
    rows = cursor.fetchall()
    conn.close()

    if not rows:
        print("📭 Nenhum link encontrado.")
        return

    print("\n📚 Seus links:")
    for row in rows:
        print(f"[{row[4][:10]}] ({row[3]}) {row[2]} → {row[1]}")
    print()

def main_menu():
    while True:
        print("\n🔐 LinkVault – Gerenciador Offline de Links")
        print("1. ➕ Adicionar link")
        print("2. 📖 Listar links")
        print("3. 📤 Exportar para HTML")
        print("4. ❌ Sair")
        choice = input("Escolha uma opção: ").strip()

        if choice == "1":
            add_link()
        elif choice == "2":
            list_links()
        elif choice == "3":
            export_to_html()
        elif choice == "4":
            print("👋 Até logo!")
            sys.exit(0)
        else:
            print("⚠️ Opção inválida.")
