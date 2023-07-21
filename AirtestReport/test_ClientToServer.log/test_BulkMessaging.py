# -*- encoding=utf8 -*-
# Case 1
__author__ = "Issac"

import allure
import pytest
import sys
from os.path import abspath, dirname

from BLL.LoginPage.LoginPage import LoginPage
from BLL.ServerToClient.ServerToClient import ServerToClient
from Common.Tool import web_tool

project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path)

excel_data = web_tool().excel_data('../Data/LoginData/data.xlsx')


@allure.story('登录账号参数化测试')
class TestBulkMessaging:
    @pytest.mark.parametrize(
        "username, password, sender_phone_no, receiver_phone_number, sender_id, whatsapp_contact_no, whatsapp_alt_contact", excel_data)
    def test_bulk_messaging(self, before, username, password, sender_phone_no, receiver_phone_number, sender_id, whatsapp_contact_no, whatsapp_alt_contact):
        driver = before

        allure.dynamic.title("登录账号参数化测试_%s" % username)
        driver.get('https://here2serve--uatc.sandbox.my.salesforce.com/?login')
        LoginPage(driver).login(username, password)

        ServerToClient(driver).test_bulk_messaging(sender_id=sender_id, sender_phone_no=sender_phone_no, phone_number_strings=receiver_phone_number)



