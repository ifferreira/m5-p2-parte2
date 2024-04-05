from flask import Flask, render_template, request
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

db = []

#Rota que retorna pong
@app.route('/ping')
def ping():
    db.append({'date': datetime.now(), 'rota': '/ping', 'metodo': request.method})
    return {'resposta': 'pong'}

#Rota que retorna o conteúdo do JSON enviado na requisicao
@app.route('/echo', methods=['POST'])
def echo():
     db.append({'date': datetime.now(), 'rota': '/echo', 'metodo': request.method})
     dados = request.json
     return {'resposta': dados.get("dados")}

#Rota que renderiza a pagina de visualizacao de logs
@app.route('/dash')
def dash():
    return render_template('dash.html')

#Rota que retorna midia sobre os dados armazenados
@app.route('/info')
def info():
    return render_template('info.html', infos=db)

if __name__ == '__main__':
    app.run(debug=True)

