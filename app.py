import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify
import mysql.connector

# ------------------------------------------------------------------------------
# Config Flask
# ------------------------------------------------------------------------------
# Use os HTMLs diretamente na raiz (como está no seu projeto)
app = Flask(__name__, static_folder="static", template_folder=".")

DEBUG = os.getenv("FLASK_DEBUG", "0") == "1"

# ------------------------------------------------------------------------------
# DB helpers (MySQL)
# ------------------------------------------------------------------------------
def get_db_config():
    return {
        "host": os.getenv("MYSQL_HOST", ""),
        "user": os.getenv("MYSQL_USER", ""),
        "password": os.getenv("MYSQL_PASSWORD", ""),
        "database": os.getenv("MYSQL_DATABASE", ""),
        "port": int(os.getenv("MYSQL_PORT", "3306")),
        "charset": "utf8mb4",
        "use_pure": True,
        "connection_timeout": 10,
    }

def open_conn():
    cfg = get_db_config()
    # Validação simples
    if not all([cfg["host"], cfg["user"], cfg["password"], cfg["database"]]):
        raise RuntimeError("Variáveis MYSQL_* não configuradas corretamente no Render.")
    return mysql.connector.connect(**cfg)

def init_db():
    """Cria a tabela se não existir (id auto incremental, etc.)."""
    try:
        conn = open_conn()
        cur = conn.cursor()
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS clientes (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nome VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                telefone VARCHAR(100) NOT NULL,
                empresa VARCHAR(255),
                sistema VARCHAR(255),
                mensagem TEXT NOT NULL,
                data_hora DATETIME NOT NULL
            ) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
            """
        )
        conn.commit()
        cur.close()
        conn.close()
        print("[init_db] Tabela 'clientes' OK")
    except Exception as e:
        print("[init_db] Erro ao criar/verificar tabela:", e)

# Inicializa tabela no boot (ignora erro para não derrubar app)
try:
    init_db()
except Exception as e:
    print("[init_db] Ignorado:", e)

# ------------------------------------------------------------------------------
# Rotas de páginas (mantêm seus nomes/arquivos)
# ------------------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quem-somos")
def quem_somos():
    return render_template("quem-somos.html")

@app.route("/solucoes")
def solucoes():
    # arquivo tem acento
    return render_template("soluções.html")

@app.route("/clientes")
def clientes():
    # arquivo com C maiúsculo
    return render_template("Clientes.html")

@app.route("/form")
def form():
    return render_template("form.html")

# Health-check
@app.get("/health")
def health():
    return {"status": "ok"}, 200

# ------------------------------------------------------------------------------
# API
# ------------------------------------------------------------------------------
@app.get("/api/mensagens")
def listar_mensagens():
    try:
        conn = open_conn()
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM clientes ORDER BY data_hora DESC")
        dados = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(dados), 200
    except Exception as e:
        print("[/api/mensagens] Erro:", e)
        return jsonify({"status": "erro", "mensagem": str(e)}), 500

@app.post("/api/enviar")
def enviar():
    conn = None
    try:
        dados = request.get_json(force=True) or {}
        nome     = (dados.get("nome") or "").strip()
        email    = (dados.get("email") or "").strip()
        telefone = (dados.get("telefone") or "").strip()
        empresa  = (dados.get("empresa") or "").strip()
        sistema  = (dados.get("sistema") or "").strip()
        mensagem = (dados.get("mensagem") or "").strip()
        data_hora = datetime.now()

        # validações mínimas
        if not nome or not email:
            return jsonify({"status": "erro", "mensagem": "Nome e e-mail são obrigatórios."}), 400
        if not telefone or not mensagem:
            return jsonify({"status": "erro", "mensagem": "Telefone e mensagem são obrigatórios."}), 400

        conn = open_conn()
        cur = conn.cursor()
        cur.execute(
            """
            INSERT INTO clientes
            (nome, email, telefone, empresa, sistema, mensagem, data_hora)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """,
            (nome, email, telefone, empresa, sistema, mensagem, data_hora),
        )
        conn.commit()
        cur.close()
        return jsonify({"status": "sucesso"}), 201

    except Exception as e:
        print("[/api/enviar] Erro:", e)
        if conn:
            try:
                conn.rollback()
            except Exception:
                pass
        return jsonify({"status": "erro", "mensagem": str(e)}), 500
    finally:
        if conn:
            try:
                conn.close()
            except Exception:
                pass

# ------------------------------------------------------------------------------
# Dev server local (em produção use Gunicorn)
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=DEBUG)
