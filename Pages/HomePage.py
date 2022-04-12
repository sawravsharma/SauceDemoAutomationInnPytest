
import os,sys
myPath = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, myPath + '/../')

import time
from Locators.Locators import Locators
from Pages.BasePage import BasePage
from EnumsPackage.Enums import Products, Products_Z_To_A, Sort_Products

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    '''Title'''
    def get_home_page_title(self, title):
        return self.get_title(title)

    '''To check Cart icon'''
    def is_cart_icon_exist(self):
        return self.is_visible(Locators.CART_ICON)

    '''To get h1 tag text'''
    def get_header_value(self):
        return self.get_element_text(Locators.HEADER)

    '''Product sorting container functionality'''
    def product_sort_container(self):
        for sorting in Sort_Products:
            sorting = self.driver.find_element_by_xpath(
                "(//*[@class='product_sort_container']//option)[%s]" % str(sorting.value))
            sorting.click()

    '''To sort products in low to high range'''
    def product_sort_container_low_to_high(self):
        lowToHighSortedProducts = self.driver.find_element_by_xpath(
            "(//*[@class='product_sort_container']//option)[%s]" % str(Sort_Products.PRICE_LOW_TO_HIGH.value))
        lowToHighSortedProducts.click()
        priceList = []
        lowToHighSortedProductsPrice = self.driver.find_elements_by_class_name("inventory_item_price")
        for price in lowToHighSortedProductsPrice:
            priceList.append(price.text.replace("$",""))
            print(priceList)
        assert priceList[0]<priceList[1], "products are not sorted"

    '''To sort products in high to low range'''
    def product_sort_container_High_to_Low(self):
        highToLowSortedProducts = self.driver.find_element_by_xpath(
            "(//*[@class='product_sort_container']//option)[%s]" % str(Sort_Products.PRICE_HIGH_TO_LOW.value))
        highToLowSortedProducts.click()
        priceListHighToLow = []
        highToLowSortedProductsPrice = self.driver.find_elements_by_class_name("inventory_item_price")
        for price in highToLowSortedProductsPrice:
            priceListHighToLow.append(price.text.replace("$",""))
            print(priceListHighToLow)
            # priceListHighToLow.append(float(price.text.replace("$","")))
        # total = 0
        # for ele in range(0,len(priceListHighToLow)):
        #     total = total + priceListHighToLow[ele]
        #     print(total)
        assert priceListHighToLow[0]>priceListHighToLow[1], "products are not sorted"
    
    '''To sort products in Z to A name range'''
    def sort_products_by_Z_To_A(self):
        sortProductsByZtoAFormat = self.driver.find_element_by_xpath(
            "(//*[@class='product_sort_container']//option)[%s]" % str(Sort_Products.NAME_Z_A.value))
        sortProductsByZtoAFormat.click()
        ProductsByZToAFormatList = []
        for zToAFormat in Products_Z_To_A:
            gettingProductsInZtoAformat  = self.driver.find_element_by_xpath(
                     "//*[contains(text(),'%s')]" % str(zToAFormat.value)) 
            ProductsByZToAFormatList.append(gettingProductsInZtoAformat.text)
            print(ProductsByZToAFormatList)
            assert gettingProductsInZtoAformat.text == zToAFormat.value 

    '''To sort products in Z to A name range'''
    def sort_products_by_A_To_Z(self):
        sortProductsByAtoZFormat = self.driver.find_element_by_xpath(
            "(//*[@class='product_sort_container']//option)[%s]" % str(Sort_Products.NAME_A_TO_Z.value))
        sortProductsByAtoZFormat.click()
        ProductsByAToZFormatList = []
        for getValue in Products:
            gettingProductsInAtoZformat  = self.driver.find_element_by_xpath(
                     "//*[contains(text(),'%s')]" % str(getValue.value)) 
            ProductsByAToZFormatList.append(gettingProductsInAtoZformat.text)
            print(ProductsByAToZFormatList)
            assert gettingProductsInAtoZformat.text == getValue.value 
        
    ''' Add to Cart functionality'''
    def do_shopping(self):
        for product in Products:
            product = self.driver.find_element_by_xpath(
                "//div[contains(text(),'%s')]/following::button" % str(product.value))
            product.click()
        self.do_click(Locators.CART_ICON)

    '''Logout'''
    def do_logout(self):
        self.do_click(Locators.BURGER_MENU_BUTTON)
        self.do_click(Locators.LOGOUT_BUTTON)
