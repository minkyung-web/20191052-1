from flask import Flask, request, render_template, redirect, url_for, abort, session
import dbdb
import game
import json

app = Flask(__name__)

app.secret_key = b'aaa!111/'

# 메인페이지

@app.route('/')
def index():
    return render_template('main.html')

# 게임

@app.route('/gameplay')
def gameplay():
    name = session['user']
    character = game.set_charact(name)
    return render_template('gamestart.html', data = character)

@app.route('/input/<int:num>')
def input_num(num):
    if num == 1:
        menu = "햄버거"
        return render_template('game.html', data = menu)
    elif num == 2:
        menu = "아이스크림"
        return render_template('game.html', data = menu)
    elif num == 3:
        menu = "감자튀김"
        return render_template('game.html', data = menu)
    elif num == 4:
        menu = "해파리버거"
        return render_template('game.html', data = menu)
    elif num == 5:
        menu = "플랑크톤버거"
        return render_template('game.html', data = menu)
    elif num == 6:
        menu = "게살버거"
        return render_template('game.html', data = menu)
    elif num == 7:
        menu = "딸기아이스크림"
        return render_template('game.html', data = menu)
    elif num == 8:
        menu = "초코아이스크림"
        return render_template('game.html', data = menu)
    elif num == 9:
        menu = "민트아이스크림"
        return render_template('game.html', data = menu)
    else:
        return "없어요."

#로그인

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        print(id,type(id))
        print(pw,type(pw))
        ret = dbdb.select_user(id, pw)
        print(ret)
        if ret != None:
            session['user'] = id
            return render_template('main.html')
        else:
            return redirect(url_for('login'))

#회원가입

@app.route('/join', methods=['GET', 'POST'])
def join():
    if request.method == 'GET':
        return render_template('join.html')
    else:
        id = request.form['id']
        pw = request.form['pw']
        name = request.form['name']
        print(id,type(id))
        print(pw,type(pw))
        ret = dbdb.check_id(id)
        if ret != None:
            return'''
                     <script>alert('이미 아이디를 사용중입니다.');
                     location.href='/join';
                     </script>
                  '''
        else:
            dbdb.insert_user(id, pw, name)
            return'''
                     <script>alert('회원가입이 완료 되었습니다.');
                     location.href='/login';
                     </script>
                  '''

#학생정보조회
@app.route('/getinfo')
def getinfo():
    if 'user' in session:
        info = dbdb.select_all()
        return render_template("getinfo.html", data=info)
    return'''
            <script>alert('로그인 후 이용하세요');
                 location.href='/login';
            </script>
           '''
#로그아웃
@app.route('/logout')
def logout():
    session.pop('user', None)
    return redirect(url_for('login'))

@app.errorhandler(404)
def page_not_found(error):
    return "페이지가 없습니다. URL를 확인 하세요", 404

if __name__ == '__main__':
    app.run(debug=True)