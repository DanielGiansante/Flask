from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/')
def index():
    return jsonify({'estado':"SP",
                    'profissao':"programador",
                    'idade': 26,
                     })

@app.route('/<string:nome>/', methods=['GET'])
def get_me(nome):
    return jsonify({'estado':"SP",
        'nome': nome,
                     
                    'profissao':"programador",
                    'idade': 26,
                     })

if __name__ == '__main__':
    app.run(debug=True)
