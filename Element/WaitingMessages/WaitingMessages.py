# -*- encoding=utf8 -*-
__author__ = "Daniel"

import datetime

from airtest.core.api import *
# from airtest.cli.parser import cli_setup
from os.path import abspath, dirname
import sys

from selenium.common.exceptions import NoSuchElementException
# import datetime

from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC

from Common.Tool import web_tool
import allure
from Element.CommonElement.CommonElement import CommonElement
from Element.Whatsapp.Whatsapp import WhatsappElement
from BLL.LoginPage.LoginPage import LoginPage
from time import sleep

project_path = dirname(dirname(dirname(abspath(__file__))))
sys.path.append(project_path)


class WaitingMessagesElement:
    def __init__(self, driver):
        self.airtest_driver = driver
        self.driver = web_tool(driver)
        self.ce = CommonElement(driver)
        self.we = WhatsappElement(driver)
        self.login_page = LoginPage(driver)

    @allure.step("Enter ")

    @allure.step("Test Bot Expiry")
    def test_bot_expiry(self, contact, alt_contact):
        self.we.search_for_contact(contact, alt_contact=alt_contact)
        self.we.client_whatsapp_reply_send_text(message="Hey, this is a case waiting test")

        # wait and login to uatc
        sleep(10*60)
        self.login_page.login()








