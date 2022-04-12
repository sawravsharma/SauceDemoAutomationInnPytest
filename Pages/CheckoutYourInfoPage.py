import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

from Locators.Locators import Locators
from Pages.BasePage import BasePage
from Config.config import TestData
from Pages.CheckoutOverviewPage import CheckoutOverviewPage

class CheckoutYourInfoPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def get_checkout_your_info_page_header(self):
        return self.get_element_text(Locators.CHECKOUT_YOUR_INFO_PAGE_HEADER)

    '''Fetching the data from config file'''
    def do_enter_your_info(self):
        self.do_send_keys(Locators.FIRST_NAME, TestData.FIRST_NAME)
        self.do_send_keys(Locators.LAST_NAME, TestData.LAST_NAME)
        self.do_send_keys(Locators.ZIP_POSTAL_CODE, TestData.POSTAL_CODE)

    def do_click_on_continue_button(self):
        self.do_click(Locators.CONTINUE_BUTTON)
        return CheckoutOverviewPage(self.driver)


        