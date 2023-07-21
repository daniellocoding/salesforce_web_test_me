import allure
from Common.Tool import web_tool
from Element.CommonElement.CommonElement import CommonElement
from Element.Whatsapp.Whatsapp import WhatsappElement
from Element.WaitingMessages.WaitingMessages import WaitingMessagesElement
from time import sleep


class WaitingMessages:
    def __init__(self, driver):
        self.ce = CommonElement(driver)
        self.we = WhatsappElement(driver)
        self.wm = WaitingMessagesElement(driver)

    @allure.story("Test Queue, case waiting")
    def test_bot_expiry_queue_wait_case_wait(self, contact, alt_contact):
        self.we.scan_qr_code()
        self.wm.test_bot_expiry(contact, alt_contact)














