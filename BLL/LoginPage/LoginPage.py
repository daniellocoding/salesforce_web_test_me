import allure
from Common.Tool import web_tool
from Element.LoginPage.LoginPage import Element
from time import sleep


class LoginPage:
    def __init__(self, driver):
        self.element = Element(driver)

    @allure.story('Login user')
    def login(self, username, password):
        self.element.username_input(username)
        self.element.password_input(password)
        self.element.login_button_click()
        self.element.check_login_status()
