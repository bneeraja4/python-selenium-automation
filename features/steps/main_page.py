from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open target main page')
def open_main(context):
    # context.driver.get('https://www.target.com/')
    context.app.main_page.open_main_page()

# @when('Click on Cart icon')
# def click_cart(context):
#     context.driver.find_element(By.CSS_SELECTOR,"[data-test='@web/CartIcon']").click()

@when('Click Account')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR,'[class="sc-43f80224-3 fBDEOp h-margin-r-x3"]').click()