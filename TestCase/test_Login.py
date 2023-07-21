# -*- encoding=utf8 -*-
__author__ = "Issac"

import allure
import pytest
import sys
from os.path import abspath, dirname

from airtest.report.report import LogToHtml
from selenium.webdriver.common.by import By

from BLL.LoginPage.LoginPage import LoginPage
from Common.Tool import web_tool

project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path)

excel_data = web_tool().excel_data('../Data/LoginData/data.xlsx')


@allure.story('登录账号参数化测试')
class TestLogin:
    # @pytest.mark.parametrize("username, password", excel_data)
    # def test_login_parametrize(self, before, username, password):
    #     allure.dynamic.title("登录账号参数化测试_%s" % username)
    #     driver = before
    #     driver.get('https://here2serve--uatc.sandbox.my.salesforce.com/?login')
    #     LoginPage(driver).login(username, password)

    def test_login(self, before):
        allure.dynamic.title("Hello")
        driver = before
        driver.get("https://here2serve--uatc.sandbox.my.salesforce.com/?login")
        LoginPage(driver).login(username="daniel.tl.lo@pccw.com.uatc", password="123456")
        # username_input(driver)



# @allure.story("test username")
# def username_input(driver):
#     with allure.step("entering username"):
#         xpath_username = '//*[@id="username"]'
#         driver.find_element(By.XPATH, xpath_username).send_keys("daniel.tl.lo@pccw.com.uatc")
#         driver.assert_exist('/html/body/div[1]/div[1]/div/div/div[2]/div[3]/form/div[1]/label', "Username")

# if __name__ == '__main__':
#     # 运行整个test_register.py文件
#     pytest.main(["-sq", fr"{project_path}\\TestCase\\test_Login.py", "--alluredir=.\\report", "--clean-alluredir","--reruns", "1", "--reruns-delay", "5"])
#     h1 = LogToHtml(script_root=f'{project_path}\\TestCase\\test_Login.py',script_name='test_login',log_root=f'{project_path}\\log',export_dir=f'{project_path}\\AirtestReport',logfile=f'{project_path}\\log\\log.txt',lang='zh',plugins=["airtest_selenium.report"])
#     h1.report()
