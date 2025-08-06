from flask import Flask, render_template, request, redirect, jsonify
import mysql.connector
from datetime import datetime

# A ÚNICA CORREÇÃO NECESSÁRIA ESTÁ AQUI:
# Adicionamos static_folder='static' para que o Flask encontre suas imagens.
app = Flask(__name__, template_folder='.', static_folder='static')

# Configuração da conexão com o banco de dados (seu código original, está perfeito)
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': '791564791564',
    'database': 'universo',
    'port': 3306,
    'charset': 'utf8'
}

# --- ROTAS DO SITE ---

# A rota principal agora carrega a página index.html
@app.route('/')
def index():
    return render_template('index.html')

# Novas rotas para cada página do seu site
@app.route('/quem-somos')
def quem_somos():
    return render_template('quem-somos.html')

@app.route('/solucoes')
def solucoes():
    return render_template('soluções.html')

# Rota para o formulário de contato (acessível via /form)
@app.route('/form')
def form():
    return render_template('form.html')

# Rota para a página de visualização de clientes (acessível via /clientes)
@app.route('/clientes')
def clientes():
    return render_template('Clientes.html')


# --- ROTAS DA API (para interagir com o banco de dados) ---

@app.route('/api/mensagens', methods=['GET'])
def listar_mensagens():
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
