from selenium.webdriver.common.by import By
from behave import given, when, then

@given('open the target circle page')
def open_circle(context):
    context.driver.get('https://www.target.com/circle')

@when('the benefit cells to load')
def benefit_cell(context):
    context.benefits = context.driver.find_elements(By.CSS_SELECTOR, "[class*='sc-']")

@then('should see 10 benefits')
def should_see(context):
    benefit_count = len(context.benefits)
    assert benefit_count >= 10, f"Expected at least 10 benefits, found {benefit_count}"
