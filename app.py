import os
import socket
from datetime import datetime
from flask import Flask, render_template, request, jsonify
import mysql.connector

# ----------------------------------------------------------------------
# Configuração Flask
# ----------------------------------------------------------------------
app = Flask(__name__, static_folder="static", template_folder=".")

DEBUG = os.getenv("FLASK_DEBUG", "0") == "1"

# ----------------------------------------------------------------------
# Helpers de conexão MySQL
# ----------------------------------------------------------------------
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

# ----------------------------------------------------------------------
# Rotas de páginas
# ----------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quem-somos")
def quem_somos():
    return render_template("quem-somos.html")

@app.route("/solucoes")
def solucoes():
    return render_template("soluções.html")  # atenção: acento no nome do arquivo

@app.route("/clientes")
def clientes():
    return render_template("Clientes.html")  # C maiúsculo no arquivo

@app.route("/form")
def form():
    return render_template("form.html")

# Health-check
@app.get("/health")
def health():
    return {"status": "ok"}, 200

# ----------------------------------------------------------------------
# API
# ----------------------------------------------------------------------
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
        nome     = dados.get("nome")
        email    = dados.get("email")
        telefone = dados.get("telefone")
        empresa  = dados.get("empresa")
        sistema  = dados.get("sistema")
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

# ----------------------------------------------------------------------
# Debug: Testes de DNS e MySQL
# ----------------------------------------------------------------------
@app.get("/debug/dns")
def debug_dns():
    host = os.getenv("MYSQL_HOST", "")
    try:
        infos = socket.getaddrinfo(host, None)
        ips = list({i[4][0] for i in infos})
        return jsonify({"host": host, "ips": ips}), 200
    except Exception as e:
        return jsonify({"host": host, "error": str(e)}), 500

@app.get("/debug/mysql")
def debug_mysql():
    try:
        cn = mysql.connector.connect(
            host=os.getenv("MYSQL_HOST"),
            user=os.getenv("MYSQL_USER"),
            password=os.getenv("MYSQL_PASSWORD"),
            database=os.getenv("MYSQL_DATABASE"),
            port=int(os.getenv("MYSQL_PORT", "3306")),
            connection_timeout=6,
            ssl_disabled=True,  # deixa True por enquanto
        )
        cur = cn.cursor()
        cur.execute("SELECT NOW()")
        now = cur.fetchone()[0]
        cur.close()
        cn.close()
        return jsonify({"ok": True, "now": str(now)}), 200
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

# ----------------------------------------------------------------------
# Dev server local
# ----------------------------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=DEBUG)
