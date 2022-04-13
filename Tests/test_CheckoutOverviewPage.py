import sys, os

myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
import allure 
import time
from Pages.AddToCartPage import AddToCartPage
from Pages.CheckoutOverviewPage import CheckoutOverviewPage
from Pages.CheckoutYourInfoPage import CheckoutYourInfoPage
from allure_commons.types import AttachmentType
from Tests.test_Base import BaseTest
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Locators.Locators import Locators
from Config.config import TestData


class Test_CheckoutOverviewPage(BaseTest):

    '''To check if added items are getting displayed in OverView page also'''
    @pytest.mark.webtest
    @pytest.mark.order(19)
    def test_verify_added_items_getting_displayed(self):
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
        checkoutOverview.is_items_getting_displayed_in_cart()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.JPG)
        checkoutOverview.do_click_on_finish_button()

    '''To assert the h1 tag of OverView page'''
    @pytest.mark.order(20)
    def test_verify_checkout_overview_page_header(self):
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
        checkout_overview_page_header = checkoutOverview.checkout_overview_page_header()
        assert checkout_overview_page_header == TestData.CHECKOUT_OVERVIEW_HEADER
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.PNG) 

