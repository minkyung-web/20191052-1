import sqlite3

def dbcon():
    return sqlite3.connect('logindb.db')

def create_table():
    try:
        db = dbcon()
        c = db.cursor()
        c.execute("CREATE TABLE student (id varchar(50), pw varchar(50), name varchar(50))")
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def insert_data(id, pw, name):
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (id, pw, name)
        c.execute("INSERT INTO student VALUES (?, ?, ?)", setdata)
        db.commit()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()

def select_all():
    ret = list()
    try:
        db = dbcon()
        c = db.cursor()
        c.execute('SELECT * FROM student')
        ret = c.fetchall()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
        return ret

def select_id(id):
    ret = ()
    try:
        db = dbcon()
        c = db.cursor()
        setdata = (num,)
        c.execute('SELECT * FROM student WHERE id = ?', setdata)
        ret = c.fetchone()
    except Exception as e:
        print('db error:', e)
    finally:
        db.close()
        return ret

#dbcon()
#create_table()
#insert_data('aa', '1234', 'mm')
#ret = select_all()
#print(ret)