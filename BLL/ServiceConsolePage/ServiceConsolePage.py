import allure
from Common.Tool import web_tool
from Element.Dashboard.Dashboard import Element
from time import sleep

class ServiceConsolePage:
    def __init__(self, driver):
        self.element = Element(driver)

    @allure.story("Open service console")
    def open_service_console(self):
        self.element.click_app_launcher()
        self.element.switch_service_in_launcher("Service Console")

    @allure.story("Test online omni-channel")
    def online_omni_channel(self):
        self.element.online_omni_channel()

    @allure.story("Test busy omni-channel")
    def busy_omni_channel(self):
        self.element.busy_omni_channel()

    @allure.story("Test offline omni-channel")
    def offline_omni_channel(self):
        self.element.offline_omni_channel()

    @allure.story('Test service console')
    def test(self):
        self.open_service_console()
        self.element.open_omni_channel()
        self.busy_omni_channel()
        self.offline_omni_channel()
        self.online_omni_channel()
        self.element.close_omni_channel()


