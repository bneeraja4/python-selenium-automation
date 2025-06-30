from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):

    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    def verify_cart_empty(self):
        actual_text = self.driver.find_element(*self.CART_EMPTY_MSG).text
        expected_text = 'Your cart is empty'
        assert actual_text == expected_text, f"Error, expected {expected_text} but got actual {actual_text}"
