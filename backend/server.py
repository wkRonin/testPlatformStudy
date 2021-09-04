# -*- coding: utf-8 -*-
# @Time    : 2021/9/4 20:29
# @Author  : wkRonin
# @File    :server.py
from flask import Flask, request

app = Flask(__name__)


# get请求
@app.route("/testcase", methods=["get"])
def select_case():
    return {"code": 0, "msg": "get success"}


@app.route("/testcase", methods=["post"])
def post_case():
    return {"code": 0, "msg": "post success"}


@app.route("/testcase", methods=["delete"])
def delete_case():
    return {"code": 0, "msg": "delete success"}


@app.route("/testcase", methods=["put"])
def put_case():
    return {"code": 0, "msg": "put success"}


if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=9123)
