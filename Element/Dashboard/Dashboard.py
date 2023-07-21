# -*- encoding=utf8 -*-
__author__ = "Issac"
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from os.path import abspath, dirname
import sys

from selenium.webdriver.common.keys import Keys

from Common.Tool import web_tool
import allure

project_path = dirname(dirname(dirname(abspath(__file__))))
sys.path.append(project_path)


class Element:
    def __init__(self, driver):
        self.airtest_driver = driver
        self.driver = web_tool(driver)

    @allure.step("Click app launcher")
    def click_app_launcher(self):
        xpath1 = r'/html/body/div[4]/div[1]/section/div[1]/div/div[1]/div[1]/div/div[1]/div[1]/button'
        self.driver.find_element_by_xpath_click(xpath1)
        sleep(2)

    @allure.step("Switch service")
    def switch_service_in_launcher(self, service_name):
        xpath1 = r'/html/body/div[4]/div[2]/div[2]/div[1]/div[2]/one-app-launcher-menu/div/one-app-launcher-search-bar/lightning-input/div/div/input'
        self.driver.find_element_by_xpath_send_keys(xpath1, service_name + ' ')
        self.driver.find_element_by_xpath_send_keys(xpath1, Keys.ENTER)
        sleep(10)
        xpath2 = r'/html/body/div[4]/div[1]/section/div[1]/div/div[1]/div[1]/div/div[1]/div[2]/span'
        self.driver.assert_element(xpath2, service_name)

    @allure.step("Open omni-channel")
    def open_omni_channel(self):
        xpath1 = r'/html/body/div[4]/div[1]/section/div[2]/div[1]/div[5]/ul/li[2]/div/div/button'
        self.driver.find_element_by_xpath_click(xpath1)
        sleep(2)

    @allure.step("Close omni-channel")
    def close_omni_channel(self):
        xpath1 = r'/html/body/div[4]/div[1]/section/div[2]/div[1]/div[5]/ul/li[2]/div/div/button'
        self.driver.find_element_by_xpath_click(xpath1)
        sleep(2)

    @allure.step("Toggle omni-channel")
    def toggle_omni_channel(self):
        xpath1 = r'/html/body/div[4]/div[1]/section/div[2]/div[1]/div[5]/ul/li[2]/div/div/button'
        self.driver.find_element_by_xpath_click(xpath1)
        sleep(2)

    @allure.step("Online omni-channel")
    def online_omni_channel(self):
        xpath1 = r'/html/body/div[4]/div[1]/section/div[2]/div[1]/div[4]/div/div/div[2]/div[1]/div/button'
        self.driver.find_element_by_xpath_click(xpath1)
        sleep(2)
        xpath2 = r'/html/body/div[4]/div[1]/section/div[2]/div[1]/div[4]/div/div/div[2]/div[1]/div/div/ul/li[1]/a'
        self.driver.find_element_by_xpath_click(xpath2)
        sleep(2)
        xpath3 = r'/html/body/div[4]/div[1]/section/div[2]/div[1]/div[4]/div/div/div[2]/div[1]/span'
        self.driver.assert_element(xpath3, "Online")

    @allure.step("Busy omni-channel")
    def busy_omni_channel(self):
        xpath1 = r'/html/body/div[4]/div[1]/section/div[2]/div[1]/div[4]/div/div/div[2]/div[1]/div/button'
        self.driver.find_element_by_xpath_click(xpath1)
        sleep(2)
        xpath2 = r'/html/body/div[4]/div[1]/section/div[2]/div[1]/div[4]/div/div/div[2]/div[1]/div/div/ul/li[2]/a'
        self.driver.find_element_by_xpath_click(xpath2)
        sleep(2)
        xpath3 = r'/html/body/div[4]/div[1]/section/div[2]/div[1]/div[4]/div/div/div[2]/div[1]/span'
        self.driver.assert_element(xpath3, "Busy")

    @allure.step("Offline omni-channel")
    def offline_omni_channel(self):
        xpath1 = r'/html/body/div[4]/div[1]/section/div[2]/div[1]/div[4]/div/div/div[2]/div[1]/div/button'
        self.driver.find_element_by_xpath_click(xpath1)
        sleep(2)
        xpath2 = r'/html/body/div[4]/div[1]/section/div[2]/div[1]/div[4]/div/div/div[2]/div[1]/div/div/ul/li[3]/a'
        self.driver.find_element_by_xpath_click(xpath2)
        sleep(2)
        xpath3 = r'/html/body/div[4]/div[1]/section/div[2]/div[1]/div[4]/div/div/div[2]/div[1]/span'
        self.driver.assert_element(xpath3, "Offline")
