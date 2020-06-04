import sqlite3
conn = sqlite3.connect('mydb.db')

# Cursor 객체 생성
c = conn.cursor()

# 테이블 생성
c.execute("CREATE TABLE student (num varchar(50), name varchar(50))")
    
# execute 에 db 에 적용
conn.commit()

# 접속한 db 닫기
conn.close()