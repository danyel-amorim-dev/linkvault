# 🔐 LinkVault

Um gerenciador **offline, simples e seguro** de links com categorias.  
Feito em **Python puro + SQLite** — sem internet, sem JavaScript, sem rastreamento.

Ideal para devs, pesquisadores ou quem valoriza **privacidade e produtividade local**.

---

## ✨ Recursos

- ✅ Salva links com **título** e **categoria**
- 📁 Armazena tudo em **SQLite** (`links.db`)
- 🖥️ Interface via **terminal** (rápida e leve)
- 📤 Exporta para **HTML estático** (visualização offline bonita)
- 🔒 100% offline — **nada sai da sua máquina**

---

## ▶️ Como usar

1. Clone ou baixe este repositório
2. No terminal, execute:
   ```bash
   python3 main.py
   ```
3. Use o menu interativo:
   - Adicionar links
   - Listar por categoria
   - Exportar para `links.html`

> Requer Python 3.6+ (já instalado na maioria das distros Linux)

---

## 📁 Arquivos

- `main.py` – Ponto de entrada
- `db.py` – Gerencia o banco SQLite
- `cli.py` – Interface do terminal
- `export.py` – Gera HTML limpo
- `links.html` – Saída exportável (não é versionado)

---

## 🛡️ Privacidade

- Nenhum dado é enviado à internet
- O arquivo `links.db` **nunca é incluído no Git** (veja `.gitignore`)
- Tudo roda localmente

---

Feito com ❤️ por pk10jj  
*Para devs que amam simplicidade e controle.*
