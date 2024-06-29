from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/<string:nome>', methods=['GET'])
def get_me(nome):
    return jsonify({'nome': nome})

if __name__ == '__main__':
  app.run(port=5000)
