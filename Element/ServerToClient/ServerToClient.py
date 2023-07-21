# -*- encoding=utf8 -*-
__author__ = "Issac"

import selenium.common.exceptions
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from os.path import abspath, dirname
import sys

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

from Common.Tool import web_tool
import allure
import datetime

project_path = dirname(dirname(dirname(abspath(__file__))))
sys.path.append(project_path)


class Element:
    def __init__(self, driver):
        self.airtest_driver = driver
        self.driver = web_tool(driver)

    @allure.step("Switch iframe")
    def switch_iframe(self):
        # WebDriverWait(self.driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.XPATH,"//iframe[@title='accessibility title']")))

        xpath_iframe = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/force-aloha-page/div/iframe'
        iframe_element = self.driver.find_element_by_xpath(xpath_iframe)
        self.driver.switch_frame(iframe_element)

    @allure.step("Return to the original iframe")
    def return_original_iframe(self):
        self.airtest_driver.switch_to.default_content()

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

    @allure.step("Click app launcher and go there")
    def click_app_launcher(self, service_name="Service Console"):
        self.airtest_driver.implicitly_wait(5)
        xpath1 = r'/html/body/div[4]/div[1]/section/div[1]/div/div[1]/div[1]/div/div[1]/div[1]/button'
        xpath2 = r'/html/body/div[4]/div[1]/section/div[1]/div[1]/one-appnav/div/div/div/div/one-app-launcher-header/button'
        try:
            self.driver.find_element_by_xpath_click(xpath1)  # service console / sales console
            self.switch_service_in_launcher_v2(service_name)
        except NoSuchElementException:
            self.driver.find_element_by_xpath_click(xpath2)  # service / bolt solutions / others (?)
            self.switch_service_in_launcher_v2(service_name)
        self.airtest_driver.implicitly_wait(15)

    @allure.step("Switch service(when clicked by xpath2)")
    def switch_service_in_launcher_v2(self, service_name="Service Console"):
        xpath2 = '/html/body/div[4]/div[2]/div[4]/div[1]/div[2]/one-app-launcher-menu/div/one-app-launcher-search-bar/lightning-input/div/div/input'
        xpath3 = '/html/body/div[4]/div[2]/div/div[1]/div[2]/one-app-launcher-menu/div/one-app-launcher-search-bar/lightning-input/div/div/input'
        try:
            self.driver.find_element_by_xpath_send_keys(xpath2, service_name + ' ')
            self.driver.find_element_by_xpath_send_keys(xpath2, Keys.ENTER)
        except NoSuchElementException:
            self.driver.find_element_by_xpath_send_keys(xpath3, service_name + ' ')
            self.driver.find_element_by_xpath_send_keys(xpath3, Keys.ENTER)
        sleep(5)

    @allure.step("Switch service(when clicked by xpath1)")
    def switch_service_in_launcher_v1(self, service_name="Service Console"):
        xpath1 = r'/html/body/div[4]/div[2]/div[2]/div[1]/div[2]/one-app-launcher-menu/div/one-app-launcher-search-bar/lightning-input/div/div/input'
        self.driver.find_element_by_xpath_send_keys(xpath1, service_name + ' ')
        self.driver.find_element_by_xpath_send_keys(xpath1, Keys.ENTER)
        sleep(5)
        if service_name.lower() != "cases":
            xpath2 = r'/html/body/div[4]/div[1]/section/div[1]/div/div[1]/div[1]/div/div[1]/div[2]/span'
            self.driver.assert_element(xpath2, service_name)

    @allure.step("Choose Sender ID")
    def choose_sender_id(self, sender_id):
        xpath1 = '/html/body/form/div[2]/span/span[2]/fieldset/div[2]/div/select'
        sender_id = 'csl UATB Testing 2 (54105130)'
        self.driver.find_element_by_xpath_set_option(xpath1, sender_id)

    @allure.step("Add Phone Numbers")
    def add_phone_number(self, phone_number_strings):
        xpath1 = '/html/body/form/div[2]/span/span[2]/fieldset/div[4]/div/textarea'
        self.driver.find_element_by_xpath_send_keys(xpath1, phone_number_strings)

    @allure.step("Choose Template Access Level")
    def choose_template_access_level(self, template_access_level):
        xpath1 = '/html/body/form/div[2]/span/span[2]/fieldset/div[6]/div/select'
        self.driver.find_element_by_xpath_set_option(xpath1, template_access_level)

    @allure.step("Choose Template")
    def choose_template(self, template_name):
        xpath1 = '/html/body/form/div[2]/span/span[2]/fieldset/div[7]/div/select'
        self.driver.find_element_by_xpath_set_option(xpath1, template_name)

    @allure.step("Send")
    def click_send_button(self):
        xpath1 = '/html/body/form/div[2]/span/span[2]/fieldset/input'
        xpath1 = '/html/body/form/div[2]/span/span[2]/fieldset/div[11]/div[1]/span/input'
        self.driver.find_element_by_xpath_click(xpath1)

    @allure.step("Close all redundant tabs in UAT")
    def close_all_tabs(self):
        xpath_first_tab_close_button = '/html/body/div[4]/div[1]/section/div[1]/div/div[1]/div[2]/div/div/ul[2]/li[' \
                                       '2]/div[2]/button'
        xpath2 = '/html/body/div[4]/div[1]/section/div[1]/div/div[1]/div[2]/div/div/ul[2]/li[2]/div[2]/button'
        list_xpath = '/html/body/div[4]/div[1]/section/div[1]/div/div[1]/div[2]/div/div/ul[2]/li'

        length = len(self.driver.find_elements_by_xpath(list_xpath))
        for i in range(length - 1):
            self.driver.find_element_by_xpath_click(xpath_first_tab_close_button)
            sleep(1)

    @allure.step("Click next")
    def click_next(self):
        try:
            self.click_next_v1()
        except NoSuchElementException:
            self.click_next_v2()

    @allure.step("Bulk Messages from csv - Click next v1")
    def click_next_v1(self):
        xpath1 = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/div[3]/div[4]/div[2]/div/div/button[2]'
        self.driver.find_element_by_xpath_click(xpath1)
        sleep(3)

    def click_next_v2(self):
        xpath2 = '/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div[3]/div/div/div[3]/div[4]/div[2]/div/div/button[2]'
        self.driver.find_element_by_xpath_click(xpath2)


    @allure.step("Bulk Messages from csv - Upload file")
    def upload_bulk_csv(self, file_url):
        xpath3 = '/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div[2]/div/div/div[3]/div[1]/div/input'
        xpath1 = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/div[3]/div[1]/div/input'
        try:
            self.driver.find_element_by_xpath_upload_file(xpath1, file_url)
        except NoSuchElementException:
            self.driver.find_element_by_xpath_upload_file(xpath3, file_url)


    @allure.step("Bulk Messages from csv - Enter Messaging in preview")
    def enter_messages_in_preview(self, msg='Testing messaging sent thru bulk message from csv'):
        xpath1 = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/div[3]/div[2]/div[1]/div[2]/fieldset/div[1]/div[1]/span/lightning-textarea/div/textarea'
        self.driver.find_element_by_xpath_send_keys(xpath1, msg)

    @allure.step("Checking which version could run")
    def run_choose_templates_version(self):
        try:
            print("Running Choose Template v1")
            self.choose_templates_in_preview_v1()
        except NoSuchElementException:
            print("Running Choose Template v2")
            self.choose_templates_in_preview_v2()

    @allure.step("Bulk Message from csv - Choose v1")
    def choose_templates_in_preview_v1(self):
        # choose select sender id
        xpath_sender_id = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section[1]/div/div/section/div/div[2]/div/div/div/div/div[3]/div[2]/div[1]/div[1]/fieldset/div[2]/select'
        xpath_sender_id_v2 =    '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section[2]/div/div/section/div/div[2]/div/div/div/div/div[3]/div[2]/div[1]/div[1]/fieldset/div[2]/select'
        self.driver.find_element_by_xpath_set_option(xpath_sender_id, "csl UATB Testing 2 (54105130)")
        # choose template access
        xpath_template_access = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section[1]/div/div/section/div/div[2]/div/div/div/div/div[3]/div[2]/div[1]/div[1]/fieldset/div[3]/select'
        xpath_template_access_v2 = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section[2]/div/div/section/div/div[2]/div/div/div/div/div[3]/div[2]/div[1]/div[1]/fieldset/div[3]/select'

        self.driver.find_element_by_xpath_set_option(xpath_template_access, "Mobile BU")
        # choose templates
        xpath_templates = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section[1]/div/div/section/div/div[2]/div/div/div/div/div[3]/div[2]/div[1]/div[1]/fieldset/div[4]/select'
        xpath_templates_v2 = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section[2]/div/div/section/div/div[2]/div/div/div/div/div[3]/div[2]/div[1]/div[1]/fieldset/div[4]/select'
        self.driver.find_element_by_xpath_set_option(xpath_templates, "i_mob_bb_button1_bulk_zh")
        # click preview
        xpath_preview = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/div[3]/div[2]/div[1]/div[2]/fieldset/div[1]/div[2]/span/button'
        self.driver.find_element_by_xpath_click(xpath_preview)

    @allure.step("Bulk Message from csv - Choose Templates v2")
    def choose_templates_in_preview_v2(self):
        # choose select sender id

        xpath_sender_id = '/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div[3]/div/div/div[3]/div[2]/div[1]/div[1]/fieldset/div[2]/select'
        self.driver.find_element_by_xpath_set_option(xpath_sender_id, "csl UATB Testing 2 (54105130)")
        # choose template access
        xpath_template_access = '/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div[3]/div/div/div[3]/div[2]/div[1]/div[1]/fieldset/div[3]'
        self.driver.find_element_by_xpath_set_option(xpath_template_access, "Mobile BU")
        # choose templates
        xpath_templates = '/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div[3]/div/div/div[3]/div[2]/div[1]/div[1]/fieldset/div[4]'
        self.driver.find_element_by_xpath_set_option(xpath_templates, "i_mob_bb_button1_bulk_zh")
        # click preview
        xpath_preview = '/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div[3]/div/div/div[3]/div[2]/div[1]/div[2]/fieldset/div[1]/div[2]/span/button'
        self.driver.find_element_by_xpath_click(xpath_preview)

    @allure.step("scroll down to bottom page")
    def scroll_to_bottom(self):
        # wait = WebDriverWait(self.driver, 10)
        self.driver.execute_script("scroll(0, 800);")
        sleep(1)

    def click_send_now_button(self):
        try:
            self.click_send_now_button_v1()
        except NoSuchElementException:
            self.click_send_now_button_v2()

    @allure.step("Bulk Messages from csv - Send Now v1")
    def click_send_now_button_v1(self):
        xpath1 = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/div[3]/div[3]/div/center/button'
        self.driver.find_element_by_xpath_click(xpath1)

    @allure.step("Bulk Messages from csv - Send Now v2")
    def click_send_now_button_v2(self):
        xpath2 = '/html/body/div[4]/div[1]/section/div[1]/div[2]/div[2]/div[1]/div/div/div/div[3]/div/div/div[3]/div[3]/div/center/button'
        self.driver.find_element_by_xpath_click(xpath2)

    # input: max_time_processing (minutes)
    @allure.step("Bulk Messages from csv - Click Finish after 100% completed")
    def click_finish_button_after_finishing(self, max_time_processing=5):
        xpath1 = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/div[3]/div[3]/div/h1'
        sleep(1)
        t = 0
        while True:
            updated_finished_percentage = self.driver.get_element_text_content_by_xpath(xpath1)
            if updated_finished_percentage == '100% Completed':
                xpath2 = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/div[3]/div[4]/div[2]/div/div/button[2]'
                self.driver.find_element_by_xpath_click(xpath2)
                break
            if t == int(max_time_processing) * 60:
                exit(-1)
                break
        sleep(3)

        # self.click_next()

    @allure.step("Check in message bucket if the messages have been sent (checking time in minutes) - assume sent 1 message")
    def check_delivered(self, sender_id, receiver_phone_number=None ):
        self.close_all_tabs()
        self.click_app_launcher("Service Console")
        self.click_app_launcher("Message Bucket")
        self.hide_app_launcher()
        sleep(5)
        # select a filterable bucket list (Benny Message is one)
        xpath_show_list_3 = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div/div[1]/h1/span[2]'
        xpath_show_list_search = '/html/body/div[4]/div[2]/div[2]/div/div[1]/div/div/input'
        xpath_benny_message = '/html/body/div[4]/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]/div/ul/li/a'

        self.driver.find_element_by_xpath_click(xpath_show_list_3)
        self.driver.find_element_by_xpath_send_keys(xpath_show_list_search, "Benny Daniel's Case")
        self.driver.find_element_by_xpath_click(xpath_benny_message)
        sleep(5)

        # Filter for my message
        xpath_filter_show_hide_button_v2 = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section[2]/div/div/section/div/div[2]/div/div/div/div/div[1]/div[2]/div[3]/force-list-view-manager-button-bar/div/lightning-button-group/div/slot/lightning-button-icon-stateful[2]/span/button'
        xpath_add_filter_v2 = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section[2]/div/div/section/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/a[1]'
        xpath_remove_all_filter_v2 = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section[2]/div/div/section/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div/div[2]/a[2]'
        xpath_filter_show_hide_button = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/div[1]/div[2]/div[3]/force-list-view-manager-button-bar/div/lightning-button-group/div/slot/lightning-button-icon-stateful[2]/span/button'
        xpath_add_filter = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/a[1]'
        xpath_remove_all_filter = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/div[2]/div/div[2]/div/div[2]/div[1]/div[2]/a[2]'
        self.driver.find_element_by_xpath_click(xpath_filter_show_hide_button)
        self.driver.find_element_by_xpath_click(xpath_remove_all_filter)

        # enter fields that you want to filter
        xpath_filter_field_v2 = '/html/body/div[4]/div[2]/div[5]/div[1]/div[1]/div/div/div[1]/lightning-combobox/div/lightning-base-combobox/div/div[1]/button'
        xpath_filter_field_sender_id_from_v2 = '/html/body/div[4]/div[2]/div[5]/div[1]/div[1]/div/div/div[1]/lightning-combobox/div/lightning-base-combobox/div/div[2]/lightning-base-combobox-item[112]'
        xpath_filter_field_number_to_phone_v2 = '/html/body/div[4]/div[2]/div[5]/div[1]/div[1]/div/div/div[1]/lightning-combobox/div/lightning-base-combobox/div/div[2]/lightning-base-combobox-item[75]'
        xpath_value_v2 = '/html/body/div[4]/div[2]/div[5]/div[1]/div[1]/div/div/div[2]/div/div/input'

        xpath_filter_field = '/html/body/div[4]/div[2]/div[3]/div[1]/div[1]/div/div/div[1]/lightning-combobox/div/lightning-base-combobox/div/div[1]/button'
        xpath_filter_field_v3 = '/html/body/div[4]/div[2]/div[2]/div[1]/div[1]/div/div/div[1]/lightning-combobox/div/lightning-base-combobox/div/div[1]/button'
        xpath_filter_field_sender_id_from = '/html/body/div[4]/div[2]/div[3]/div[1]/div[1]/div/div/div[1]/lightning-combobox/div/lightning-base-combobox/div/div[2]/lightning-base-combobox-item[112]'
        xpath_filter_field_number_to_phone = '/html/body/div[4]/div[2]/div[3]/div[1]/div[1]/div/div/div[1]/lightning-combobox/div/lightning-base-combobox/div/div[2]/lightning-base-combobox-item[75]'
        xpath_value = '/html/body/div[4]/div[2]/div[3]/div[1]/div[1]/div/div/div[2]/div/div/input'
        xpath_done_button = '/html/body/div[4]/div[2]/div[3]/div[1]/div[1]/div/button'
        # 1st filter (sended id)
        self.driver.find_element_by_xpath_click(xpath_add_filter)
        self.driver.find_element_by_xpath_click(xpath_filter_field)
        self.driver.find_element_by_xpath_click(xpath_filter_field_sender_id_from)
        self.driver.find_element_by_xpath_send_keys(xpath_value, sender_id)
        self.driver.find_element_by_xpath_click(xpath_done_button)
        # 2nd filter (number to phone)
        if receiver_phone_number is not None:
            self.driver.find_element_by_xpath_click(xpath_add_filter)
            self.driver.find_element_by_xpath_click(xpath_filter_field)
            self.driver.find_element_by_xpath_click(xpath_filter_field_number_to_phone)
            self.driver.find_element_by_xpath_send_keys(xpath_value, receiver_phone_number)
            self.driver.find_element_by_xpath_click(xpath_done_button)

        # close filter menu, wait check time * 60, and refresh
        self.driver.find_element_by_xpath_click(xpath_filter_show_hide_button)

        # calculate how much time we need to wait

        current_time = datetime.datetime.now()
        minute = current_time.minute
        remainder = minute % 10
        waiting_times = [6, 5, 4, 3, 12, 11, 10, 9, 8, 7]
        waiting_time = waiting_times[remainder]
        print("start waiting")
        sleep(waiting_time*60)
        print("Finish waiting")

        # proceed process
        xpath_table_refresh_button_v2 = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section[2]/div/div/section/div/div[2]/div/div/div/div/div[1]/div[2]/div[3]/force-list-view-manager-button-bar/div/div[1]/lightning-button-icon/button'
        xpath_table_refresh_button = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/div[1]/div[2]/div[3]/force-list-view-manager-button-bar/div/div[1]/lightning-button-icon/button'
        self.driver.find_element_by_xpath_click(xpath_table_refresh_button)
        sleep(1)
        print("Clicked refresh")


        # sort status in Descending submitted time
        submitted_on_button_xpath_v2 = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section[2]/div/div/section/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/thead/tr/th[9]/div/a'
        submitted_on_xpath_v2 = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section[2]/div/div/section/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/thead/tr/th[9]/div/span'
        submitted_on_button_xpath = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/thead/tr/th[9]/div/a'
        submitted_on_xpath = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/thead/tr/th[9]/div/span'
        submitted_on = self.driver.find_element_by_xpath(submitted_on_xpath)
        while submitted_on.text != "Sorted Descending":
            print("Start clicking on submit")
            self.driver.find_element_by_xpath_click(submitted_on_button_xpath)
            submitted_on = self.driver.find_element_by_xpath(submitted_on_xpath)
            print("Clicked on submit")
            sleep(3)

        sleep(3)
        latest_case_status_xpath_v2 = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section[2]/div/div/section/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/td[7]/span/span[1]'
        latest_case_status_xpath = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[2]/section/div/div/section/div/div[2]/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/td[7]/span/span[1]'
        print("Asserting Status")
        self.driver.assert_element(latest_case_status_xpath, "Delivered")
        print("Success Asserting")

