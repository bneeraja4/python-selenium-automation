from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&')
#create your amazon account button
driver.find_element(By.CSS_SELECTOR, "#createAccountSubmit").click()
#driver.get("https://www.amazon.com/ap/register?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_ya_signin&prevRID=8PJEV8Q5SS0P85DA4077&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0")
sleep(6)
#amazon logo
driver.find_element(By.CSS_SELECTOR,'i[class="a-icon a-icon-logo"]')
#create account
driver.find_element(By.CSS_SELECTOR,'h1.a-spacing-small')
#your name field
driver.find_element(By.ID,"ap_customer_name")
#mobile number or email field
driver.find_element(By.ID,"ap_email")
#password field
driver.find_element(By.ID,"ap_password")
#re-enter password field
driver.find_element(By.ID,'ap_password_check')
#continue button
driver.find_element(By.ID,"continue")
#conditions of use link
driver.find_element(By.CSS_SELECTOR,"[href*='ap_register_notification_condition_of_use']")
#privacy notice link
driver.find_element(By.CSS_SELECTOR,"[href*='ap_register_notification_privacy_notice']")
#sign-in
driver.find_element(By.CSS_SELECTOR,"a[class='a-link-emphasis']").click()




