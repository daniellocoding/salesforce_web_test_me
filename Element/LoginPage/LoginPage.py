# -*- encoding=utf8 -*-
__author__ = "Issac"
from airtest.core.api import *
from airtest.cli.parser import cli_setup
from os.path import abspath, dirname
import sys

from Common.Tool import web_tool
import allure

project_path = dirname(dirname(dirname(abspath(__file__))))
sys.path.append(project_path)


class Element:
    def __init__(self, driver):
        self.airtest_driver = driver
        self.driver = web_tool(driver)

    @allure.step("Input username")
    def username_input(self, username):
        xpath1 = '//*[@id="username"]'
        self.driver.find_element_by_xpath_send_keys(xpath1, username)

    @allure.step("Input password")
    def password_input(self, password):
        xpath1 = '//*[@id="password"]'
        self.driver.find_element_by_xpath_send_keys(xpath1, password)

    @allure.step("Click login button")
    def login_button_click(self):
        xpath1 = '//*[@id="Login"]'
        self.driver.find_element_by_xpath_click(xpath1)

    @allure.step("Check login status")
    def check_login_status(self):
        xpath1 = r'/html/body/div[4]/div[1]/section/header/div[1]/div/span'
        self.driver.assert_element(xpath1, "Sandbox: UATC")
