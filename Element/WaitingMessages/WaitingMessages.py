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
from Element.ClientToServer.ClientToServer import Element as ClientToServer
from BLL.LoginPage.LoginPage import LoginPage
from time import sleep

project_path = dirname(dirname(dirname(abspath(__file__))))
sys.path.append(project_path)


class WaitingMessagesElement:
    def __init__(self, driver):
        self.airtest_driver = driver
        self.driver = web_tool(driver)
        self.common = CommonElement(driver)
        self.whatsapp = WhatsappElement(driver)
        self.login_page = LoginPage(driver)
        self.client_to_server = ClientToServer(driver)

    @allure.step("Test Bot Expiry")
    def test_bot_expiry(self, contact, alt_contact, username, password):
        # whatsapp
        # self.whatsapp.search_for_contact(contact, alt_contact=alt_contact)
        # self.whatsapp.client_whatsapp_reply_send_text(message="Hey, this is a case waiting test")
        # sleep(10)
        # whatsapp_last_message_xpath = '/html/body/div[1]/div/div/div[5]/div/div[2]/div/div[2]/div[3]/div[last()]/div/div/div/div[1]/div[1]/div[1]/div/span[1]/span'
        # self.driver.assert_element(whatsapp_last_message_xpath, "UATA csl testing bot")
        # print(self.driver.find_element_by_xpath(whatsapp_last_message_xpath).text)
        # salesforce
        self.common.click_app_launcher("Service Console")
        self.common.click_app_launcher("Cases")
        self.driver.find_element_by_xpath_click('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div')
        self.driver.find_element_by_xpath_send_keys('/html/body/div[4]/div[2]/div[1]/div/div[1]/div/div/input','Benny\'s Case Automation')
        self.driver.find_element_by_xpath_click('/html/body/div[4]/div[2]/div[1]/div/div[1]/div/div/div/div/div[1]/div/ul/li[1]')

        self.common.test_accept_case()
        self.client_to_server.close_case()
        self.client_to_server.close_all_tabs()










