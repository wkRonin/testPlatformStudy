# -*- coding: utf-8 -*-
# @Time    : 2021/9/4 20:29
# @Author  : wkRonin
# @File    :server.py
import json

from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from backend.log_util import logger

from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)
# # get请求
# @app.route("/testcase", methods=["get"])
# def select_case():
#     return {"code": 0, "msg": "get success"}
#
#
# @app.route("/testcase", methods=["post"])
# def post_case():
#     return {"code": 0, "msg": "post success"}
#
#
# @app.route("/testcase", methods=["delete"])
# def delete_case():
#     return {"code": 0, "msg": "delete success"}
#
#
# @app.route("/testcase", methods=["put"])
# def put_case():
#     return {"code": 0, "msg": "put success"}


username = "root"
pwd = "password"
ip = "127.0.0.1"
port = 3306
database = "test"
app.config['SQLALCHEMY_DATABASE_URI'] = \
    f'mysql+pymysql://{username}:{pwd}@{ip}:{port}/{database}?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class TestCase(db.Model):
    # __table__ = "client"
    id = db.Column(db.Integer, primary_key=True)
    node_id = db.Column(db.String(80), nullable=False)
    remark = db.Column(db.String(120))

    def as_dict(self):
        return {
            "id": self.id,
            "node_id": self.node_id,
            "remark": self.remark
        }


class TestCaseServer(Resource):

    def get(self):
        '''
        测试用例的查找
        :return:
        '''
        case_id = request.args.get("id")
        logger.info(f"接收到的参数id <==== {case_id}")
        if case_id:
            case_data = TestCase.query.filter_by(id=case_id).first()
            if case_data:
                # datas = [{"id": case_data.id, "node_id": case_data.node_id, "remark": case_data.remark}]
                datas = [case_data.as_dict()]
            else:
                datas = []
        else:
            case_datas = TestCase.query.all()
            # datas = [{"id": case_data.id, "node_id": case_data.node_id, "remark": case_data.remark} for case_data in
            #          case_datas]
            datas = [case_data.as_dict() for case_data in case_datas]
        logger.info(f"将要返回的内容 ====> {datas}")
        return {"code": 0, "msg": {"data": datas}}

    def post(self):
        '''
        测试用例的新增
        :return:
        '''
        # 获取调用该接口传入的json数据
        case_data = request.json
        logger.info(f"接收到的参数 <==== {case_data}")
        # 获取调用该接口传入的json数据中的id
        case_id = case_data.get("id")
        # 使用数据体中的id进行查询，查询到了则使用下述的else逻辑
        exist = TestCase.query.filter_by(id=case_id).first()
        logger.info(f"此id已存在 ====> {exist}")
        # 不存在的时候进行数据的新增操作
        if not exist:
            testcase = TestCase(**case_data)
            # 处理不符合字符串的格式的内容 转换成json字符串
            testcase.node_id = json.dumps(case_data.get("node_id"))
            db.session.add(testcase)
            db.session.commit()
            logger.info(f"将要返回的内容 ====> Case id {case_id} success add")
            return {"code": 0, "msg": f"Case id {case_id} success add"}
        else:
            return {"code": 40001, "msg": f"Case is exist"}

    def put(self):
        '''
        测试用例的修改
        :return:
        '''
        case_data = request.json
        logger.info(f"接收到的参数 <==== {case_data}")
        # 获取调用该接口传入的json数据中的id
        case_id = case_data.get("id")
        # 使用数据体中的id进行查询，查询到了则使用下述的else逻辑
        exist = TestCase.query.filter_by(id=case_id).first()
        logger.info(f"{exist}")
        if exist:
            case_data['node_id'] = json.dumps(case_data.get("node_id"))
            TestCase.query.filter_by(id=case_id).update(case_data)
            db.session.commit()
            logger.info(f"将要返回的内容 ====> Case id {case_id} success change to {case_data}")
            return {"code": 0, "msg": f"Case id {case_id} success change to {case_data}"}
        else:
            return {"code": 40002, "msg": f"Case is not exist"}

    def delete(self):
        '''
        测试用例的删除
        :return:
        '''
        case_id = request.args.get("id")
        logger.info(f"接收到的参数id <==== {case_id}")
        if not case_id:
            return {"code": 40003, "msg": "Delete case_id must not null"}
        exist = TestCase.query.filter_by(id=case_id).first()
        logger.info(f"{exist}")
        if exist:
            TestCase.query.filter_by(id=case_id).delete()
            db.session.commit()
            return {"code": 0, "msg": f"Case id {case_id} success delete"}
        else:
            return {"code": 40002, "msg": f"Case is not exist"}


class TaskServer(Resource):

    def get(self):
        logger.info("task get method ")


api.add_resource(TestCaseServer, '/testcase')
api.add_resource(TaskServer, '/task')


if __name__ == '__main__':
    # db.create_all()
    app.run(debug=True, host='127.0.0.1', port=9123)
