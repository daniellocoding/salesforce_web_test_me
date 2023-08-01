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

class WaitingMessagesElement:
    def __init__(self, driver):
            self.airtest_driver = driver
            self.driver = web_tool(driver)
            self.common = CommonElement(driver)
            self.whatsapp = WhatsappElement(driver)
            self.login_page = LoginPage(driver)
            self.client_to_server = ClientToServer(driver)
            self.cookie_whatsapp = self.whatsapp_get_cookie()
    def get_bot_info(self,contact, alt_contact, username, password):
        # Login
        self.airtest_driver.get('https://here2serve--uatc.sandbox.my.salesforce.com/?login')
        LoginPage(self.airtest_driver).login(username, password)
        # Go to Sender ID
        self.airtest_driver.get('https://here2serve--uatc.sandbox.lightning.force.com/lightning/o/rsplus__Sender_Id_Registration__c/list?filterName=Recent')
        self.client_to_server.close_all_tabs()
        # Sender ID Search for number
        self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[2]/div[2]/force-list-view-manager-search-bar/div/lightning-input/div/div/input').send_keys(contact)
        self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[2]/div[2]/force-list-view-manager-search-bar/div/lightning-input/div/div/input').send_keys(Keys.ENTER)
        time.sleep(5)
        self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/tbody/tr/th/span/a').click()
        time.sleep(10)
        # Get Bot Expiry Information
        self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-sender_-i-d_-record_-page1___rsplus__-sender_-id_-registration__c___-v-i-e-w/forcegenerated-flexipage_sender_id_record_page1_rsplus__sender_id_registration__c__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-template-desktop2/div/div[1]/slot/flexipage-component2/slot/records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_rsplus__sender_id_registration__c___012000000000000aaa___compact___view___recordlayout2/records-highlights2/div[1]/div/div[3]/div/runtime_platform_actions-actions-ribbon/ul/li[4]/lightning-button-menu/button').click()
        self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-sender_-i-d_-record_-page1___rsplus__-sender_-id_-registration__c___-v-i-e-w/forcegenerated-flexipage_sender_id_record_page1_rsplus__sender_id_registration__c__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-template-desktop2/div/div[1]/slot/flexipage-component2/slot/records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_rsplus__sender_id_registration__c___012000000000000aaa___compact___view___recordlayout2/records-highlights2/div[1]/div/div[3]/div/runtime_platform_actions-actions-ribbon/ul/li[4]/lightning-button-menu/div').find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-sender_-i-d_-record_-page1___rsplus__-sender_-id_-registration__c___-v-i-e-w/forcegenerated-flexipage_sender_id_record_page1_rsplus__sender_id_registration__c__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-template-desktop2/div/div[1]/slot/flexipage-component2/slot/records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_rsplus__sender_id_registration__c___012000000000000aaa___compact___view___recordlayout2/records-highlights2/div[1]/div/div[3]/div/runtime_platform_actions-actions-ribbon/ul/li[4]/lightning-button-menu/div/div/slot/runtime_platform_actions-action-renderer[5]').click()
        iframe_element = self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div[2]/section/div/force-aloha-page/div/iframe')
        self.airtest_driver.switch_to.frame(iframe_element)
        time.sleep(10)
        bot_info = {'bot_expiry_msg': self.airtest_driver.find_element_by_xpath('/html/body/form/fieldset/div[1]/div/textarea').text}
        # Get Queue Waiting Information
        self.airtest_driver.get('https://here2serve--uatc.sandbox.lightning.force.com')
        self.airtest_driver.switch_to.default_content()
        self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-sender_-i-d_-record_-page1___rsplus__-sender_-id_-registration__c___-v-i-e-w/forcegenerated-flexipage_sender_id_record_page1_rsplus__sender_id_registration__c__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-template-desktop2/div/div[1]/slot/flexipage-component2/slot/records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_rsplus__sender_id_registration__c___012000000000000aaa___compact___view___recordlayout2/records-highlights2/div[1]/div/div[3]/div/runtime_platform_actions-actions-ribbon/ul/li[4]/lightning-button-menu/button').click()
        self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-sender_-i-d_-record_-page1___rsplus__-sender_-id_-registration__c___-v-i-e-w/forcegenerated-flexipage_sender_id_record_page1_rsplus__sender_id_registration__c__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-template-desktop2/div/div[1]/slot/flexipage-component2/slot/records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_rsplus__sender_id_registration__c___012000000000000aaa___compact___view___recordlayout2/records-highlights2/div[1]/div/div[3]/div/runtime_platform_actions-actions-ribbon/ul/li[4]/lightning-button-menu/div').find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-sender_-i-d_-record_-page1___rsplus__-sender_-id_-registration__c___-v-i-e-w/forcegenerated-flexipage_sender_id_record_page1_rsplus__sender_id_registration__c__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-template-desktop2/div/div[1]/slot/flexipage-component2/slot/records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_rsplus__sender_id_registration__c___012000000000000aaa___compact___view___recordlayout2/records-highlights2/div[1]/div/div[3]/div/runtime_platform_actions-actions-ribbon/ul/li[4]/lightning-button-menu/div/div/slot/runtime_platform_actions-action-renderer[11]').click()
        bot_info['bot_queue_msg'] = self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/section/div/div/div/form/div[1]/lightning-input-field[2]/lightning-textarea/div').text
        # Get Case Waiting Information
        self.airtest_driver.get('https://here2serve--uatc.sandbox.lightning.force.com')
        self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-sender_-i-d_-record_-page1___rsplus__-sender_-id_-registration__c___-v-i-e-w/forcegenerated-flexipage_sender_id_record_page1_rsplus__sender_id_registration__c__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-template-desktop2/div/div[1]/slot/flexipage-component2/slot/records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_rsplus__sender_id_registration__c___012000000000000aaa___compact___view___recordlayout2/records-highlights2/div[1]/div/div[3]/div/runtime_platform_actions-actions-ribbon/ul/li[4]/lightning-button-menu/button').click()
        self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-sender_-i-d_-record_-page1___rsplus__-sender_-id_-registration__c___-v-i-e-w/forcegenerated-flexipage_sender_id_record_page1_rsplus__sender_id_registration__c__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-template-desktop2/div/div[1]/slot/flexipage-component2/slot/records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_rsplus__sender_id_registration__c___012000000000000aaa___compact___view___recordlayout2/records-highlights2/div[1]/div/div[3]/div/runtime_platform_actions-actions-ribbon/ul/li[4]/lightning-button-menu/div').find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-sender_-i-d_-record_-page1___rsplus__-sender_-id_-registration__c___-v-i-e-w/forcegenerated-flexipage_sender_id_record_page1_rsplus__sender_id_registration__c__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-template-desktop2/div/div[1]/slot/flexipage-component2/slot/records-lwc-highlights-panel/records-lwc-record-layout/forcegenerated-highlightspanel_rsplus__sender_id_registration__c___012000000000000aaa___compact___view___recordlayout2/records-highlights2/div[1]/div/div[3]/div/runtime_platform_actions-actions-ribbon/ul/li[4]/lightning-button-menu/div/div/slot/runtime_platform_actions-action-renderer[12]').click()
        time.sleep(10)
        bot_info['bot_case_msg'] = self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div/div[2]/div/div/div/div/div/div/div[2]/section/div/div/div/form/lightning-input-field[2]/lightning-textarea/div/textarea').text
        print(bot_info)
        return bot_info
    def click_out_pop_up(self):
        if len(self.airtest_driver.find_elements_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div/div[3]/button[1]')) != 0:
                self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[2]/div/div[3]/button[1]').click()
    def whatsapp_get_cookie(self):
        self.airtest_driver.get('https://web.whatsapp.com')
        input()
        cookies = self.airtest_driver.get_cookies()
        return cookies
    def whatsapp_logout(self):
        self.airtest_driver.get('https://web.whatsapp.com')
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[4]/header/div[2]/div/span/div[4]/div').click()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[1]/div/div/div[4]/header/div[2]/div/span/div[4]/span/div/ul/li[6]/div').click()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[1]/div/span[2]/div/div/div/div/div/div/div[3]/div/button[2]').click()
    def test_bot_expiry(self, contact, alt_contact, username, password):
        # 1. whatsapp_send_message
        self.airtest_driver.get('https://web.whatsapp.com')
        self.whatsapp.search_for_contact(contact, alt_contact=alt_contact)
        self.whatsapp.client_whatsapp_reply_send_text(message="Hey, this is a bot expiry test")
        # 2. Login
        self.airtest_driver.get('https://here2serve--uatc.sandbox.my.salesforce.com/?login')
        LoginPage(self.airtest_driver).login(username, password)
        # 3. After 10 minutes Search for Benny's Case Automation Chat List
        time.sleep(10*60)
        self.airtest_driver.get('https://here2serve--uatc.sandbox.lightning.force.com/lightning/o/Case/list?filterName=00BBU000000blxd2AA')
        self.client_to_server.close_all_tabs()
        # 4. Case filtering
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[2]/div[3]/force-list-view-manager-button-bar/div/lightning-button-group/div/slot/lightning-button-icon-stateful[2]/span/button').click()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/a[2]').click()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/a[1]').click()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/div[1]/div[1]/div/div/div[1]/lightning-combobox/div/lightning-base-combobox/div/div[1]/button').click()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/div[1]/div[1]/div/div/div[1]/lightning-combobox/div/lightning-base-combobox/div/div[2]/lightning-base-combobox-item[128]').click()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/div[1]/div[1]/div/div/div[2]/lightning-combobox/div/lightning-base-combobox/div/div[1]/button').click()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/div[1]/div[1]/div/div/div[2]/lightning-combobox/div/lightning-base-combobox/div/div[2]/lightning-base-combobox-item[7]').click()
        self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div/input').send_keys(contact)
        self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/div[1]/div/button').click()
        time.sleep(5)
        if 'descend' not in self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/thead/tr/th[4]').get_attribute("class"):
            self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/thead/tr/th[4]/div/a').click()
        # 5. Check status and Owner
        row_list = self.airtest_driver.find_element_by_css_selector('.slds-table--resizable-cols.uiVirtualDataTable').find_element_by_tag_name('tbody')
        bot_expiry = {
            'Salesforce_Status': row_list.find_elements_by_tag_name('tr')[0].find_elements_by_css_selector('.slds-cell-edit.cellContainer')[5].text,
            'Salesforce_Owner': row_list.find_elements_by_tag_name('tr')[0].find_elements_by_css_selector('.slds-cell-edit.cellContainer')[12].text}
        # 6. Chceck last message
        self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/th/span/a').click()
        time.sleep(10)
        element = self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-communication_-case_record_page___-case___-v-i-e-w/forcegenerated-flexipage_communication_case_record_page_case__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three-col-template-desktop2/div/div/div/flexipage-record-home-scrollable-column[1]/slot/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/article/fieldset/div[3]/section')
        bot_expiry['Bot_expiry_reply'] = element.find_elements_by_tag_name('ul')[-1].text.split('\n')[0]

        time.sleep(10)
        return bot_expiry
    def test_queue_waiting(self, contact, alt_contact, username, password):
        # 1. whatsapp_send_message
        self.airtest_driver.get('https://web.whatsapp.com')
        self.whatsapp.search_for_contact(contact, alt_contact=alt_contact)
        self.whatsapp.client_whatsapp_reply_send_text(message="Hey, this is a Queue Waiting test")
        time.sleep(20)
        self.whatsapp.client_whatsapp_reply_send_text(message="1")
        # 2. Login
        self.airtest_driver.get('https://here2serve--uatc.sandbox.my.salesforce.com/?login')
        LoginPage(self.airtest_driver).login(username, password)
        # 3. After 10 minutes Search for Benny's Case Automation Chat List
        time.sleep(10*60)
        self.airtest_driver.get('https://here2serve--uatc.sandbox.lightning.force.com/lightning/o/Case/list?filterName=00BBU000000blxd2AA')
        self.client_to_server.close_all_tabs()
        # 4. Case filtering
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[2]/div[3]/force-list-view-manager-button-bar/div/lightning-button-group/div/slot/lightning-button-icon-stateful[2]/span/button').click()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/a[2]').click()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/a[1]').click()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/div[1]/div[1]/div/div/div[1]/lightning-combobox/div/lightning-base-combobox/div/div[1]/button').click()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/div[1]/div[1]/div/div/div[1]/lightning-combobox/div/lightning-base-combobox/div/div[2]/lightning-base-combobox-item[128]').click()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/div[1]/div[1]/div/div/div[2]/lightning-combobox/div/lightning-base-combobox/div/div[1]/button').click()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/div[1]/div[1]/div/div/div[2]/lightning-combobox/div/lightning-base-combobox/div/div[2]/lightning-base-combobox-item[7]').click()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div/input').send_keys(contact)
        self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/div[1]/div/button').click()
        time.sleep(10)
        if 'descend' not in self.airtest_driver.find_element_by_xpath(
                '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/thead/tr/th[4]').get_attribute(
                "class"):
            self.airtest_driver.find_element_by_xpath(
                '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/thead/tr/th[4]/div/a').click()
        # 5. Check last message
        self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/th/span/a').click()
        element = self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-communication_-case_record_page___-case___-v-i-e-w/forcegenerated-flexipage_communication_case_record_page_case__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three-col-template-desktop2/div/div/div/flexipage-record-home-scrollable-column[1]/slot/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/article/fieldset/div[3]/section/div')
        bot_queuewaiting = {'Bot_queue_waiting': element.find_elements_by_tag_name('ul')[-1].text}
        # # # 6. Close Case
        self.client_to_server.toggle_omni_channel()
        self.client_to_server.online_omni_channel()
        self.client_to_server.accept_omni_channel_case()
        self.client_to_server.toggle_omni_channel()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-communication_-case_record_page___-case___-v-i-e-w/forcegenerated-flexipage_communication_case_record_page_case__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three-col-template-desktop2/div/div/div/flexipage-record-home-scrollable-column[2]/slot/slot/flexipage-component2[1]/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/flexipage-tab2[1]/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/div[1]/div[1]/div/select/option[14]').click()
        button = self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-communication_-case_record_page___-case___-v-i-e-w/forcegenerated-flexipage_communication_case_record_page_case__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three-col-template-desktop2/div/div/div/flexipage-record-home-scrollable-column[2]/slot/slot/flexipage-component2[1]/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/flexipage-tab2[1]/slot/flexipage-component2/slot/flexipage-aura-wrapper').find_element_by_xpath(
            '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-communication_-case_record_page___-case___-v-i-e-w/forcegenerated-flexipage_communication_case_record_page_case__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three-col-template-desktop2/div/div/div/flexipage-record-home-scrollable-column[2]/slot/slot/flexipage-component2[1]/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/flexipage-tab2[1]/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/div[2]').find_element_by_css_selector(
            '.slds-button')
        self.airtest_driver.execute_script('arguments[0].click()', button)
        time.sleep(10)
        return bot_queuewaiting
    def test_case_waiting(self, contact, alt_contact, username, password):
        # whatsapp_send_message
        self.airtest_driver.get('https://web.whatsapp.com')
        self.whatsapp.search_for_contact(contact, alt_contact=alt_contact)
        self.whatsapp.client_whatsapp_reply_send_text(message="Hey, this is a Case Waiting test")
        time.sleep(20)
        self.whatsapp.client_whatsapp_reply_send_text(message="1")
        # Login
        self.airtest_driver.get('https://here2serve--uatc.sandbox.my.salesforce.com/?login')
        LoginPage(self.airtest_driver).login(username, password)
        # Omni Channel Accept Case
        time.sleep(10)
        self.click_out_pop_up()
        self.client_to_server.toggle_omni_channel()
        self.client_to_server.online_omni_channel()
        self.client_to_server.accept_omni_channel_case()
        self.client_to_server.toggle_omni_channel()
        # After 10 minutes Search for Benny's Case Automation Chat List
        time.sleep(60*10)
        self.airtest_driver.get('https://here2serve--uatc.sandbox.lightning.force.com/lightning/o/Case/list?filterName=00BBU000000blxd2AA')
        self.click_out_pop_up()
        self.client_to_server.close_all_tabs()
        time.sleep(10)
        # Case filtering
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[2]/div[3]/force-list-view-manager-button-bar/div/lightning-button-group/div/slot/lightning-button-icon-stateful[2]/span/button').click()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/a[2]').click()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/a[1]').click()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/div[1]/div[1]/div/div/div[1]/lightning-combobox/div/lightning-base-combobox/div/div[1]/button').click()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/div[1]/div[1]/div/div/div[1]/lightning-combobox/div/lightning-base-combobox/div/div[2]/lightning-base-combobox-item[128]').click()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/div[1]/div[1]/div/div/div[2]/lightning-combobox/div/lightning-base-combobox/div/div[1]/button').click()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/div[1]/div[1]/div/div/div[2]/lightning-combobox/div/lightning-base-combobox/div/div[2]/lightning-base-combobox-item[7]').click()
        self.airtest_driver.find_element_by_xpath(
            '/html/body/div[4]/div[2]/div/div[1]/div[1]/div/div/div[2]/div/div/input').send_keys(contact)
        self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div[1]/div[1]/div/button').click()
        if 'descend' not in self.airtest_driver.find_element_by_xpath(
                '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/thead/tr/th[4]').get_attribute(
                "class"):
            self.airtest_driver.find_element_by_xpath(
                '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/thead/tr/th[4]/div/a').click()
        time.sleep(10)
        # Check last message
        self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/th/span/a').click()
        element = self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-communication_-case_record_page___-case___-v-i-e-w/forcegenerated-flexipage_communication_case_record_page_case__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three-col-template-desktop2/div/div/div/flexipage-record-home-scrollable-column[1]/slot/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/article/fieldset/div[3]/section')
        time.sleep(10)
        case_waiting = {'Bot_case_waiting': element.find_elements_by_tag_name('ul')[-1].text.split('\n')[0]}
        # Close Case
        self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-communication_-case_record_page___-case___-v-i-e-w/forcegenerated-flexipage_communication_case_record_page_case__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three-col-template-desktop2/div/div/div/flexipage-record-home-scrollable-column[2]/slot/slot/flexipage-component2[1]/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/flexipage-tab2[1]/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/div[1]/div[1]/div/select/option[14]').click()
        button = self.airtest_driver.find_element_by_xpath('/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-communication_-case_record_page___-case___-v-i-e-w/forcegenerated-flexipage_communication_case_record_page_case__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three-col-template-desktop2/div/div/div/flexipage-record-home-scrollable-column[2]/slot/slot/flexipage-component2[1]/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/flexipage-tab2[1]/slot/flexipage-component2/slot/flexipage-aura-wrapper').find_element_by_xpath(
            '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force-generated__flexipage_-record-page___-communication_-case_record_page___-case___-v-i-e-w/forcegenerated-flexipage_communication_case_record_page_case__view_js/record_flexipage-desktop-record-page-decorator/div[1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three-col-template-desktop2/div/div/div/flexipage-record-home-scrollable-column[2]/slot/slot/flexipage-component2[1]/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/flexipage-tab2[1]/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/div[2]').find_element_by_css_selector(
            '.slds-button')
        self.airtest_driver.execute_script('arguments[0].click()', button)
        return case_waiting
