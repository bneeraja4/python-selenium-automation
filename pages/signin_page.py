from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import Page

class SigninPage(Page):
    def verify_sign_in_form(self):
        actual_text = self.driver.find_element(By.CSS_SELECTOR,
                                                  'h1[class="styles_ndsHeading__HcGpD styles_fontSize1__i0fbt styles_x2Margin__M5gHh h-text-lg h-text-center h-margin-b-tiny"]').text
        expected_text = 'Sign in or create account'
        assert actual_text == expected_text, f"Error, expected {expected_text} but got actual {actual_text}"
