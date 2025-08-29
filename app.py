import os
from datetime import datetime
from flask import Flask, render_template, request, jsonify

# psycopg 3 (PostgreSQL)
import psycopg
from psycopg.rows import dict_row

# ------------------------------------------------------------------------------
# Config Flask
# ------------------------------------------------------------------------------
# Usa os arquivos HTML diretamente na raiz (mesmo padrão que você já usa)
app = Flask(__name__, static_folder="static", template_folder=".")

DEBUG = os.getenv("FLASK_DEBUG", "0") == "1"

# ------------------------------------------------------------------------------
# Conexão com o banco (PostgreSQL no Render)
# ------------------------------------------------------------------------------
def get_conn():
    """
    Conecta no PostgreSQL usando o DSN fornecido pelo Render em DATABASE_URL.
    Ex.: postgres://user:pass@host:port/dbname
    """
    dsn = os.getenv("DATABASE_URL")
    if not dsn:
        raise RuntimeError(
            "DATABASE_URL não configurado. Defina essa variável nas Environment Variables do Render."
        )
    # Em geral, o DSN do Render já vem com sslmode=require
    return psycopg.connect(dsn, autocommit=False, row_factory=dict_row)

def init_db():
    """
    Cria a tabela 'clientes' se não existir.
    """
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

# Inicializa a tabela ao subir a app
try:
    init_db()
except Exception as e:
    # Não quebra a app se falhar na inicialização; loga o erro
    print("[init_db] Erro ao criar/verificar tabela:", e)

# ------------------------------------------------------------------------------
# Rotas de páginas (mantive exatamente como você já tinha)
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
    """
    Retorna todas as mensagens (mais recentes primeiro).
    """
    try:
        with get_conn() as conn, conn.cursor() as cur:
            cur.execute("SELECT * FROM clientes ORDER BY data_hora DESC;")
            dados = cur.fetchall()
        return jsonify(dados), 200
    except Exception as e:
        print("[/api/mensagens] Erro:", e)
        return jsonify({"status": "erro", "mensagem": str(e)}), 500

@app.post("/api/enviar")
def enviar():
    """
    Recebe JSON com: nome, email, telefone, empresa, sistema, mensagem
    e salva na tabela 'clientes'.
    """
    conn = None
    try:
        dados = request.get_json(force=True) or {}
        nome     = dados.get("nome", "").strip()
        email    = dados.get("email", "").strip()
        telefone = dados.get("telefone", "").strip()
        empresa  = dados.get("empresa", "")
        sistema  = dados.get("sistema", "")
        mensagem = dados.get("mensagem", "").strip()
        data_hora = datetime.now()

        # validações mínimas (mantidas)
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
                    (%s,   %s,    %s,       %s,      %s,      %s,       %s)
                """,
                (nome, email, telefone, empresa, sistema, mensagem, data_hora),
            )
        conn.commit()
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
