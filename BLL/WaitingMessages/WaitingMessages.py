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
    def test_bot_expiry_queue_wait_case_wait(self, contact, alt_contact, username, password):
        bot_info = self.wm.get_bot_info(contact, alt_contact, username, password)
        e1 = self.wm.test_bot_expiry(contact, alt_contact, username, password)
        e2 = self.wm.test_queue_waiting(contact, alt_contact, username, password)
        e3 = self.wm.test_case_waiting(contact, alt_contact, username, password)
        print(bot_info,'\n',e1,'\n',{'Queue_waiting_Reply': e2.split('\n')[0]},'\n',{'Case_waiting_Reply': e3.split('\n')[0]})











