import sys, os
import time
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import pytest
import allure 
from Pages.AddToCartPage import AddToCartPage
from Pages.CheckoutYourInfoPage import CheckoutYourInfoPage
from allure_commons.types import AttachmentType
from Tests.test_Base import BaseTest
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Config.config import TestData
from Locators.Locators import Locators

class Test_CheckoutYourInfoPage(BaseTest):

    @pytest.mark.order(16)
    def test_verify_CheckoutYourInfo_page_header(self):
        loginPage = LoginPage(self.driver)
        homePage = loginPage.do_login()
        homePage = HomePage(self.driver)
        homePage.do_shopping()
        addToCart = AddToCartPage(self.driver)
        addToCart.do_click_checkout_button()
        checkInfo = CheckoutYourInfoPage(self.driver)
        title = checkInfo.get_element_text(Locators.CHECKOUT_YOUR_INFO_PAGE_HEADER)
        assert title == TestData.CHECKOUT_YOUR_INFO_HEADER
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.JPG)  

    @pytest.mark.order(17)
    def test_verify_enter_info_in_form(self):
        loginPage = LoginPage(self.driver)
        homePage = loginPage.do_login()
        homePage = HomePage(self.driver)
        homePage.do_shopping()
        addToCart = AddToCartPage(self.driver)
        addToCart.do_click_checkout_button()
        checkInfo = CheckoutYourInfoPage(self.driver)
        checkInfo.do_enter_your_info()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.JPG)      

    @pytest.mark.order(18)
    def test_verify_continue_button(self):
        loginPage = LoginPage(self.driver)
        homePage = loginPage.do_login()
        homePage = HomePage(self.driver)
        homePage.do_shopping()
        addToCart = AddToCartPage(self.driver)
        addToCart.do_click_checkout_button()
        checkInfo = CheckoutYourInfoPage(self.driver)
        checkInfo.do_enter_your_info()
        checkInfo.do_click_on_continue_button()
        allure.attach(self.driver.get_screenshot_as_png(),attachment_type=AttachmentType.JPG)  
