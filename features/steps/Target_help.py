from selenium.webdriver.common.by import By
from behave import given, when, then

target_header = (By.CSS_SELECTOR,"[class='custom-h2']")
search_field = (By.ID,"j_id0:j_id2:j_id44:name")
search_btn = (By.CSS_SELECTOR,"[class='btn-sm search-btn']")
Help_topic_section = (By.XPATH,"/div[@class='col-lg-12']")
contactus_section = (By.XPATH,"/div[@class='col-lg-12']")
footer_section = (By.XPATH,"//h2[text()='Browse all Help pages']")

@given( 'Open Target Help page' )
def open_target(context):
    context.driver.get('https://help.target.com/help')

@then('the UI element should be present on the page')
def verify_ui_element(context):
    context.driver.find_element(*target_header)
    context.driver.find_element(*search_field)
    context.driver.find_element(*search_btn)
    context.driver.find_elements(*Help_topic_section)
    context.driver.find_elements(*contactus_section)
    context.driver.find_element(*footer_section)


