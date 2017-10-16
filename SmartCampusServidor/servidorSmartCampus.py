'''
João Marcos de Oliveira Santos
Site: www.jm7087.com
10/10/2017
'''
import os
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def arquivo():
    arq = open(os.getcwd()+'/arquivos/teste1.txt', 'r')
    texto = arq.readlines()
    for linha in texto:
        print(linha)
    arq.close()
    return linha



@app.route('/arcondicionado/ligado=<string:ligado>&tempo=<string:tempo>&auto=<string:auto>', methods=['GET'])
def arCondicionado(ligado, tempo, auto):
        arq = open(os.getcwd()+'/arquivos/tempo.txt', 'w')
        arq.write(ligado+"|"+tempo+"|"+auto)
        arq.close()
        return jsonify({'response': 'OK'})

@app.route('/luz/luzOnOff=<string:ligadorDesligarLuz>', methods=['GET'])
def luz(ligadorDesligarLuz):
        arq = open(os.getcwd()+'/arquivos/LuzOnOff.txt', 'w')
        arq.write(ligadorDesligarLuz)
        arq.close()
        return jsonify({'response': 'OK'})

@app.route('/lixeira/')
def lixeira():
        arq = open(os.getcwd()+'/arquivos/capacidadeDaLixeira.txt', 'r')
        capacidadeDaLixeira = arq.readlines()
        resp = ""
        for porcentagem in capacidadeDaLixeira:

            resp = porcentagem
        arq.close()
        return jsonify({'response':resp})


@app.route('/energia/')
def energia():
        arq = open(os.getcwd()+'/arquivos/energia.txt', 'r')
        enegia = arq.readlines()
        resp = ""
        for CP in enegia:

            resp = CP
        arq.close()
        return jsonify({'response':resp})

if __name__ == '__main__':
    app.run(debug=True,  host='localhost')