from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):

    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")
    def open_cart(self):
        self.driver.find_element(By.XPATH,"//a[text()='View cart & check out']").click()

    def verify_cart_empty(self):
        actual_text = self.driver.find_element(*self.CART_EMPTY_MSG).text
        expected_text = 'Your cart is empty'
        assert actual_text == expected_text, f"Error, expected {expected_text} but got actual {actual_text}"

    def verify_cart_items(context, amount):
        cart_summary = context.driver.find_element(By.XPATH, "//div[./span[contains(text(), 'subtotal')]]").text
        assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"

    def verify_item_added(self):
        items = self.driver.find_element(By.CSS_SELECTOR,"[data-test='cartItem']").text
        assert len(items) > 0, "No items found in the cart"