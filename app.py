from flask import Flask, request, render_template, redirect, url_for, abort, session
import dbdb

app = Flask(__name__)

app.secret_key = b'aaa!111/'

# 메인페이지

@app.route('/')
def index():
    return render_template('main.html')

# 로그인 후 메인페이지

@app.route('/main1')
def main1():
    if 'user' in session:
        return render_template("main1.html")
    return'''
            <script>alert('로그인이 필요합니다.');
                 location.href='/login';
            </script>
           '''

# 로그인

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
            return render_template('main1.html')
        else:
            return "아이디 또는 패스워드를 확인 하세요."

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
            <script>alert('로그인이 필요합니다');
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