# -*- encoding=utf8 -*-
__author__ = "Issac"

import allure
import pytest
import sys
from os.path import abspath, dirname

from BLL.LoginPage.LoginPage import LoginPage
from BLL.ENameCard.ENameCard import ENameCard
from Common.Tool import web_tool

project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path)

excel_data = web_tool().excel_data('../Data/LoginData/data_ename.xlsx')


@allure.story('登录账号参数化测试')
class TestENameCard:
    @pytest.mark.parametrize(
        "username, password, list_, owner_name", excel_data)
    def test_login_parametrize(self, before, username, password, list_, owner_name):
        allure.dynamic.title("登录账号参数化测试_%s" % username)
        driver = before
        ENameCard(driver).test(username, password, list=list_, owner_name=owner_name)
