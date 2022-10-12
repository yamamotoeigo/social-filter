from flask import Flask, render_template, request
from models import filter

app = Flask(__name__)

#
# @app.route('/')
# def index():
#     return 'hello world'

import MeCab

with open('models/pn.csv.m3.120408.trim.csv', encoding='utf-8') as f:
    lines = f.readlines()
    dic = {x.split('\t')[0]: x.split('\t')[1] for x in lines}

wakati = MeCab.Tagger("-Owakati")


# 文字列を受け取って形態素解析
def filter(sent):
    sentence = sent
    words = wakati.parse(sentence).split()

    for i in range(len(words)):
        judge = dic.get(words[i], '-')
        if judge == "n":
            words[i] = "にゃーん"
        # print(f'{lines[i]}: {judge}')

    return "".join(words)


@app.route('/', methods=["POST", "GET"])
def post():
    body = request.form['before']
    body = filter(body)
    return render_template('index.html', body=body)
