# -*- encoding=utf8 -*-
__author__ = "Issac"

from os.path import abspath, dirname

from airtest_selenium.proxy import WebChrome
from selenium import webdriver

import pyautogui
import pytest
import sys

project_path = dirname(dirname(abspath(__file__)))
sys.path.append(project_path)

chromedriver_path = r'../chromedriver/chromedriver.exe'


@pytest.fixture(scope='module', autouse=False)
def before():
    # custom_tool().connect_driver()
    option = webdriver.ChromeOptions()
    option.add_argument('--window-size=1080,800')
    # 模拟按下 Win + D 快捷键
    # pyautogui.hotkey('win', 'd')
    driver = WebChrome(executable_path=chromedriver_path, options=option)
    driver.implicitly_wait(30)
    driver.maximize_window()
    print("打开浏览器".encode('utf-8'))
    yield driver
    print("关闭浏览器".encode('utf-8'))
    driver.quit()
    # pyautogui.hotkey('alt', 'tab')
