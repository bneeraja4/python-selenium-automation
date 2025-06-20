from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

SIDE_NAV_ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='content-wrapper'] [id*='addToCart']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "[data-test='content-wrapper'] h4")
ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[id*='addToCartButton']")
OPEN_CART_CHECKOUT_BTN = (By.XPATH,"//*[text()='View cart & check out']")
VERIFY_CORRECT_PRODUCT = (By.CSS_SELECTOR,"[data-test*='cartItem']")
SEARCH_FIELD = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
SEARCH_RESULT_TEXT = (By.XPATH, "//div[@data-test='lp-resultsCount']")

@when('Search for {search_word}')
def search_product(context, search_word):
    context.driver.find_element(*SEARCH_FIELD).send_keys(search_word)
    context.driver.find_element(*SEARCH_BTN).click()

@then('Verify search worked for {product}')
def verify_search_results(context, product):
    actual_text = context.driver.find_element(*SEARCH_RESULT_TEXT).text
    assert product in actual_text, f"Error, expected {product} not in actual {actual_text}"

@when('Click on Add to Cart button')
def click_add_to_cart(context):
    context.driver.find_element(*ADD_TO_CART_BTN).click()  # always clicks on 1st Add to cart context
    sleep(10)

@when('Store product name')
def store_product_name(context):
    context.product_name = context.driver.find_element(*SIDE_NAV_PRODUCT_NAME).text
    print('Product name stored: ', context.product_name)

@when('Confirm Add to Cart button from side navigation')
def side_nav_click_add_to_cart(context):
    context.driver.wait.until(Ec.element_to_be_clickable(SIDE_NAV_ADD_TO_CART_BTN)).click()
    #context.driver.find_element(*SIDE_NAV_ADD_TO_CART_BTN).click()
    sleep(10)

@when('open the cart and checkout')
def open_cart(context):
    context.driver.find_element(*OPEN_CART_CHECKOUT_BTN).click()
    sleep(5)

@then('Verify cart has correct product')
def verify_cart(context):
    actual_text = context.driver.find_element(*VERIFY_CORRECT_PRODUCT).text
    assert  actual_text is not None
    print("testcase passed")
    sleep(10)