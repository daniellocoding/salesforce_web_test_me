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
        input('Please check that last routing agent, dedicated agent are closed, then enter')
        bot_info = self.wm.get_bot_info(contact, alt_contact, username, password)
        bot_expiry = self.wm.test_bot_expiry(contact, alt_contact, username, password)
        queue_waiting = self.wm.test_queue_waiting(contact, alt_contact, username, password)
        case_waiting = self.wm.test_case_waiting(contact, alt_contact, username, password)
        print(bot_info,'\n' ,bot_expiry,'\n', queue_waiting,'\n', case_waiting)
        self.wm.whatsapp_logout()









