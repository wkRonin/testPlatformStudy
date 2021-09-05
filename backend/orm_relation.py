# -*- coding: utf-8 -*-
# @Time    : 2021/9/5 17:32
# @Author  : wkRonin
# @File    :orm_relation.py
"""
多表查询demo
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# 实例化flask
app = Flask(__name__)
# 进行数据库的配置
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
# 数据库的用户名
username = "root"
# 数据库的密码
pwd = "zwk.912370908"
# 数据库的ip地址
ip = "47.100.50.226"
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


class UserInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.Integer)
    ut = db.relationship('UserType')


class UserType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    user_info_id = db.Column(db.Integer, db.ForeignKey('user_info.id'))


if __name__ == '__main__':
    # db.create_all()
    # ui1 = UserInfo(name="张三", age=18)
    # ui2 = UserInfo(name="李四", age=28)
    # ui3 = UserInfo(name="王五", age=30)
    # ui4 = UserInfo(name="赵六", age=22)
    # ui5 = UserInfo(name="洪七", age=25)
    # ui6 = UserInfo(name="吴八", age=19)
    # db.session.add_all([ui1, ui2, ui3, ui4, ui5, ui6])
    # db.session.flush()
    # ut1 = UserType(title="管理用户", user_info_id=ui1.id)
    # ut2 = UserType(title="高级用户", user_info_id=ui1.id)
    # ut3 = UserType(title="普通用户", user_info_id=ui1.id)
    # ut4 = UserType(title="管理用户", user_info_id=ui2.id)
    # ut5 = UserType(title="高级用户", user_info_id=ui3.id)
    # ut6 = UserType(title="普通用户", user_info_id=ui4.id)
    # ut7 = UserType(title="高级用户", user_info_id=ui5.id)
    # ut8 = UserType(title="普通用户", user_info_id=ui6.id)
    # db.session.add_all([ut1, ut2, ut3, ut4, ut5, ut6, ut7, ut8])
    # db.session.commit()
    data = db.session.query(UserInfo.name, UserInfo.age, UserType.title).join(UserInfo,
                                                                              UserType.user_info_id == UserInfo.id).filter(
        UserInfo.name == "张三").all()
    print(data)
