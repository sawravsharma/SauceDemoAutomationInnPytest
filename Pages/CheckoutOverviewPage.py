import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
from Locators.Locators import Locators
from Pages.BasePage import BasePage
from EnumsPackage.Enums import Products, Products_Z_To_A
from Pages.CheckoutCompletePage import CheckoutCompletePage


class CheckoutOverviewPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def  checkout_overview_page_header(self):
        return self.get_element_text(Locators.CHECKOUT_OVERVIEW_PAGE_HEADER)

    def is_items_getting_displayed_in_cart(self):
        for getValue in Products:
            addedItems  = self.driver.find_element_by_xpath(
                "//div[contains(text(),'%s')]" % str(getValue.value)) 
        assert addedItems.text == getValue.value

    def do_click_on_finish_button(self):
        self.do_click(Locators.FINISH_BUTTON)
        return CheckoutCompletePage(self.driver)