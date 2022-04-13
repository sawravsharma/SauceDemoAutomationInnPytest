import sys, os
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
import allure 
import time
from Pages.AddToCartPage import AddToCartPage
from Pages.CheckoutOverviewPage import CheckoutOverviewPage
from Pages.CheckoutYourInfoPage import CheckoutYourInfoPage
from Pages.CheckoutCompletePage import CheckoutCompletePage
from allure_commons.types import AttachmentType
from Tests.test_Base import BaseTest
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Locators.Locators import Locators
from Config.config import TestData
from Pages.CheckoutCompletePage import CheckoutCompletePage

class Test_CheckoutCompletePage(BaseTest):

    @pytest.mark.webtest
    @pytest.mark.order(21)
    def test_verify_checkout_complete_page_header(self):
        loginPage = LoginPage(self.driver)
        homePage = loginPage.do_login()
        homePage = HomePage(self.driver)
        homePage.do_shopping()
        addToCart = AddToCartPage(self.driver)
        addToCart.do_click_checkout_button()
        checkInfo = CheckoutYourInfoPage(self.driver)
        checkInfo.do_enter_your_info()  
        checkInfo.do_click_on_continue_button()
        checkoutOverview = CheckoutOverviewPage(self.driver)
        checkoutOverview.do_click_on_finish_button()
        checkoutcomplete = CheckoutCompletePage(self.driver)
        checkoutcompletepageheader = checkoutcomplete.checkout_complete_page_header()
        assert checkoutcompletepageheader == TestData.CHECKOUT_COMPLETE_PAGE_HEADER
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    @pytest.mark.order(22)
    def test_verify_checkout_complete_page_message(self):
        loginPage = LoginPage(self.driver)
        homePage = loginPage.do_login()
        homePage = HomePage(self.driver)
        homePage.do_shopping()
        addToCart = AddToCartPage(self.driver)
        addToCart.do_click_checkout_button()
        checkInfo = CheckoutYourInfoPage(self.driver)
        checkInfo.do_enter_your_info() 
        checkInfo.do_click_on_continue_button() 
        checkoutOverview = CheckoutOverviewPage(self.driver)
        checkoutOverview.do_click_on_finish_button()
        checkoutcomplete = CheckoutCompletePage(self.driver)
        checkoutcompletepageordermsg = checkoutcomplete.checkout_complete_page_order_message()
        assert checkoutcompletepageordermsg == TestData.CHECKOUT_COMPLETE_PAGE_ORDER_MESSAGE
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)

    @pytest.mark.order(23)
    def test_verify_checkout_complete_page_back_home_button(self):
        loginPage = LoginPage(self.driver)
        homePage = loginPage.do_login()
        homePage = HomePage(self.driver)
        homePage.do_shopping()
        addToCart = AddToCartPage(self.driver)
        addToCart.do_click_checkout_button()
        checkInfo = CheckoutYourInfoPage(self.driver)
        checkInfo.do_enter_your_info() 
        checkInfo.do_click_on_continue_button() 
        checkoutOverview = CheckoutOverviewPage(self.driver)
        checkoutOverview.do_click_on_finish_button()
        checkoutcomplete = CheckoutCompletePage(self.driver)
        checkoutcomplete.checkout_complete_page_order_back_home_button()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG)