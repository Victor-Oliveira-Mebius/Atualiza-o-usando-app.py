import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify
import mysql.connector

# ------------------------------------------------------------------------------
# Config Flask
# ------------------------------------------------------------------------------
# Pega os arquivos HTML diretamente da raiz (".")
app = Flask(__name__, static_folder="static", template_folder=".")

DEBUG = os.getenv("FLASK_DEBUG", "0") == "1"

# ------------------------------------------------------------------------------
# DB helpers
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
    return mysql.connector.connect(**cfg)

# ------------------------------------------------------------------------------
# Rotas de páginas (usa nomes exatamente como estão na pasta)
# ------------------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quem-somos")
def quem_somos():
    return render_template("quem-somos.html")

@app.route("/solucoes")
def solucoes():
    # nome real do arquivo: soluções.html (com acento)
    return render_template("soluções.html")

@app.route("/clientes")
def clientes():
    # nome real do arquivo: Clientes.html (com C maiúsculo)
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
        print("Erro ao listar mensagens:", e)
        return jsonify({"status": "erro", "mensagem": str(e)}), 500

@app.post("/api/enviar")
def enviar():
    conn = None
    try:
        dados = request.get_json(force=True) or {}
        nome = dados.get("nome")
        email = dados.get("email")
        telefone = dados.get("telefone")
        empresa = dados.get("empresa")
        sistema = dados.get("sistema")
        mensagem = dados.get("mensagem")
        data_hora = datetime.now()

        if not nome or not email:
            return jsonify({"status": "erro", "mensagem": "Nome e e-mail são obrigatórios."}), 400

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
        print("Erro ao inserir:", e)
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
