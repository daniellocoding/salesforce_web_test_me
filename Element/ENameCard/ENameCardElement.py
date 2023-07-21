# -*- encoding=utf8 -*-
__author__ = "Issac"
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from os.path import abspath, dirname
import sys

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from pynput.mouse import Button
from pynput.keyboard import Key
from pynput import mouse, keyboard


from Common.Tool import web_tool
import allure

project_path = dirname(dirname(dirname(abspath(__file__))))
sys.path.append(project_path)


class ENameCardElement:
    def __init__(self, driver):
        self.airtest_driver = driver
        self.driver = web_tool(driver)

    @allure.step("Decode QR")
    def decode_qr(self):
        return self.driver.decode()

    @allure.step("Get to a website")
    def get(self, url):
        self.airtest_driver.get(url)

    @allure.step("Click Popup Enter Whatsapp")
    def click_popup(self, x, y):
        m = mouse.Controller()
        m.position = (x, y)
        m.click(Button.left)

    @allure.step("Send the preset message")
    def send_preset_message(self, x, y):
        m = mouse.Controller()
        m.position = (x, y)
        m.click(Button.left)

        k = keyboard.Controller()
        k.press(Key.enter)
        k.release(Key.enter)

    @allure.step("Click switch to the other website")
    def click_switch_to_utac(self):
        m = mouse.Controller()
        m.position = (304, 413)
        m.click(Button.left)

    @allure.step("Assert Element")
    def assert_element(self, xpath, msg=None):
        self.driver.assert_element(xpath, msg)


    @allure.step("Change to other list - Benny's Cases")
    def change_list(self, list):
        xpath_list_button = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[1]/div[1]/div[1]/div/div/div/div[1]/div/div/div[2]/div/button'
        xpath_search = '/html/body/div[4]/div[2]/div[2]/div/div[1]/div/div/input'
        xpath_bennys_case = '/html/body/div[4]/div[2]/div[2]/div/div[1]/div/div/div/div/div[1]/div/ul/li/a'

        self.driver.find_element_by_xpath_click(xpath_list_button)
        self.driver.find_element_by_xpath_send_keys(xpath_search, list)
        self.driver.find_element_by_xpath_click(xpath_bennys_case)
        sleep(5)

    @allure.step("Status descending")
    def status_descending(self, owner_name):
        xpath_status_button = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/thead/tr/th[6]/div/a'
        xpath_status = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/thead/tr/th[6]/div/span'

        status = self.driver.find_element_by_xpath(xpath_status)
        while status.text != "Sorted Descending":
            print("Start clicking on status")
            self.driver.find_element_by_xpath_click(xpath_status_button)
            status = self.driver.find_element_by_xpath(xpath_status)
            print("Clicked on status")
            sleep(3)
        sleep(3)

        latest_case_status_xpath = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/tbody/tr[1]/td[5]/span/span'
        latest_case_owner_name_xpath = '/html/body/div[4]/div[1]/section/div[1]/div/div[2]/div[1]/div/div/div/div/div/div/div/div[2]/div/div[1]/div[2]/div[2]/div[1]/div/div/table/thead/tr/th[13]/div/a/span[2]'
        print("Asserting Status")
        self.driver.assert_element(latest_case_status_xpath, "New")
        self.driver.assert_element(latest_case_owner_name_xpath, owner_name)
        print("Success Asserting")









