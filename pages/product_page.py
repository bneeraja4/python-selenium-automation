from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class ProductPage(Page):
    ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
    SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
    SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")

    def click_add_to_cart(self):
       self.driver.find_element(*self.ADD_TO_CART_BTN).click()
       sleep(2)

    def side_nav_click_add_to_cart(self):
       self.driver.find_element(*self.SIDE_NAV_ADD_TO_CART_BTN).click()
       sleep(10)

    def store_product_name(self):
        self.driver.find_element(*self.SIDE_NAV_PRODUCT_NAME)

