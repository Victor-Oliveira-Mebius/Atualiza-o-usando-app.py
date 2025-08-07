import os
from flask import Flask, render_template, request, jsonify
import mysql.connector
from datetime import datetime

app = Flask(__name__, static_folder='static', template_folder='.')

db_config = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE'),
    'port': int(os.getenv('MYSQL_PORT')),
    'charset': 'utf8'
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form')
def form():
    return render_template('form.html')

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

# Outras rotas...

if __name__ == '__main__':
    app.run(debug=True)
