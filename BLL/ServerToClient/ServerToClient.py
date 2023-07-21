import allure

from Common.Tool import web_tool
from Element.ServerToClient.ServerToClient import Element
from time import sleep


class ServerToClient:
    def __init__(self, driver):
        self.driver = driver
        self.element = Element(driver)

    @allure.story("Test Bulk Messaging")
    def test_bulk_messaging(self, sender_id, sender_phone_no, phone_number_strings, template_access_level='Mobile BU', template_name='i_mob_bb_button1_bulk_zh'):
        # open bulk messaging
        self.element.click_app_launcher("Service Console")
        self.element.close_all_tabs()
        self.element.click_app_launcher("Bulk Messaging")
        sleep(3)

        self.element.switch_iframe()
        print("Switched")
        assert "Bulk Messaging" in self.driver.find_element_by_xpath("/html/body/form/div[2]/span/span[2]/fieldset/legend").text
        # enter info and bulk messaging
        print("Try test sender id")
        self.element.choose_sender_id(sender_id)
        self.element.add_phone_number(phone_number_strings)
        self.element.choose_template_access_level(template_access_level)
        self.element.choose_template(template_name)
        self.element.click_send_button()
        sleep(5)
        print("Closing all tabs")
        self.element.return_original_iframe()
        self.element.close_all_tabs()
        sleep(10)
        self.element.check_delivered(sender_id=sender_phone_no, receiver_phone_number=phone_number_strings)

    @allure.story("Test Bulk Messages From Csv")
    def test_bulk_messages_from_csv(self, file_url, sender_phone_no, receiver_phone_number):
        # open bulk messages from csv
        self.element.click_app_launcher("Service Console")
        self.element.close_all_tabs()
        self.element.click_app_launcher("Bulk Messages From Csv")
        sleep(3)

        # send csv file
        self.element.upload_bulk_csv(file_url)
        self.element.click_next()
        # page 2
        self.element.run_choose_templates_version()
        self.element.scroll_to_bottom()
        self.element.click_next()
        # page 3
        self.element.click_send_now_button()
        self.element.click_finish_button_after_finishing(5)
        self.element.close_all_tabs()

        # check if delivered or not (might wait up to 12 minutes)
        self.element.check_delivered(sender_id=sender_phone_no, receiver_phone_number=receiver_phone_number)
        sleep(10)

