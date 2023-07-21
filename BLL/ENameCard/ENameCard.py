from threading import Timer

import allure
from Common.Tool import web_tool
from Element.ClientToServer.ClientToServer import Element as ClientToElement
from Element.LoginPage.LoginPage import Element as LoginPageElement
from Element.ENameCard.ENameCardElement import ENameCardElement
from Element.Whatsapp.Whatsapp import WhatsappElement

from time import sleep
from pynput.mouse import Button
from pynput.keyboard import Key
from pynput import mouse, keyboard

import logging
from Element.CommonElement.CommonElement import CommonElement


class ENameCard:
    def __init__(self, driver):
        self.driver = driver
        self.ename_element = ENameCardElement(driver)
        self.whatsapp_element = WhatsappElement(driver)
        self.login_page_element = LoginPageElement(driver)
        self.common_element = CommonElement(driver)

    @allure.story("ENameCard Test")
    def test(self, username, password, list, owner_name, click_popup_x=908, click_popup_y=221, send_preset_msg_x=1103, send_preset_msg_y=800):
        decode_url = self.ename_element.decode_qr()
        self.ename_element.get(decode_url)
        self.ename_element.click_popup(click_popup_x, click_popup_y)
        sleep(2)
        self.ename_element.send_preset_message(send_preset_msg_x, send_preset_msg_y)
        sleep(2)

        # web uatc assert element is existed?
        self.ename_element.click_switch_to_utac()
        self.ename_element.get("https://here2serve--uatc.sandbox.my.salesforce.com/?login")
        self.login_page_element.username_input(username)
        self.login_page_element.password_input(password)
        self.login_page_element.login_button_click()
        self.login_page_element.check_login_status()

        # close all tabs
        self.common_element.click_app_launcher("Service Console")
        self.common_element.close_all_tabs()
        self.common_element.click_app_launcher("Cases")

        # click
        self.ename_element.change_list(list)

        # status descending
        self.ename_element.status_descending(owner_name=owner_name)





        # def on_click(x, y, button, pressed):
        #     # print("{0} at {1}".format("Pressed" if pressed else 'Released', (x, y)))
        #
        #     if pressed:
        #         # logging.info('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        #         print('Mouse clicked at ({0}, {1}) with {2}'.format(x, y, button))
        #
        # def on_scroll(x, y, dx, dy):
        #     # logging.info('Mouse scrolled at ({0}, {1})({2}, {3})'.format(x, y, dx, dy))
        #     print("Scrolled {0} at {1}".format('down' if dy < 0 else 'up', (x, y)))
        #
        # with mouse.Listener(on_click=on_click) as listener:
        #     Timer(5, listener.stop).start()
        #     listener.join()
        #     print("5 seconds passed")



