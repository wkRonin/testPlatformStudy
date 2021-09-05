# -*- coding: utf-8 -*-
# @Time    : 2021/9/5 15:22
# @Author  : wkRonin
# @File    :sql_demo.py
# 导入flask和flask_sqlalchemy
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 实例化flask
app = Flask(__name__)
# 进行数据库的配置
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# 数据库的用户名
username = "root"
# 数据库的密码
pwd = "password"
# 数据库的ip地址
ip = "127.0.0.1"
# 数据库的端口
port = 3306
# 数据库的库名
database = "test"
# 设置mysql 数据库的连接
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# sqlalcchemy绑定app
db = SQLAlchemy(app)


# 每个类表示的是一张表
class User(db.Model):
    # 每一个类的变量表示数据库的一个表头
    # db.Column定义表头格式  类型  primary_key是否主键
    id = db.Column(db.Integer, primary_key=True)
    # 字符串  括号里边是最大的长度 unique 是否允许重复，nullable 是否允许为空
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    gender = db.Column(db.String(10))

    # 魔法方法 定义打印的格式
    def __repr__(self):
        return '<User %r>' % self.username


if __name__ == '__main__':
    # 新建表
    # db.create_all()
    # 删除表
    # db.drop_all()
    # 数据的增删改查
    # 新增数据
    # user1 = User(id=1, username="张三", email="123456@123.com", gender="男")

    # # 对数据库的数据有改变操作的话，必须要进行commit
    # db.session.commit()
    # user2 = User(id=2, username="张四", email="123451@123.com", gender="男")
    # user3 = User(id=3, username="张五", email="123452@123.com", gender="男")
    # user4 = User(id=4, username="张六", email="123453@123.com", gender="男")
    # user5 = User(id=5, username="张七", email="123454@123.com", gender="男")
    # 操作类似于git   add操作相当于git的commit  commit 相当于git的push
    # db.session.add(user1)
    # db.session.add(user2)
    # db.session.add(user3)
    # db.session.add_all([user4,user5])
    # db.session.add(user2)
    # db.session.commit()
    # res = User.query.filter_by(id=1).first()
    # print(res.username, res.email, res.gender)
    # res = User.query.all()
    # print(res)
    # res = db.session.query(User.username, User.email, User.gender).filter(User.id==1).first()
    # print(res)
    # 修改操作
    # 两种写法  第一种
    # res = User.query.filter_by(id=1).first()
    # res.gender = "女"
    # 第二种写法
    User.query.filter_by(id=2).update({"gender": "女"})
    db.session.commit()
    # 删除操作
    # User.query.filter_by(id=3).delete()
    # db.session.commit()
