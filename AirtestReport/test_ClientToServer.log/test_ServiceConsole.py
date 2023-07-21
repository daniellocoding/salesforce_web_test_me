# -*- encoding=utf8 -*-
__author__ = "Issac"

import allure
import pytest
import sys
from os.path import abspath, dirname

from BLL.LoginPage.LoginPage import LoginPage
from BLL.ServiceConsolePage.ServiceConsolePage import ServiceConsolePage
from Common.Tool import web_tool

project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path)

excel_data = web_tool().excel_data('../Data/LoginData/data.xlsx')


@allure.story('登录账号参数化测试')
class TestServiceConsole:
    @pytest.mark.parametrize(
        "username, password, sender_phone_no, receiver_phone_number, sender_id, whatsapp_contact_no", excel_data)
    def test_login_parametrize(self, before, username, password, sender_phone_no, receiver_phone_number, sender_id, whatsapp_contact_no):
        allure.dynamic.title("登录账号参数化测试_%s" % username)
        driver = before
        driver.get('https://here2serve--uatc.sandbox.my.salesforce.com/?login')
        LoginPage(driver).login(username, password)

    def test_service_console(self, before):
        driver = before
        ServiceConsolePage(driver).test()

