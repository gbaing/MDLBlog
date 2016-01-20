# -*- coding: utf-8 -*-
"""
Create on 2016/1/20

@Author:MinRui

@Module Description:
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/test1')
def test01():
    return "This is test1"

if __name__ == '__main__':
    app.run()
