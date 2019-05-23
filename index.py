#! /usr/bin/env python3
import sys
import io
import sqlite3

# windowsにおける文字化け回避
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 以下のコードを書かないと、htmlとして読み込んでもらえない。


# htmlの部分
# print(
#     """
#      <html>
#        <head>
#            <meta http-equiv=\”Content-Type\” content=\ “text/html
#            charset=utf-8\” / >
#        </head>
#      <body>
#        <a href='http://localhost:8000/cgi-bin/input.py'>create new record</a>
#      </body>
#      """
# )

# データベースに接続する

mojiretu = """<h1>リスト</h1>"""

conn = sqlite3.connect('example.db')
c = conn.cursor()


# レコードを生年月日の降順で取得する
for row in c.execute('SELECT * FROM users ORDER BY student_id DESC'):
    a = """<h1>学籍番号:{0[0]}\n氏名:{0[1]}\n年齢:{0[2]}\n備考:{0[3]}</h1>""".format(row)
    mojiretu = mojiretu + a
# データベースへのアクセスが終わったら close する
conn.close()
print('Content-type:text/html;charset=utf-8')
print("""
     <html>
       <head>
           <meta http-equiv=\”Content-Type\” content=\ “text/html
           charset=utf-8\” / >
       </head>
     <body>
       <a href='http://localhost:8000/cgi-bin/input.py'>create new record</a>
       """ + mojiretu + """ </body>
     """)
