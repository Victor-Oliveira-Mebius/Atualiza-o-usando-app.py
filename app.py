import os
import mysql.connector
from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__, static_folder='static', template_folder='.')

def get_db_config():
    return {
        'host': os.getenv('MYSQL_HOST'),
        'user': os.getenv('MYSQL_USER'),
        'password': os.getenv('MYSQL_PASSWORD'),
        'database': os.getenv('MYSQL_DATABASE'),
        'port': int(os.getenv('MYSQL_PORT') or 3306),
        'charset': 'utf8'
    }

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

@app.route('/api/mensagens', methods=['GET'])
def listar_mensagens():
    db_config = get_db_config()
    print("Banco de dados de configuração:", db_config)  # Debug!
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
    db_config = get_db_config()
    print("Banco de dados de configuração:", db_config)  # Debug!
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

if __name__ == '__main__':
    app.run(debug=True)
