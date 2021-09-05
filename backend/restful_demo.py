# -*- coding: utf-8 -*-
# @Time    : 2021/9/5 15:22
# @Author  : wkRonin
# @File    :restful_demo.py
# 导入 flask的库
# 从flask-restful中导入 Resource和 Api
from flask import Flask
from flask_restful import Resource, Api

# 进行flask的实例化一级绑定app实例到api
app = Flask(__name__)
api = Api(app)


# 定义一个类实现hello
class HelloWorld(Resource):
    # 编写get方法做的事情
    def get(self):
        return {'hello': 'world'}


# 进行资源的绑定
api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=9123)
