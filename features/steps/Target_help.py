from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given( 'Open Target Help page' )
def open_target(context):
    context.driver.get('https://help.target.com/help')

@then( 'Verify Target Help header' )
def verify_help_header(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class='sc-606bee4-0 eZfijo']")
    sleep(5)

@then( 'Verify search help input field' )
def verify_search_help_input(context):
    context.driver.find_element(By.ID, 'search')
    sleep(5)

@then( 'Verify search button' )
def verify_search_button(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    sleep(5)

@then( 'Verify What would you like to do section' )
def verify_what_to_do_section(context):
    context.driver.find_element(By.CSS_SELECTOR, "[class='sc-c55f45dd-0 bsAQNK']")

@then( 'Verify Browse all help pages text is displayed' )
def verify_browse_all_help_pages(context):
    context.driver.find_element(By.XPATH, "//button[text()='Browse all help']")
