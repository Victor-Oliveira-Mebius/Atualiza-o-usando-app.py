import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify

# PostgreSQL (psycopg 3)
import psycopg
from psycopg.rows import dict_row

# ------------------------------------------------------------------------------
# Flask
# ------------------------------------------------------------------------------
# usa os HTML exatamente onde estão hoje (raiz do projeto)
app = Flask(__name__, static_folder="static", template_folder=".")

DEBUG = os.getenv("FLASK_DEBUG", "0") == "1"

# ------------------------------------------------------------------------------
# Banco de dados (Postgres via DATABASE_URL do Render)
# ------------------------------------------------------------------------------
def get_conn():
    """
    Abre conexão com Postgres usando a variável de ambiente DATABASE_URL.
    Ex.: postgres://usuario:senha@host:5432/nomedb
    """
    dsn = os.getenv("DATABASE_URL")
    if not dsn:
        raise RuntimeError(
            "DATABASE_URL não configurado. Defina no Render (Settings -> Environment)."
        )
    return psycopg.connect(dsn, autocommit=False, row_factory=dict_row)

def init_db():
    """Cria a tabela 'clientes' se não existir."""
    with get_conn() as conn, conn.cursor() as cur:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS clientes (
                id        SERIAL PRIMARY KEY,
                nome      TEXT NOT NULL,
                email     TEXT NOT NULL,
                telefone  TEXT NOT NULL,
                empresa   TEXT,
                sistema   TEXT,
                mensagem  TEXT NOT NULL,
                data_hora TIMESTAMP NOT NULL DEFAULT NOW()
            );
            """
        )
        conn.commit()

# cria a tabela na subida do app (não quebra se falhar)
try:
    init_db()
except Exception as e:
    print("[init_db] erro:", e)

# ------------------------------------------------------------------------------
# Rotas de páginas (nomes dos arquivos mantidos)
# ------------------------------------------------------------------------------
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/quem-somos")
def quem_somos():
    return render_template("quem-somos.html")

@app.route("/solucoes")
def solucoes():
    # nome real do arquivo tem acento
    return render_template("soluções.html")

@app.route("/clientes")
def clientes():
    # nome real do arquivo tem C maiúsculo
    return render_template("Clientes.html")

@app.route("/form")
def form():
    return render_template("form.html")

# Health-check utilizado pelo Render
@app.get("/health")
def health():
    return {"status": "ok"}, 200

# ------------------------------------------------------------------------------
# API
# ------------------------------------------------------------------------------
@app.get("/api/mensagens")
def listar_mensagens():
    try:
        with get_conn() as conn, conn.cursor() as cur:
            cur.execute("SELECT * FROM clientes ORDER BY data_hora DESC;")
            dados = cur.fetchall()
        return jsonify(dados), 200
    except Exception as e:
        print("[/api/mensagens] erro:", e)
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

        if not nome or not email:
            return jsonify({"status": "erro", "mensagem": "Nome e e-mail são obrigatórios."}), 400
        if not telefone or not mensagem:
            return jsonify({"status": "erro", "mensagem": "Telefone e mensagem são obrigatórios."}), 400

        conn = get_conn()
        with conn.cursor() as cur:
            cur.execute(
                """
                INSERT INTO clientes
                    (nome, email, telefone, empresa, sistema, mensagem, data_hora)
                VALUES
                    (%s,   %s,    %s,       %s,      %s,      %s,       %s);
                """,
                (nome, email, telefone, empresa, sistema, mensagem, data_hora),
            )
        conn.commit()
        return jsonify({"status": "sucesso"}), 201

    except Exception as e:
        print("[/api/enviar] erro:", e)
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
# Debug opcional
# ------------------------------------------------------------------------------
@app.get("/debug/pg")
def debug_pg():
    """Conecta e retorna NOW() para validar a conexão com Postgres."""
    try:
        with get_conn() as conn, conn.cursor() as cur:
            cur.execute("SELECT NOW() AS agora;")
            row = cur.fetchone()
        return jsonify({"ok": True, "now": str(row["agora"])}), 200
    except Exception as e:
        return jsonify({"ok": False, "error": str(e)}), 500

# ------------------------------------------------------------------------------
# Dev server local (em produção o Render usa Gunicorn)
# ------------------------------------------------------------------------------
if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=DEBUG)
