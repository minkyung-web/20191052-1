from flask import Flask, request, render_template, redirect, url_for, abort, session

import json
import game
import dbdb

app = Flask(__name__)

@app.route('/hello/<name>')
def hellovar(name):
    character = game.set_charact(name)
    return render_template('gamestart.html', data=character)

@app.route('/gamestart')
def gamestart():
    with open("static/save.txt", "r", encoding='utf-8') as f:
        data = f.read()
        character = json.loads(data)
        print(character)
    return "{0}님 반갑습니다. (hp {1})으로 시작합니다.".format(character["name"], character["hp"])

@app.route('/input/<int:num>')
def input_num(num):
    if num == 1:
        return "도라에몽"
    elif num == 2:
        return "진구"
    elif num == 3:
        return "퉁퉁이"
    else:
        return "없어요"

if __name__ == '__main__':
    app.run(debug=True)