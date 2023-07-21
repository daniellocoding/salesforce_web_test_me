# -*- encoding=utf8 -*-
__author__ = "Issac"
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from os.path import abspath, dirname
import sys

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Common.Tool import web_tool
import allure

project_path = dirname(dirname(dirname(abspath(__file__))))
sys.path.append(project_path)


class WhatsappElement:
    def __init__(self, driver):
        self.airtest_driver = driver
        self.driver = web_tool(driver)


    @allure.step("Scan QR Code, And Then Enter")
    def scan_qr_code(self):
        print("Scan QR Code, And then Enter after loaded into whatsapp")
        input()
        # sleep(30) # load in messages
        print("Logged In")
        sleep(3)

    @allure.step("Search for contact")
    def search_for_contact(self, contact="+852 5410 5130", alt_contact="csl UATB Testing 2"):
        # find contact by number
        inp_xpath_search = '/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/button'
        inp_xpath_search_content = '/html/body/div[1]/div/div/div[4]/div/div[1]/div/div/div[2]/div/div'
        input_box_search = self.driver.find_element_by_xpath(inp_xpath_search)
        input_box_search.click()
        time.sleep(2)
        input_box_search_content = self.driver.find_element_by_xpath(inp_xpath_search_content)
        input_box_search_content.send_keys(contact)
        try:
            selected_contact = self.driver.find_element_by_xpath("//span[@title='" + contact + "']")
            selected_contact.click()
        except NoSuchElementException:
            selected_contact = self.driver.find_element_by_xpath("//span[@title='" + alt_contact + "']")
            selected_contact.click()
        time.sleep(2)

    @allure.step("Send text thru chat box")
    def client_whatsapp_reply_send_text(self, message="Hey, this message was sent using Selenium"):
        inp_xpath = '/html/body/div[1]/div/div/div[5]/div/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[1]'
        input_box = self.driver.find_element_by_xpath(inp_xpath)
        time.sleep(2)

        input_box.send_keys(message + Keys.ENTER)
        time.sleep(5)

    @allure.step("Client Whatsapp Reply Thru button")
    def client_whatsapp_reply_button(self):
        ask_for_other_price_button_xpath = '/html/body/div[1]/div/div/div[5]/div/div[2]/div/div[2]/div[3]/div[last()]/div/div/div/div[3]/div/button[2]'
        self.driver.find_element_by_xpath_click(ask_for_other_price_button_xpath)
        sleep(3)

    @allure.step("Open new Tab")
    def open_new_tab(self):
        # Open New Tab
        window_1_id = self.driver.get_current_window_handle()
        self.driver.execute_script("window.open('about:blank','secondtab');")
        self.driver.switch_window("secondtab")
        window_2_id = self.driver.get_current_window_handle()
        # new tab id
        return [window_1_id, window_2_id]

    @allure.step("Switch Tab")
    def switch_tab(self, tab_to_be_switched_id):
        self.driver.switch_window(tab_to_be_switched_id)
