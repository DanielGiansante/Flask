from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/sobre')
def sobre():
  return render_template('sobre.html')

@app.route('/<string:nome>', methods=['GET'])
def get_me(nome):
    return jsonify({'nome': nome})

if __name__ == '__main__':
  app.run(app.run(debug=True, port=os.getenv("PORT", default=5000)))
