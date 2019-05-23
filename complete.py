#! /usr/bin/env python3
import cgi
import os
import sys
import io
import sqlite3

# データベースに接続する
form = cgi.FieldStorage()
student_id = form['student_id'].value
your_name = form['your_name'].value
age = form['age'].value
bikou = form['bikou'].value

conn = sqlite3.connect('example.db')
c = conn.cursor()
# c.execute(
#     '''CREATE TABLE users(student_id real, your_name text, age text, bikou text)''')
# data = [(f'{student_id}', f'{your_name}', f'{age}')]
# c.executemany('INSERT INTO users VALUES (?,?,?)', data)
sql = 'insert into users (student_id, your_name, age, bikou) values (?,?,?,?)'
user = (f'{student_id}', f'{your_name}', f'{age},', f'{bikou}')
c.execute(sql, user)

conn.commit()

# windowsにおける文字化け回避
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 以下のコードを書かないと、htmlとして読み込んでもらえない。
print('Content-type:text/html;charset=utf-8')

# htmlの部分
print(
    """
     <html>
       <head>
           <meta http-equiv=\”Content-Type\” content=\ “text/html
           charset=utf-8\” / >
       </head>
     <body>
       <p>保存に成功しました。<P>
       <a href='http://localhost:8000/cgi-bin/index.py'>go to index page</a>
     </body>
     """
)
