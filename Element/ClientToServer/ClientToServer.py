# -*- encoding=utf8 -*-
__author__ = "Issac"

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

project_path = dirname(dirname(dirname(abspath(__file__))))
sys.path.append(project_path)


class Element:
    def __init__(self, driver):
        self.airtest_driver = driver
        self.driver = web_tool(driver)

    @allure.step("Click app launcher")
    def click_app_launcher(self, service_name="Service Console"):
        sleep(3)
        xpath1 = r'/html/body/div[4]/div[1]/section/div[1]/div/div[1]/div[1]/div/div[1]/div[1]/button'
        xpath2 = r'/html/body/div[4]/div[1]/section/div[1]/div[1]/one-appnav/div/div/div/div/one-app-launcher-header/button'
        try:
            self.driver.find_element_by_xpath_click(xpath1)  # service console / sales console
            self.switch_service_in_launcher_v1(service_name)
        except NoSuchElementException:
            self.driver.find_element_by_xpath_click(xpath2)  # service / bolt solutions / others (?)
            self.switch_service_in_launcher_v2(service_name)
        sleep(3)

    @allure.step("Only hide the app launcher")
    def hide_app_launcher(self):
        sleep(3)
        xpath1 = r'/html/body/div[4]/div[1]/section/div[1]/div/div[1]/div[1]/div/div[1]/div[1]/button'
        xpath2 = r'/html/body/div[4]/div[1]/section/div[1]/div[1]/one-appnav/div/div/div/div/one-app-launcher-header/button'
        try:
            self.driver.find_element_by_xpath_click(xpath1)  # service console / sales console
        except NoSuchElementException:
            self.driver.find_element_by_xpath_click(xpath2)  # service / bolt solutions / others (?)
        sleep(3)
    @allure.step("Switch service(when clicked by xpath1)")
    def switch_service_in_launcher_v1(self, service_name="Service Console"):
        xpath1 = r'/html/body/div[4]/div[2]/div[2]/div[1]/div[2]/one-app-launcher-menu/div/one-app-launcher-search-bar/lightning-input/div/div/input'
        self.driver.find_element_by_xpath_send_keys(xpath1, service_name + ' ')
        self.driver.find_element_by_xpath_send_keys(xpath1, Keys.ENTER)
        sleep(5)
        if service_name.lower() != "cases":
            xpath2 = r'/html/body/div[4]/div[1]/section/div[1]/div/div[1]/div[1]/div/div[1]/div[2]/span'
            self.driver.assert_element(xpath2, service_name)

    @allure.step("Switch service(when clicked by xpath2)")
    def switch_service_in_launcher_v2(self, service_name="Service Console"):
        xpath2 = '/html/body/div[4]/div[2]/div/div[1]/div[2]/one-app-launcher-menu/div/one-app-launcher-search-bar/lightning-input/div/div/input'
        #xpath2 = r'/html/body/div[4]/div[2]/div[4]/div[1]/div[2]/one-app-launcher-menu/div/one-app-launcher-search-bar/lightning-input/div/div/input'
        self.driver.find_element_by_xpath_send_keys(xpath2, service_name + ' ')
        self.driver.find_element_by_xpath_send_keys(xpath2, Keys.ENTER)
        sleep(5)


    @allure.step("Close all redundant tabs")
    def close_all_tabs(self):
        xpath_first_tab_close_button = '/html/body/div[4]/div[1]/section/div[1]/div/div[1]/div[2]/div/div/ul[2]/li[' \
                                       '2]/div[2]/button'
        list_xpath = '/html/body/div[4]/div[1]/section/div[1]/div/div[1]/div[2]/div/div/ul[2]/li'

        length = len(self.driver.find_elements_by_xpath(list_xpath))
        for i in range(length - 1):
            self.driver.find_element_by_xpath_click(xpath_first_tab_close_button)
            sleep(1)

    @allure.step("Toggle omni-channel")
    def toggle_omni_channel(self):
        xpath1 = r'/html/body/div[4]/div[1]/section/div[2]/div[1]/div[5]/ul/li[2]/div/div/button'
        self.driver.find_element_by_xpath_click(xpath1)
        sleep(5)

    @allure.step("Online omni-channel")
    def online_omni_channel(self):
        base_link = '/html/body/div[4]/div[1]/section/div[2]/div[1]/div[4]/div/div/div[2]/div[1]/'
        xpath1 = base_link + 'div/button'
        self.driver.find_element_by_xpath_click(xpath1)
        sleep(2)
        xpath2 = base_link + 'div/div/ul/li[1]/a'
        self.driver.find_element_by_xpath_click(xpath2)
        sleep(5)
        xpath3 = base_link + 'span'
        self.driver.assert_element(xpath3, "Online")
        sleep(1)

    @allure.step("Accept Omni-Channel case")
    def accept_omni_channel_case(self):
        # Waiting client
        base_link = '/html/body/div[4]/div[1]/section'

        xpath_button = base_link + '/div[2]/div[1]/div[4]/div/div/div[2]/div[2]/div/section[1]/div/ul/li/div/div[' \
                                   '2]/button'
        self.driver.find_element_by_xpath_click(xpath_button)
        sleep(5)

        xpath_case_status = base_link + '/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[' \
                                        '2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg' \
                                        '-rollup_component___force-generated__flexipage_-record-page___' \
                                        '-communication_-case_record_page___-case___-v-i-e-w/forcegenerated' \
                                        '-flexipage_communication_case_record_page_case__view_js/record_flexipage' \
                                        '-desktop-record-page-decorator/div[' \
                                        '1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three' \
                                        '-col-template-desktop2/div/div/flexipage-record-home-scrollable-column/slot' \
                                        '/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/article/div/div[' \
                                        '2]/div/div/div[2]/div/section/div[1]/div/div/div/div/div[2]/div[1]/div'
        self.driver.assert_element(xpath_case_status, "New")
        sleep(5)

        self.driver.find_element_by_xpath_click(
            base_link + '/div[1]/div/div[1]/div[2]/div/div/ul[2]/li[2]/a')

    @allure.step("Enter free text in textarea")
    def send_free_text(self, msg):
        base_link = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[' \
                    '2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force' \
                    '-generated__flexipage_-record-page___-communication_-case_record_page___-case___-v-i-e-w' \
                    '/forcegenerated-flexipage_communication_case_record_page_case__view_js/record_flexipage-desktop' \
                    '-record-page-decorator/div[' \
                    '1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three-col-template' \
                    '-desktop2/div/div/div/flexipage-record-home-scrollable-column[' \
                    '1]/slot/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/article/fieldset/'
        xpath_textarea = base_link + 'div[8]/div[1]/div[4]/span/div/span/div/div[1]/lightning-textarea/div/textarea'
        self.driver.find_element_by_xpath_send_keys(xpath_textarea, msg)
        sleep(5)
        xpath_send_button = base_link + 'div[8]/div[1]/div[4]/span/div/span/div/div[2]/div[2]/div/div[8]/button'
        self.driver.find_element_by_xpath_click(xpath_send_button)
        sleep(5)
        xpath_text_msg = base_link + 'div[3]/section/div/div/ul[last()]/li/div/div/div[1]/div/div[2]/div/span'
        self.driver.assert_element(xpath_text_msg, msg)

    @allure.step("Send example template without fields in textarea")
    def send_template(self, template):
        base_link = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[' \
                    '2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force' \
                    '-generated__flexipage_-record-page___-communication_-case_record_page___-case___-v-i-e-w' \
                    '/forcegenerated-flexipage_communication_case_record_page_case__view_js/record_flexipage-desktop' \
                    '-record-page-decorator/div[' \
                    '1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three-col-template' \
                    '-desktop2/div/div/div/flexipage-record-home-scrollable-column[' \
                    '1]/slot/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/article/fieldset/'
        msg = r'🔆您好，csl 現為特選客戶提供轉台優惠'
        xpath_select_template_button = base_link + 'div[8]/div[1]/div[3]/span/div/div[2]/div/div[1]/span/select'
        self.driver.find_element_by_xpath_set_option(xpath_select_template_button, template)
        sleep(5)
        xpath_send_button = base_link + 'div[8]/div[1]/div[4]/span/div/span/div/div[2]/div[2]/div/div[8]/button'
        self.driver.find_element_by_xpath_click(xpath_send_button)
        sleep(5)
        xpath_text_msg = base_link + 'div[3]/section/div/div/ul[50]/li/div/div/div[1]/div/div[2]/div/span'
        self.driver.assert_element(xpath_text_msg, msg)

    @allure.step("Send example template without fields in textarea")
    def send_template_with_fields(self):
        base_link = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[' \
                    '2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force' \
                    '-generated__flexipage_-record-page___-communication_-case_record_page___-case___-v-i-e-w' \
                    '/forcegenerated-flexipage_communication_case_record_page_case__view_js/record_flexipage-desktop' \
                    '-record-page-decorator/div[' \
                    '1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three-col-template' \
                    '-desktop2/div/div/div/flexipage-record-home-scrollable-column[' \
                    '1]/slot/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/article/fieldset/'
        xpath_select_template_button = base_link + 'div[8]/div[1]/div[3]/span/div/div[2]/div/div[1]/span/select'
        xpath_textarea = base_link + "div[8]/div[1]/div[4]/span/div/span/div/div[1]/lightning-textarea/div/textarea"
        xpath_send_button = base_link + 'div[8]/div[1]/div[4]/span/div/span/div/div[2]/div[2]/div/div[8]/button'
        xpath_text_msg = base_link + 'div[3]/section/div/div/ul[50]/li/div/div/div[1]/div/div[2]/div/span'

        template_msg = 'Please feel free to contact Daniel at 12345678'
        template = 'Template : btu_user_contact_test(WhatsApp Approved)'

        self.driver.find_element_by_xpath_set_option(xpath_select_template_button, template)
        sleep(5)

        for i in range(29):
            self.driver.find_element_by_xpath_send_keys_without_clearing(xpath_textarea, Keys.BACKSPACE)
        self.driver.find_element_by_xpath_send_keys_without_clearing(xpath_textarea, "Daniel at 12345678")
        self.driver.find_element_by_xpath_click(xpath_send_button)
        self.airtest_driver.implicitly_wait(10)
        self.driver.assert_element(xpath_text_msg, template_msg)
        sleep(1)

    @allure.step("Close case")
    def close_case(self):
        base_link = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[' \
                    '2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg-rollup_component___force' \
                    '-generated__flexipage_-record-page___-communication_-case_record_page___-case___-v-i-e-w' \
                    '/forcegenerated-flexipage_communication_case_record_page_case__view_js/record_flexipage-desktop' \
                    '-record-page-decorator/div[' \
                    '1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three-col-template' \
                    '-desktop2/div/div/div/flexipage-record-home-scrollable-column[2]/slot/slot/flexipage-component2[' \
                    '1]/slot/flexipage-tabset2/div/lightning-tabset/div/slot/slot/flexipage-tab2[' \
                    '1]/slot/flexipage-component2/slot/flexipage-aura-wrapper/div/div/'
        xpath_select_case_close = base_link + 'div[1]/div[1]/div/select'
        self.driver.find_element_by_xpath_set_option(xpath_select_case_close, 'Test')
        sleep(5)
        xpath_save_case_close = base_link + 'div[2]/button'
        self.driver.find_element_by_xpath_click(xpath_save_case_close)
        sleep(5)
        xpath_case_status = r'/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[' \
                            r'2]/section/div/div/section/div/div[' \
                            r'2]/div/div/div/div/one-record-home-flexipage2/forcegenerated-adg' \
                            r'-rollup_component___force-generated__flexipage_-record-page___-communication_' \
                            r'-case_record_page___-case___-v-i-e-w/forcegenerated' \
                            r'-flexipage_communication_case_record_page_case__view_js/record_flexipage-desktop-record' \
                            r'-page-decorator/div[' \
                            r'1]/records-record-layout-event-broker/slot/slot/flexipage-record-home-three-col' \
                            r'-template-desktop2/div/div/flexipage-record-home-scrollable-column/slot/slot/flexipage' \
                            r'-component2/slot/flexipage-aura-wrapper/div/article/div/div[2]/div/div/div[' \
                            r'2]/div/section/div[1]/div/div/div/div/div[2]/div[1]/div/div[2]/span/span'
        self.driver.assert_element(xpath_case_status, "Closed")
        print("close case")

    @allure.step("Click on 'New' status + session < 24 hrs cases")
    def click_on_latest_new_available_cases(self):
        base_link = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/'
        # sort status in descending order (New):
        status_button_xpath = base_link + 'thead/tr/th[5]/div/a'
        status_xpath = base_link + 'thead/tr/th[5]/div/span'
        status = self.driver.find_element_by_xpath(status_xpath)
        print("-------status--------")
        print(status.text)
        sleep(1)
        while status.text != 'Sorted Descending':
            self.driver.find_element_by_xpath_click(status_button_xpath)
            status = self.driver.find_element_by_xpath(status_xpath)
            sleep(5)

        latest_case_status_xpath = base_link + 'tbody/tr[1]/td[4]/span/span'
        latest_case_xpath = base_link + 'tbody/tr[1]/th/span/a'
        print("====latest_case====")
        print(self.driver.find_element_by_xpath(latest_case_status_xpath).text)
        if self.driver.find_element_by_xpath(latest_case_status_xpath).text == "New":
            self.driver.find_element_by_xpath_click(latest_case_xpath)
        print('end latest case')
