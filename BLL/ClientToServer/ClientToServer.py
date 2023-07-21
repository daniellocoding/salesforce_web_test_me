import allure
from Common.Tool import web_tool
from Element.ClientToServer.ClientToServer import Element
from Element.Whatsapp.Whatsapp import WhatsappElement

from time import sleep


class ClientToServer:
    def __init__(self, driver):
        self.driver = driver
        self.element = Element(driver)
        self.whatsappElement = WhatsappElement(driver)

    @allure.story("Open service console")
    def open_service_console(self):
        self.element.click_app_launcher("Service Console")

    @allure.story('Test accept case')
    def test_accept_case(self):
        self.open_service_console()
        self.element.close_all_tabs()
        self.element.toggle_omni_channel()
        self.element.online_omni_channel()

        self.element.accept_omni_channel_case()
        self.element.toggle_omni_channel()

    @allure.story("Test send free text and template")
    def test_send_text_and_template(self, msg="Hi testing 123"):
        sleep(10)
        self.element.send_free_text(msg)
        sleep(5)
        template = 'Template : i_mob_bb_button1_zh(WhatsApp Approved)'
        self.element.send_template(template)

    @allure.story("Send templates that have to replace fields")
    def send_template_have_fields(self):
        self.element.send_template_with_fields()

    @allure.story("Close case and close all tabs")
    def close_case_and_tabs(self):
        self.element.close_case()
        sleep(1)
        self.element.close_all_tabs()

    @allure.story("Run whatsapp")
    def run_whatsapp(self, contact, alt_contact):
        self.whatsappElement.scan_qr_code()
        self.whatsappElement.search_for_contact(contact=contact, alt_contact=alt_contact)
        self.whatsappElement.client_whatsapp_reply_send_text(message="Hey, this message was sent using Selenium -- Start program")
        sleep(10)
        self.whatsappElement.client_whatsapp_reply_send_text(message="1")

    @allure.story("Run Whatsapp - Used in test cases 1, 2")
    def client_to_server_test_first_part(self, contact, alt_contact):
        self.run_whatsapp(contact=contact, alt_contact=alt_contact)
        # return [window_1_id, window_2_id]
        return self.whatsappElement.open_new_tab()

    @allure.story("Test Case 1b - ClientToServer")
    def client_to_server_test(self, windows_id: list):
        # windows_id = [Whatsapp, UAT]
        self.test_accept_case()
        self.test_send_text_and_template()

        # Switch tab (id2: UAT -> id1: Whatsapp)
        self.whatsappElement.switch_tab(windows_id[0])
        # Client whatsapp reply
        self.whatsappElement.client_whatsapp_reply_button()
        self.whatsappElement.client_whatsapp_reply_send_text("399? - Test message")
        # switch tab (id1: Whatsapp -> id2: UAT)
        self.whatsappElement.switch_tab(windows_id[1])
        # Server whatsapp Reply
        self.element.send_free_text("499!")
        sleep(2)
        self.close_case_and_tabs()
        sleep(5)

    @allure.story("Test case 2 - FreeTextMessaging")
    def free_text_messaging_test(self):

        # simulate opened case
        self.test_accept_case()
        # close all tabs
        self.element.close_all_tabs()
        # "Go back cases page and select the 'New' status page" // simulate enter new status case
        self.element.click_app_launcher("Cases")
        self.element.hide_app_launcher()
        sleep(1)
        self.element.click_on_latest_new_available_cases()
        sleep(3)

        # Test send text and template
        self.test_send_text_and_template()
        self.send_template_have_fields()

        # close cases and tabs after sending
        self.close_case_and_tabs()
        sleep(3)

