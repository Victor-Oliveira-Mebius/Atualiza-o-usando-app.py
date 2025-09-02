import os
from datetime import datetime
from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    redirect,
    url_for,
    make_response,
)

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
# Proteção com TOKEN (cookie/query/header) + variável global no Jinja
# ------------------------------------------------------------------------------
CLIENTES_TOKEN = os.getenv("CLIENTES_TOKEN", "").strip()

# disponibiliza {{ CLIENTES_TOKEN }} nos templates (Jinja)
app.jinja_env.globals.update(CLIENTES_TOKEN=CLIENTES_TOKEN)


def _tem_acesso():
    """Confere token por cookie, querystring ?t= e header X-Access-Token."""
    if not CLIENTES_TOKEN:
        # Se não configurar a var no Render, não bloqueia nada
        return True

    # 1) cookie
    if request.cookies.get("ctok") == CLIENTES_TOKEN:
        return True
    # 2) querystring ?t=SEU_TOKEN
    if request.args.get("t") == CLIENTES_TOKEN:
        return True
    # 3) Header opcional
    if request.headers.get("X-Access-Token") == CLIENTES_TOKEN:
        return True

    return False


@app.before_request
def _protege_rotas():
    """
    Protege /clientes e /api/mensagens (e o caminho /Clientes.html, se alguém
    tentar acessar diretamente). Ajuste a lista se quiser proteger mais rotas.
    """
    rotas_protegidas = {"/clientes", "/api/mensagens"}
    if request.path in rotas_protegidas or request.path.lower() == "/clientes.html":
        if not _tem_acesso():
            prox = request.path
            if request.query_string:
                prox += "?" + request.query_string.decode("utf-8")
            return redirect(url_for("acesso", next=prox))


@app.get("/acesso")
def acesso():
    """Tela simples para digitar o token (se CLIENTES_TOKEN estiver setado)."""
    if not CLIENTES_TOKEN:
        return "<p>CLIENTES_TOKEN não está configurado; acesso liberado.</p>", 200

    proximo = request.args.get("next") or url_for("clientes")
    return f"""
<!DOCTYPE html>
<html lang="pt-BR"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Acesso restrito</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@3.4.14/dist/tailwind.min.css">
</head><body class="bg-gray-50 flex items-center justify-center min-h-screen">
  <form action="{url_for('acesso_post')}" method="post" class="bg-white p-6 rounded shadow w-full max-w-sm">
    <h1 class="text-lg font-semibold mb-4">Área restrita</h1>
    <input type="hidden" name="next" value="{proximo}"/>
    <label class="block text-sm text-gray-700 mb-2">Token de acesso</label>
    <input name="token" type="password" class="w-full border rounded px-3 py-2 mb-4" autofocus required />
    <button class="w-full bg-blue-600 hover:bg-blue-700 text-white py-2 rounded">Entrar</button>
    <p class="text-xs text-gray-500 mt-3">Dica: você também pode acessar com <code>?t=SEU_TOKEN</code>.</p>
  </form>
</body></html>
"""


@app.post("/acesso")
def acesso_post():
    """Valida o token e grava um cookie para liberar as rotas protegidas."""
    if not CLIENTES_TOKEN:
        destino = request.form.get("next") or url_for("clientes")
        return redirect(destino)

    token = (request.form.get("token") or "").strip()
    destino = request.form.get("next") or url_for("clientes")

    if token != CLIENTES_TOKEN:
        return redirect(url_for("acesso", next=destino))

    resp = make_response(redirect(destino))
    # cookie “ctok” com validade de 30 dias
    resp.set_cookie(
        "ctok",
        CLIENTES_TOKEN,
        max_age=30 * 24 * 3600,
        secure=True,      # somente HTTPS
        httponly=True,    # JS não lê
        samesite="Lax",
        path="/",
    )
    return resp


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
        nome = (dados.get("nome") or "").strip()
        email = (dados.get("email") or "").strip()
        telefone = (dados.get("telefone") or "").strip()
        empresa = (dados.get("empresa") or "").strip()
        sistema = (dados.get("sistema") or "").strip()
        mensagem = (dados.get("mensagem") or "").strip()
        data_hora = datetime.now()

        if not nome or not email:
            return (
                jsonify({"status": "erro", "mensagem": "Nome e e-mail são obrigatórios."}),
                400,
            )
        if not telefone ou not mensagem:
            return (
                jsonify({"status": "erro", "mensagem": "Telefone e mensagem são obrigatórios."}),
                400,
            )

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
