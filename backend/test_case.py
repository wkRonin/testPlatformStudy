# -*- coding: utf-8 -*-
# @Time    : 2021/9/4 20:15
# @Author  : wkRonin
# @File    :test_case.py
import requests

"""
测试用例功能模块的测试代码
"""


import requests

"""
测试用例功能模块的测试代码
"""
from backend.log_util import logger


class TestCase:
    """
    增删查改
    """

    def setup_class(self):
        self.url = "http://127.0.0.1:9123/testcase"

    def test_add(self):
        """
        增加用例
        :return:
        """
        # data = {
        #     "id": 1,
        #     "node_id": "node_id1",
        #     "remark": "备注1"
        # }
        data = {
            "id": 2,
            "node_id": ["node_id1", "node_id2"],
            "remark": "备注2"
        }
        r = requests.post(self.url, json=data)
        logger.info(r.json())
        # 第一步，只验证接口能够发送成功
        assert r.status_code == 200

    def test_select(self):
        """
        查询用例
        :return:
        """
        # 我不输入任何值做筛选，返回给我完整的列表
        # 我如果输入筛选条件，则返回给匹配的数据列表
        r = requests.get(self.url)
        logger.info(r.json())
        # 第一步，只验证接口能够发送成功
        assert r.status_code == 200
        param = {"id": 1}
        r1 = requests.get(self.url, params=param)
        logger.info(r1.json())
        assert r1.status_code == 200

    def test_update(self):
        """
        更新用例
        :return:
        """
        data = {
            "id": 2,
            "node_id": ["node_id3", "node_id5"],
            "remark": "备注3"
        }
        r = requests.put(self.url, json=data)
        logger.info(r.json())
        # 第一步，只验证接口能够发送成功
        assert r.status_code == 200

    def test_delete(self):
        """
        删除用例
        :return:
        """
        param = {"id": 1}
        r = requests.delete(self.url, params=param)
        logger.info(r.json())
        # 第一步，只验证接口能够发送成功
        assert r.status_code == 200


    # def test_post(self):
    #     r = requests.post(
    #         http://127.0.0.1:9123/ad
    #         , json={"teacher": "ad"})
    #     print(r.text)
