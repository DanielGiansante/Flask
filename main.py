from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/<string:nome>/', methods=['GET'])
def get_me(nome):
    return jsonify({'estado':"SP",
        'nome': nome,
                     
                    'profissao':"programador",
                    'idade': 26,
                     })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
