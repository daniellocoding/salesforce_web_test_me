# -*- encoding=utf8 -*-
__author__ = "Daniel"

import datetime

from airtest.core.api import *
from os.path import abspath, dirname
import sys
from Common.Tool import web_tool
import allure
from Element.CommonElement.CommonElement import CommonElement
from Element.Whatsapp.Whatsapp import WhatsappElement
from Element.ClientToServer.ClientToServer import Element as ClientToServer
from BLL.LoginPage.LoginPage import LoginPage
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from airtest.cli.parser import cli_setup

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
        self.client_to_server.close_all_tabs()
        # Search for Benny's Case Automation Chat List
        self.driver.find_element_by_css_selector_click('.triggerLinkText.selectedListView')
        self.airtest_driver.find_element_by_css_selector('.uiInputTextForAutocomplete.uiInput--default.uiInput--input').send_keys("Benny's Case Automation")
        search_list = self.airtest_driver.find_element_by_css_selector('.slds-dropdown__list.slds-show')
        search_list.find_element_by_css_selector('.forceVirtualAutocompleteMenuOption').click()
        time.sleep(10)
        # Get the last message from the chat list
        row_list = self.airtest_driver.find_element_by_css_selector('.slds-table--resizable-cols.uiVirtualDataTable').find_element_by_tag_name('tbody')
        dict_last_msg = {
            'Status': row_list.find_elements_by_tag_name('tr')[0].find_elements_by_css_selector('.slds-cell-edit.cellContainer')[5].text,
            'Created by': row_list.find_elements_by_tag_name('tr')[0].find_elements_by_css_selector('.slds-cell-edit.cellContainer')[12].text
        }
        print(dict_last_msg)

        # after 10 minutes
        # time.sleep(10*60)
        # row_list = self.airtest_driver.find_element_by_css_selector('.slds-table--resizable-cols.uiVirtualDataTable')
        # print(row_list.find_elements_by_tag('tr')[0].find_element_by_css_selector('.slds-truncate').text)
        # self.common.test_accept_case()
        # self.client_to_server.close_case()











