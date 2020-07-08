import time

import pytest
from selenium import webdriver
from lib.util import loginAndCheck

class Test_错误登录:

    def test_UI_0001(self):
        print('\n用例UI_0001')

        alertText = loginAndCheck(None,'88888888')

        assert alertText == "请输入用户名"

    def test_UI_0002(self):
        print('\n用例UI_0002')

        alertText = loginAndCheck('byhy', None)

        assert alertText == '请输入密码'

    def test_UI_0003(self):
        print('\n用例UI_0003')

        alertText = loginAndCheck('byh', '88888888')

        assert alertText == '登录失败 : 用户名或者密码错误'




