# -*- encoding=utf8 -*-
__author__ = "Winson"

import datetime
import time
from airtest.core.api import *
from os.path import abspath, dirname
import sys
import allure
from time import sleep
from selenium.common.exceptions import NoSuchElementException
import datetime
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from airtest.cli.parser import cli_setup
from Common.Tool import web_tool
from Element.CommonElement.CommonElement import CommonElement
from Element.Whatsapp.Whatsapp import WhatsappElement
from Element.ClientToServer.ClientToServer import Element as ClientToServer
from BLL.LoginPage.LoginPage import LoginPage
import pandas as pd
project_path = dirname(dirname(dirname(abspath(__file__))))
sys.path.append(project_path)

class Last_routing_agent_dedadicated:
        def __init__(self, driver, username, password, contact, alt_contact):
                self.airtest_driver = driver
                self.driver = web_tool(driver)
                self.common = CommonElement(driver)
                self.whatsapp = WhatsappElement(driver)
                self.login_page = LoginPage(driver)
                self.client_to_server = ClientToServer(driver)
                self.contact = contact
                self.alt_contact = alt_contact
                self.username = username
                self.password = password
                self.cookies = self.whatsapp_get_cookie()
        def whatsapp_get_cookie(self):
                self.airtest_driver.get('https://web.whatsapp.com')
                input()
                cookies = self.airtest_driver.get_cookies()
                return cookies
        def click_out_pop_up(self):
                if len(self.airtest_driver.find_elements_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div/div[3]/button[1]')) != 0:
                        self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div/div[3]/button[1]').click()
        def last_routing_agent(self):
                # 1. Whatsapp say Hi and 1
                self.airtest_driver.get('https://web.whatsapp.com')
                self.whatsapp.search_for_contact(self.contact, alt_contact=self.alt_contact)
                self.whatsapp.client_whatsapp_reply_send_text(message="Hey, this is a last routing agent test")
                time.sleep(20)
                self.whatsapp.client_whatsapp_reply_send_text(message="1")
                # 2. Login
                self.airtest_driver.get('https://here2serve--uatc.sandbox.my.salesforce.com/?login')
                LoginPage(self.airtest_driver).login(self.username, self.password)
                # 3. Salesforce accept case
                self.click_out_pop_up()
                self.common.click_app_launcher('Service Console')
                self.click_out_pop_up()
                self.airtest_driver.get('https://here2serve--uatc.sandbox.lightning.force.com/lightning/o/Case/list?filterName=00BBU000000blxd2AA')
                self.click_out_pop_up()
                self.common.close_all_tabs()
                # 4. Get info from page
                row_list = self.airtest_driver.find_element_by_css_selector('.slds-table--resizable-cols.uiVirtualDataTable').find_element_by_tag_name('tbody')
                dict_info = {
                        'Case_origin_before': row_list.find_elements_by_tag_name('tr')[0].find_elements_by_css_selector('.slds-cell-edit.cellContainer')[9].text,
                        'Owner_name_before': row_list.find_elements_by_tag_name('tr')[0].find_elements_by_css_selector('.slds-cell-edit.cellContainer')[12].text
                }
                # 5. Accept case and close case
                self.client_to_server.toggle_omni_channel()
                self.client_to_server.online_omni_channel()
                self.client_to_server.accept_omni_channel_case()
                self.client_to_server.toggle_omni_channel()
                self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-communication_-case_record_page___-case___-v-i-e-w/forcegenerated-flexipage_communication_case_record_page_case__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three-col-template-desktop2/div/div/div/flexipage-record-home-scrollable-column[2]/slot/slot/flexipage-component2[1]/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/flexipage-tab2[1]/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/div[1]/div[1]/div/select/option[14]').click()
                button = self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-communication_-case_record_page___-case___-v-i-e-w/forcegenerated-flexipage_communication_case_record_page_case__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three-col-template-desktop2/div/div/div/flexipage-record-home-scrollable-column[2]/slot/slot/flexipage-component2[1]/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/flexipage-tab2[1]/slot/flexipage-component2/slot/flexipage-aura-wrapper').find_element_by_xpath(
                        '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-communication_-case_record_page___-case___-v-i-e-w/forcegenerated-flexipage_communication_case_record_page_case__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three-col-template-desktop2/div/div/div/flexipage-record-home-scrollable-column[2]/slot/slot/flexipage-component2[1]/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/flexipage-tab2[1]/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/div[2]').find_element_by_css_selector('.slds-button')
                self.airtest_driver.execute_script('arguments[0].click()', button)
                # 5. Whatsapp say Hi
                self.airtest_driver.get('https://web.whatsapp.com')
                self.whatsapp.search_for_contact(self.contact, alt_contact=self.alt_contact)
                self.whatsapp.client_whatsapp_reply_send_text(message="Second Hi!")
                # 6. Get info from Case page
                self.airtest_driver.get('https://here2serve--uatc.sandbox.lightning.force.com/lightning/o/Case/list?filterName=00BBU000000blxd2AA')
                self.click_out_pop_up()
                self.common.close_all_tabs()
                row_list = self.airtest_driver.find_element_by_css_selector('.slds-table--resizable-cols.uiVirtualDataTable').find_element_by_tag_name('tbody')
                dict_info['Case_origin_after'] = row_list.find_elements_by_tag_name('tr')[0].find_elements_by_css_selector('.slds-cell-edit.cellContainer')[9].text,
                dict_info['Owner_name_after'] = row_list.find_elements_by_tag_name('tr')[0].find_elements_by_css_selector('.slds-cell-edit.cellContainer')[12].text
                # 8. Whatsapp Logout
                self.airtest_driver.get('https://web.whatsapp.com')
                self.airtest_driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/header/div[2]/div/span/div[4]/div').click()
                self.airtest_driver.find_element_by_xpath('/html/body/div[1]/div/div/div[4]/header/div[2]/div/span/div[4]/span/div/ul/li[6]/div').click()
                self.airtest_driver.find_element_by_xpath('/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div[3]/div/button[2]').click()
                # 9. Print output
                print(dict_info)
        def dedicated_agent(self):
                # 1. Whatsapp say Hi and 1
                self.airtest_driver.get('https://web.whatsapp.com')
                self.whatsapp.search_for_contact('54104965', alt_contact=self.alt_contact)
                self.whatsapp.client_whatsapp_reply_send_text(message="Hey, this is a dedicated agent test")
                # 2. Login
                self.airtest_driver.get('https://here2serve--uatc.sandbox.my.salesforce.com/?login')
                LoginPage(self.airtest_driver).login(self.username, self.password)
                # 3. Salesforce accept case
                self.click_out_pop_up()
                self.common.click_app_launcher('Service Console')
                self.click_out_pop_up()
                self.airtest_driver.get(
                        'https://here2serve--uatc.sandbox.lightning.force.com/lightning/o/Case/list?filterName=00BBU000000blxd2AA')
                self.click_out_pop_up()
                self.common.close_all_tabs()
                # 4. Get info from page
                row_list = self.airtest_driver.find_element_by_css_selector(
                        '.slds-table--resizable-cols.uiVirtualDataTable').find_element_by_tag_name('tbody')
                dict_info = {
                        'Case_origin': row_list.find_elements_by_tag_name('tr')[0].find_elements_by_css_selector('.slds-cell-edit.cellContainer')[9].text,
                        'Owner_name': row_list.find_elements_by_tag_name('tr')[0].find_elements_by_css_selector('.slds-cell-edit.cellContainer')[12].text
                }
                print(dict_info)