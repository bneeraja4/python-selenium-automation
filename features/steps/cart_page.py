from selenium.webdriver.common.by import By
from behave import given, when, then

@when('Open cart page')
def open_cart(context):
    context.app.cart_page.open_cart()

@then('Verify cart has correct product')
def verify_product_name(context):
    # context.product_name => stored before
    product_name_in_cart = context.driver.find_element(By.CSS_SELECTOR, "[data-test='cartItem-title']").text
    print('Name in cart: ', product_name_in_cart)

    assert context.product_name[:20] == product_name_in_cart[:20], \
        f'Expected {context.product_name[:20]} did not match {product_name_in_cart[:20]}'

@then('Verify cart has {amount} item(s)')
def verify_cart_items(context, amount):
    cart_summary = context.driver.find_element(By.XPATH, "//div[./span[contains(text(), 'subtotal')]]").text
    assert f'{amount} item' in cart_summary, f"Expected {amount} items but got {cart_summary}"

@then("Verify 'Your cart is empty' message is shown")
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty()


@then('Verify Cart page opened')
def verify_cart_opened(context):
    context.app.cart_page.verify_cart_opened()

@then('Verify cart should contain at least one item')
def verify_cart_items(context):
    context.app.cart_page.verify_item_added()
