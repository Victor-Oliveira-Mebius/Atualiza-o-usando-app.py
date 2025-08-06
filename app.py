# Forçando um novo deploy no Railway
from flask import Flask, render_template, request, redirect, jsonify
import mysql.connector
from datetime import datetime
import os  # <-- CORREÇÃO 1: Importa a biblioteca 'os'

# CORREÇÃO 2: A inicialização do Flask vem primeiro.
# Diz ao Flask para procurar HTMLs na pasta atual e imagens na pasta 'static'.
app = Flask(__name__, static_folder='static', template_folder='.')

# Configuração da conexão para ler as variáveis de ambiente do Railway
db_config = {
    'host': os.getenv('MYSQLHOST'),
    'user': os.getenv('MYSQLUSER'),
    'password': os.getenv('MYSQLPASSWORD'),
    'database': os.getenv('MYSQLDATABASE'),
    'port': int(os.getenv('MYSQLPORT')),
    'charset': 'utf8'
}

# --- ROTAS DO SITE ---
# CORREÇÃO 3: Todas as rotas devem ser definidas ANTES da inicialização do servidor.

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


# --- ROTAS DA API (para interagir com o banco de dados) ---

@app.route('/api/mensagens', methods=['GET'])
def listar_mensagens():
    conn = None
    try:
        conn = mysql.connector.connect(**db_config)
        cur = conn.cursor(dictionary=True)
        cur.execute("SELECT * FROM clientes ORDER BY data_hora DESC")
        dados = cur.fetchall()
        return jsonify(dados)
    except Exception as e:
        print("Erro ao listar mensagens:", e)
        return jsonify({'status': 'erro', 'mensagem': str(e)})
    finally:
        if conn and conn.is_connected():
            cur.close()
            conn.close()

@app.route('/api/enviar', methods=['POST'])
def enviar():
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
        return jsonify({'status': 'sucesso'})
    except Exception as e:
        print("Erro ao inserir:", e)
        if conn:
            conn.rollback()
        return jsonify({'status': 'erro', 'mensagem': str(e)})
    finally:
        if conn and conn.is_connected():
            cur.close()
            conn.close()

# --- INICIALIZAÇÃO DO SERVIDOR ---
# CORREÇÃO 4: Este bloco deve ser a ÚLTIMA coisa no arquivo.
if __name__ == '__main__':
    app.run(debug=True)

