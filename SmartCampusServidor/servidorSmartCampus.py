from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def arquivo():
    arq = open('D:\PyCharm/SmartCampusServidor/arquivos/teste1.txt', 'r')
    texto = arq.readlines()
    for linha in texto:
        print(linha)
    arq.close()
    return linha



@app.route('/arcondicionado/ligado=<string:ligado>&tempo=<string:tempo>&auto=<string:auto>', methods=['GET'])
def arCondicionado(ligado, tempo, auto):
        arq = open('D:\PyCharm/SmartCampusServidor/arquivos/tempo.txt', 'w')
        arq.write(ligado+"|"+tempo+"|"+auto)
        arq.close()
        return jsonify({'response': 'OK'})

@app.route('/luz/luzOnOff=<string:ligadorDesligarLuz>', methods=['GET'])
def luz(ligadorDesligarLuz):
        arq = open('D:\PyCharm/SmartCampusServidor/arquivos/LuzOnOff.txt', 'w')
        arq.write(ligadorDesligarLuz)
        arq.close()
        return jsonify({'response': 'OK'})

@app.route('/lixeira/')
def lixeira():
        arq = open('D:\PyCharm/SmartCampusServidor/arquivos/capacidadeDaLixeira.txt', 'r')
        capacidadeDaLixeira = arq.readlines()
        resp = ""
        for porcentagem in capacidadeDaLixeira:

            resp = porcentagem
        arq.close()
        return jsonify({'response':resp})


if __name__ == '__main__':
    app.run(debug=True,  host='192.168.0.103')