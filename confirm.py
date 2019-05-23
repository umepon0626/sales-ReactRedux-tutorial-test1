#!/usr/bin/python3.4
# -*- coding: utf-8 -*-

import cgi
import sys
import io
import time
import requests
from string import Template
from os import path


# 日本語を受信時にエラーにならないようにする為に必要。
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

form = cgi.FieldStorage()

student_id = form.getfirst('student_id')
age = form.getfirst('age')
bikou = form.getfirst('bikou')

# 入力チェック（必要な変数が送信されていない場合はエラー。）
# if 'your_name' not in form:
#     print('Content-type: text/html; charset=UTF-8')
#     print('')
#     print('your_name 名前が未入力です。')
#     payload = {'student_id': student_id, 'your_name': '名前が未入力です。', 'age': age}
#     requests.get('http://localhost:8000/cgi-bin/input.py', params=payload)
#     sys.exit()

# your_name の値を取得して変数にセット。
# your_name が複数ある場合は先頭の値を取得。
your_name = form.getfirst('your_name')

# テキストファイルとして内容を出力
li = {'student_id': student_id, 'your_name': your_name, 'age': age, 'bikou': bikou}
print('Content-type: text/html; charset=UTF-8')
print('')

# res = Response()
# f = open(path.join(path.dirname(__file__), 'templete.html'))
# t = Template(unicode(f.read(), 'utf-8', 'ignore'))

# body = t.substitute(li)
# res.set_body(body)
# print res
print(
    """
     <html>
       <head>
           <meta http-equiv=\”Content-Type\” content=\ “text/html
           charset=utf-8\” / >
       </head>
     <body>
        <p>お名前:{0[your_name]}</p>
        <p>学籍番号:{0[student_id]}</p>
        <p>年齢:{0[age]}</p>
        <p>備考:{0[bikou]}</p>
        <p>以上の内容で登録しますか？</p>
        <p>登録される場合はokを押してください</p>
        <a href='http://localhost:8000/cgi-bin/complete.py?student_id={0[student_id]}&your_name={0[your_name]}&age={0[age]}&bikou={0[bikou]}'>ok</a>
     </body>
     """.format(li)
)
