# -*- encoding=utf8 -*-
__author__ = "Issac"
import time
import allure
import pytest
import sys
from os.path import abspath, dirname
from selenium.webdriver.common.by import By
from BLL.LoginPage.LoginPage import LoginPage
from Common.Tool import web_tool
from BLL.WaitingMessages.WaitingMessages import WaitingMessages

project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path)

excel_data = web_tool().excel_data('../Data/LoginData/data.xlsx')

@allure.story('登录账号参数化测试')
class TestWaitMessages:
    @pytest.mark.parametrize(
        "username, password, sender_phone_no, receiver_phone_number, sender_id, whatsapp_contact_no, whatsapp_alt_contact", excel_data)
    def test_wait_messages(self, before, username, password, sender_phone_no, receiver_phone_number, sender_id, whatsapp_contact_no, whatsapp_alt_contact):
        driver = before
        allure.dynamic.title("登录账号参数化测试_%s" % username)
        # driver.get('https://web.whatsapp.com')
        # time.sleep(10)
        driver.get('https://here2serve--uatc.sandbox.my.salesforce.com/?login')
        LoginPage(driver).login(username, password)
        time.sleep(5)
        WaitingMessages(driver).test_bot_expiry_queue_wait_case_wait(contact=whatsapp_contact_no, alt_contact=whatsapp_alt_contact, username=username, password=password)






