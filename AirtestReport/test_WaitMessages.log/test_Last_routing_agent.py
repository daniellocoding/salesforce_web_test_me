# -*- encoding=utf8 -*-
__author__ = "Winson"
import time
import allure
import pytest
import sys
from os.path import abspath, dirname
from selenium.webdriver.common.by import By
from BLL.LoginPage.LoginPage import LoginPage
from Common.Tool import web_tool
from Element.Last_routing_agent.Last_routing_agent import Last_routing_agent_dedadicated

project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path)
excel_data = web_tool().excel_data('../Data/LoginData/data.xlsx')

@allure.story('登录账号参数化测试')
class TestLastRouting_Dedadicated:
    @pytest.mark.parametrize("username, password, sender_phone_no, receiver_phone_number, sender_id, whatsapp_contact_no, whatsapp_alt_contact", excel_data)
    def test_last_routing_dedadicated(self, before, username, password, sender_phone_no, receiver_phone_number, sender_id, whatsapp_contact_no, whatsapp_alt_contact):
        driver = before
        allure.dynamic.title("登录账号参数化测试_%s" % username)
        obj = Last_routing_agent_dedadicated(driver, username, password, whatsapp_contact_no, whatsapp_alt_contact)
        last_routing = obj.last_routing_agent()
        # dedicated = obj.dedicated_agent()
        print(f"Last_routing: {last_routing}")
        # print(f"Dedicated: {dedicated}")
