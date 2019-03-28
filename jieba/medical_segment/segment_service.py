#encoding=utf8
import os
from flask import Flask, request,jsonify
from wordcut import word_cut
app = Flask(__name__)

@app.route('/segment', methods=['POST'])
def segment():
    inputdata = request.form.get('input')
    outdata = word_cut(inputdata)
    return jsonify(outdata)


if __name__ == '__main__':
    app.run(host='192.168.10.87', port=8760, debug = True)
