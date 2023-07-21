# -*- encoding=utf8 -*-
# Case 2
__author__ = "Issac"

import allure
import pytest
import sys
from os.path import abspath, dirname

from BLL.LoginPage.LoginPage import LoginPage
from BLL.ClientToServer.ClientToServer import ClientToServer
from Common.Tool import web_tool

project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path)

excel_data = web_tool().excel_data('../Data/LoginData/data.xlsx')


@allure.story('登录账号参数化测试')
class TestFreeTextMessaging:

    @pytest.mark.parametrize(
        "username, password, sender_phone_no, receiver_phone_number, sender_id, whatsapp_contact_no, whatsapp_alt_contact", excel_data)
    def test_free_text_messaging(self, before, username, password, sender_phone_no, receiver_phone_number, sender_id, whatsapp_contact_no, whatsapp_alt_contact):
        driver = before

        # first part + switched browser
        driver.get("http://web.whatsapp.com")
        windows_id = ClientToServer(driver).client_to_server_test_first_part(contact=whatsapp_contact_no, alt_contact=whatsapp_alt_contact)

        # second part
        allure.dynamic.title("登录账号参数化测试_%s" % username)
        driver.get('https://here2serve--uatc.sandbox.my.salesforce.com/?login')
        LoginPage(driver).login(username, password)

        # third part
        ClientToServer(driver).free_text_messaging_test()
