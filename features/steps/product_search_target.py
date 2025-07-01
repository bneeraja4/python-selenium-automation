from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import given, when, then
from time import sleep

SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
OPEN_CART_CHECKOUT_BTN = (By.XPATH,"//*[text()='View cart & check out']")
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
SEARCH_RESULT_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")

# @when('Search for {search_word}')
# def search_product(context, search_word):
#     context.app.header.search_product(search_word)
    #context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    #context.driver.find_element(*SEARCH_BTN).click()


@then('Verify search worked for {product}')
def verify_search_results(context,product):
    context.app.search_results_page.verify_search_results(product)
    #actual_text = context.driver.find_element(*SEARCH_RESULT_TEXT).text
    #assert product in actual_text, f"Error, expected {product} not in actual {actual_text}"

@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.app.product_page.click_add_to_cart()
    # context.driver.find_element(*ADD_TO_CART_BTN).click()  # always clicks on 1st Add to cart context
    # context.driver.wait.until(EC.visibility_of_element_located(SIDE_NAV_PRODUCT_NAME),message='Product name was not visible')

@when('Store product name')
def store_product_name(context):
    context.app.product_page.store_product_name()
    #context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    #print('Product name stored: ', context.product_name)


@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.app.product_page.side_nav_click_add_to_cart()
    #context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    sleep(10)

@when('open the cart and checkout')
def open_cart(context):
    context.driver.find_element(*OPEN_CART_CHECKOUT_BTN).click()
    sleep(5)