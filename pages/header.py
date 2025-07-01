from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    ACCOUNT_BTN = (By.XPATH, "//span[text()='Account']")
    SIGNIN_BTN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")

    def search_product(self,search_word):
        self.input_text(search_word, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(10)

    def click_account(self):
        self.click(*self.ACCOUNT_BTN)

    def verify_navigation_menu(self):
        self.click(*self.SIGNIN_BTN)

    def click_cart(self):
        self.click(*self.CART_ICON)