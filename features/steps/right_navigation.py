from selenium.webdriver.common.by import By
from behave import given, when, then

@then("From right side navigation menu, click Sign In")
def verify_navigation_menu(context):
    #context.driver.find_element(By.CSS_SELECTOR, "[data-test='accountNav-signIn']").click()
    context.app.header.verify_navigation_menu()

@then("Verify Sign In form opened")
def verify_sign_in_form(context):
    context.app.signin_page.verify_sign_in_form()
    #actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Sign in or create account']").text
    # actual_text = context.driver.find_element(By.CSS_SELECTOR,'h1[class="styles_ndsHeading__HcGpD styles_fontSize1__i0fbt styles_x2Margin__M5gHh h-text-lg h-text-center h-margin-b-tiny"]').text
    # expected_text = 'Sign in or create account'
    # assert actual_text == expected_text, f"Error, expected {expected_text} but got actual {actual_text}"