import os
import mysql.connector
from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__, static_folder='static', template_folder='.')

# O DICIONÁRIO db_config FOI REMOVIDO DAQUI

# --- ROTAS DO SITE ---
@app.route('/')
def index():
    return render_template('index.html')

# ... (suas outras rotas do site continuam aqui, sem mudança) ...
@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/clientes')
def clientes():
    return render_template('Clientes.html')

# --- ROTAS DA API (COM A CORREÇÃO) ---

@app.route('/api/mensagens', methods=['GET'])
def listar_mensagens():
    # CORREÇÃO: O db_config agora está DENTRO da função
    db_config = {
        'host': os.getenv('MYSQLHOST'),
        'user': os.getenv('MYSQLUSER'),
        'password': os.getenv('MYSQLPASSWORD'),
        'database': os.getenv('MYSQLDATABASE'),
        'port': int(os.getenv('MYSQLPORT')),
        'charset': 'utf8'
    }
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
        return jsonify({'status': 'erro', 'mensagem': str(e)})

@app.route('/api/enviar', methods=['POST'])
def enviar():
    # CORREÇÃO: O db_config também está DENTRO desta função
    db_config = {
        'host': os.getenv('MYSQLHOST'),
        'user': os.getenv('MYSQLUSER'),
        'password': os.getenv('MYSQLPASSWORD'),
        'database': os.getenv('MYSQLDATABASE'),
        'port': int(os.getenv('MYSQLPORT')),
        'charset': 'utf8'
    }
    conn = None
    try:
        dados = request.get_json()
        nome = dados.get('nome')
        email = dados.get('email')
        telefone = dados.get('telefone')
        empresa = dados.get('empresa')
        sistema = dados.get('sistema')
        mensagem = dados.get('mensagem')
        data_hora = datetime.now()

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
        if conn:
            conn.rollback()
        return jsonify({'status': 'erro', 'mensagem': str(e)})
    finally:
        if conn and conn.is_connected():
            conn.close()

# --- INICIALIZAÇÃO DO SERVIDOR ---

if __name__ == '__main__':
    app.run(debug=True)
