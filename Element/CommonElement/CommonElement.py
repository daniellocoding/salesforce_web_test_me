# -*- encoding=utf8 -*-
__author__ = "Issac"

from airtest.core.api import *
# from airtest.cli.parser import cli_setup
from os.path import abspath, dirname
import sys
from Element.ClientToServer.ClientToServer import Element as ClientToServer


from selenium.common.exceptions import NoSuchElementException
# import datetime

from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support import expected_conditions as EC

from Common.Tool import web_tool
import allure

project_path = dirname(dirname(dirname(abspath(__file__))))
sys.path.append(project_path)


class CommonElement:
    def __init__(self, driver):
        self.airtest_driver = driver
        self.driver = web_tool(driver)
        self.client_to_server = ClientToServer(driver)

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
        xpath2 = r'/html/body/div[4]/div[2]/div[4]/div[1]/div[2]/one-app-launcher-menu/div/one-app-launcher-search-bar/lightning-input/div/div/input'
        xpath3 = r'/html/body/div[4]/div[2]/div/div[1]/div[2]/one-app-launcher-menu/div/one-app-launcher-search-bar/lightning-input/div/div/input'
        try:
            self.driver.find_element_by_xpath_send_keys(xpath2, service_name + ' ')
            self.driver.find_element_by_xpath_send_keys(xpath2, Keys.ENTER)
        except NoSuchElementException:
            self.driver.find_element_by_xpath_send_keys(xpath3, service_name + ' ')
            self.driver.find_element_by_xpath_send_keys(xpath3, Keys.ENTER)
        sleep(5)

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

    @allure.story('Test accept case')
    def test_accept_case(self):
        self.client_to_server.click_app_launcher("Service Console")
        self.client_to_server.close_all_tabs()
        self.client_to_server.toggle_omni_channel()
        self.client_to_server.online_omni_channel()

        self.client_to_server.accept_omni_channel_case()
        self.client_to_server.toggle_omni_channel()

