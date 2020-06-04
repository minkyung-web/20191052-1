from flask import Flask, request, render_template, redirect, url_for, abort

import json
import game
import dbdb
import db

app = Flask(__name__)



@app.route('/')
def index():
    return '메인페이지'

@app.route('/hello/')
def hello():
    return 'Hello, World!'

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


@app.route('/senddata')
def senddata():
    name = 'world'
    return render_template('senddata.html', data=name)


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

@app.route('/aa')
def aa():
    return render_template('sign.html')

@app.route('/form')
def form():
    return render_template('test.html')

@app.route('/method', methods=['GET', 'POST'])
def method():
    if request.method == 'GET':
        return 'GET 으로 전송이다.'
    else:
        num = request.form['num']
        name = request.form['name']
        print(num, name)
        dbdb.insert_data(num, name)
        return 'POST 이다. 학번은: {} 이름은: {}'.format(num, name)

@app.route('/getinfo')
def getinfo():
    ret = dbdb.select_all()
    print(ret)
    return render_template('getinfo.html', data=ret)
    #return '번호 : {}, 이름 : {}'.format(ret[0], ret[1])


@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/check', methods=['POST'])
def check():
    id = request.form['id']
    pw = request.form['pw']
    if id == 'abc':
        if pw == '1234':
            return '맞다.'
        else:
            return '틀리다.'
    else:
        return '틀리다.'


@app.route('/move/<name>')
def move(name):
    if name == 'naver':
        return redirect(url_for('naver'))
    elif name == 'daum':
        return redirect(url_for('daum'))
    else:
        abort(404)

@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL를 확인 하세요", 404

@app.route('/naver')
def naver():
    return redirect("https://www.naver.com/")

@app.route('/daum')
def daum():
    return redirect("https://www.daum.net/")


@app.route('/img')
def img():
    return render_template("image.html")



if __name__ == '__main__':
    app.run(debug=True)