import os
import mysql.connector
from flask import Flask, render_template, request, jsonify
from datetime import datetime
import traceback

app = Flask(__name__, static_folder='static', template_folder='.')

# --- ROTAS DO SITE ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quem-somos')
def quem_somos():
    return render_template('quem-somos.html')

@app.route('/solucoes')
def solucoes():
    return render_template('soluções.html')

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/clientes')
def clientes():
    return render_template('Clientes.html')

# --- FUNÇÃO PARA CONFIG DE BANCO (para facilitar mudança de nomes de env) ---
def get_db_config():
    return {
        'host': os.getenv('MYSQL_HOST') or os.getenv('MYSQLHOST'),
        'user': os.getenv('MYSQL_USER') or os.getenv('MYSQLUSER'),
        'password': os.getenv('MYSQL_PASSWORD') or os.getenv('MYSQLPASSWORD'),
        'database': os.getenv('MYSQL_DATABASE') or os.getenv('MYSQLDATABASE'),
        'port': int(os.getenv('MYSQL_PORT') or os.getenv('MYSQLPORT') or 3306),
        'charset': 'utf8'
    }

# --- ROTAS DA API (COM DEBUG E LOG DE ERRO) ---

@app.route('/api/mensagens', methods=['GET'])
def listar_mensagens():
    db_config = get_db_config()
    print("Config DB:", db_config)  # Debug para ver as variáveis de ambiente
    try:
        conn = mysql.connector.connect(**db_config)
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM clientes ORDER BY data_hora DESC")
        dados = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(dados)
    except Exception as e:
        print("Erro ao listar mensagens:", e)
        traceback.print_exc()
        return jsonify({'status': 'erro', 'mensagem': str(e)}), 500

@app.route('/api/enviar', methods=['POST'])
def enviar():
    db_config = get_db_config()
    print("Config DB:", db_config)  # Debug para ver as variáveis de ambiente
    print("HEADERS RECEBIDOS:", request.headers)
    print("DADOS RECEBIDOS (raw):", request.data)
    conn = None
    try:
        dados = request.get_json(force=True)
        print("DADOS RECEBIDOS (JSON):", dados)
        nome = dados.get('nome')
        email = dados.get('email')
        telefone = dados.get('telefone')
        empresa = dados.get('empresa')
        sistema = dados.get('sistema')
        mensagem = dados.get('mensagem')
        data_hora = datetime.now()

        # Checagem simples para campos obrigatórios
        if not all([nome, email, telefone, empresa, sistema, mensagem]):
            return jsonify({'status': 'erro', 'mensagem': 'Campos obrigatórios faltando!'}), 400

        conn = mysql.connector.connect(**db_config)
        cur = conn.cursor()
        cur.execute("""
            INSERT INTO clientes 
            (nome, email, telefone, empresa, sistema, mensagem, data_hora)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, (nome, email, telefone, empresa, sistema, mensagem, data_hora))
        conn.commit()
        cur.close()
        return jsonify({'status': 'sucesso'})
    except Exception as e:
        print("Erro ao inserir:", e)
        traceback.print_exc()
        if conn:
            conn.rollback()
        return jsonify({'status': 'erro', 'mensagem': str(e)}), 500
    finally:
        if conn and conn.is_connected():
            conn.close()

# --- INICIALIZAÇÃO DO SERVIDOR ---
if __name__ == '__main__':
    app.run(debug=True)
