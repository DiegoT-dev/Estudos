import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import sqlite3


app = Flask(__name__)
cor = CORS(app, resource={r'/*':{'origins':'*'}})

cnx = sqlite3.connect('cadastro.bd')
c = cnx.cursor()

c.execute('create table if not exists usuarios(id integer primary key AUTOINCREMENT, nome varchar(20), linguagem varchar(15))')
cnx.commit()


# HOME
@app.route('/')
def index():
    return ('<h1>API feita com FLASK e BD (SQLITE3)</h1><h2>Rotas</h2><ul><li><h3>Consulta Geral:</h3></li><p>Para consultar todos o cadastro use o método GET na uri "/cad"</p><li><h3>Pesquisa por Cadastro:</h3></li><p>POR ID => Usar GET na uri "/cad/id", onde o id deve ser o id (numeral) do usuário</p><p>POR LINGUAGEM => Usar GET na uri "/cad/linguagem", onde a linguagem deve ser substituida pela linguagem que procura</p><li><h3>Incluir Cadastro:</h3></li><p>Usar método POST na uri "/cad"</p><p>A inclusão deve ser feita somente em formato JSON contendo os argumentos "nome" e "linguagem", exemplo: <br> { <br> "nome":"FULANO", <br> "linguagem":"CSS" <br> } </p><li><h3>Alteração de Cadastro:</h3></li><p>Usar método PUT com a uri "/cad/id", onde o id deve ser o id (numeral) do usuário</p><p>Por hora apenas fazendo alteração do campo linguagem dos cadastros</p><p>Alteração deve ser feita somente em formato JSON contendo os argumento "linguagem", exemplo: {"linguagem":"CSS"}</p><li><h3>Deletar Cadastro:</h3></li><p>Usar método DELETE com a uri "/cad/id", onde o id deve ser o id (numeral) do usuário</p></ul>')


# pesquisa de todos cadastros
@app.route('/cad')
def home():
    cnx = sqlite3.connect('cadastro.bd')
    c = cnx.cursor()
    temp = dict()
    cads = list()
    c.execute('select * from usuarios')
    for row in c:
        for lista, i in enumerate(row):
            if lista == 0:
                temp["id"] = i
            if lista == 1:
                temp["nome"] = i
            if lista == 2:
                temp["linguagem"] = i
        cads.append(temp.copy())
    

    return jsonify(cads), 200


# pesquisa por Linguagem
@app.route('/cad/<string:lg>')
def devs_per_lang(lg):
    cnx = sqlite3.connect('cadastro.bd')
    c = cnx.cursor()
    temp = dict()
    c.execute(f'select * from usuarios where "linguagem"="{lg}"')
    for row in c:
        for lista, i in enumerate(row):
            if lista == 0:
                temp["id"] = i
            if lista == 1:
                temp["nome"] = i
            if lista == 2:
                temp["linguagem"] = i
            
    
    return jsonify(temp), 200


# pesquisa por ID
@app.route('/cad/<int:id>')
def devs_per_id(id):
    cnx = sqlite3.connect('cadastro.bd')
    c = cnx.cursor()
    temp = dict()
    cads = list()
    c.execute(f'select * from usuarios where "id" = "{id}"')
    for row in c:
        for lista, i in enumerate(row):
            if lista == 0:
                temp["id"] = i
            if lista == 1:
                temp["nome"] = i
            if lista == 2:
                temp["linguagem"] = i
        cads.append(temp.copy())
    
    for cad in cads:
        if cad["id"] == id:
            return jsonify(cad), 200
    return jsonify({'error':'not found'}), 404


# Inserir dados
@app.route('/cad', methods=['POST'])
def sav_dev():
    cnx = sqlite3.connect('cadastro.bd')
    c = cnx.cursor()

    c.execute('create table if not exists usuarios(id integer primary key AUTOINCREMENT, nome varchar(20), linguagem varchar(15))')
    cnx.commit()
    data = request.get_json()
    query = ('insert into usuarios (nome, linguagem) values (?,?)')
    dados = (f'{data["nome"]}',f'{data["linguagem"]}')
    
    c.execute(query,dados)
    cnx.commit()
            
    return jsonify(data), 201



# Alterar Linguagem
@app.route('/cad/<int:id>', methods=['PUT'])
def change_lang(id):
    cnx = sqlite3.connect('cadastro.bd')
    c = cnx.cursor()

        
    data = request.get_json().get('linguagem')
    c.execute(f'update usuarios set linguagem = "{data}" where "id" = "{id}"')
    cnx.commit()
    
    temp = dict()
    cads = list()
    
    c.execute(f'select * from usuarios where "id" = "{id}"')
    for row in c:
        for lista, i in enumerate(row):
            if lista == 0:
                temp["id"] = i
            if lista == 1:
                temp["nome"] = i
            if lista == 2:
                temp["linguagem"] = i
        cads.append(temp.copy())
        
    for cad in cads:
        if cad["id"] == id:
            return jsonify(cad), 200                       
      
    return jsonify({'error':f'Usuário com id {id} não Existe'}), 404


# Deletar cadastros
@app.route('/cad/<int:id>', methods=['DELETE'])
def remove_dev(id):
    cnx = sqlite3.connect('cadastro.bd')
    c = cnx.cursor()
    c.execute(f'delete from usuarios where "id" = "{id}"')
    cnx.commit()
    return jsonify({'message':'Usuário removido'}), 200


def main():
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)



if __name__== '__main__':
    main()