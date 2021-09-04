# -*- coding: utf-8 -*-
# @Time    : 2021/9/4 20:15
# @Author  : wkRonin
# @File    :test_case.py
import requests

"""
测试用例功能模块的测试代码
"""


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
        r = requests.post(self.url)
        # 第一步，只验证接口能够发送成功
        assert r.status_code == 200

    def test_delete(self):
        """
        删除用例
        :return:
        """
        r = requests.delete(self.url)
        # 第一步，只验证接口能够发送成功
        assert r.status_code == 200

    def test_select(self):
        """
        查询用例
        :return:
        """
        r = requests.get(self.url)
        # 第一步，只验证接口能够发送成功
        assert r.status_code == 200

    def test_update(self):
        """
        更新用例
        :return:
        """
        r = requests.put(self.url)
        # 第一步，只验证接口能够发送成功
        assert r.status_code == 200

    # def test_post(self):
    #     r = requests.post(
    #         http://127.0.0.1:9123/ad
    #         , json={"teacher": "ad"})
    #     print(r.text)
