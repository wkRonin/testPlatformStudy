# -*- coding: utf-8 -*-
# @Time    : 2021/9/4 19:57
# @Author  : wkRonin
# @File    :flask_demo.py
# 路由定义
# 设定请求方法
# 获取请求参数
# 获取请求体

# 不要import requests ~!!!!!!!!!!!!
from flask import Flask, request

# 实例化Flask，获取实例对象app
app = Flask(__name__)


# 路由定义, 第一个参数传递path
@app.route("/")
# 路由对应的方法，当启动服务之后，每次访问上面定义的路由/ 的时候，就会执行函数内的方法
def flask_demo():
    # 获取url中的参数内容
    app.logger.info(f"url中的参数内容为{request.args}")
    # 通过get 获取键值对对应的value
    # print(request.args.get("ad"))
    # 接口的响应值，对应的就是return的内容
    return f"my_ad_data is {request.args.get('ad')}"


# 通过methods 参数指定此接口支持的请求方法
@app.route("/ad", methods=["get", "post"])
# 路由对应的方法，当启动服务之后，每次访问上面定义的路由/ 的时候，就会执行函数内的方法
def hogwarts():
    # 获取url中的参数内容
    # app.logger.info(f"url中的参数内容为{request.args}")
    # 通过get 获取键值对对应的value
    # print(request.args.get("ad"))
    app.logger.info(f'请求体为{request.json}')
    # 接口的响应值，对应的就是return的内容
    return "VN"


if __name__ == '__main__':
    # 使用debug模式启动服务，可以热加载
    app.run(debug=True, host='127.0.0.1', port=9123)

