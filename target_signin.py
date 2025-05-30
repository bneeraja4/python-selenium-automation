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
driver.get('https://www.target.com/')
#sleep(5)
#Click Account button
driver.find_element(By.XPATH,"//*[text()='Account']").click()
sleep(5)
#click signin button from side navigation
driver.find_element(By.XPATH,"//button[text()='Sign in or create account']").click()
sleep(5)
#Assert(verification)
expected_text = 'Sign in or create account'
actual_text = driver.find_element(By.XPATH,"//h1[text()='Sign in or create account']").text
assert expected_text in actual_text, f'Error, expected{expected_text} not in actual {actual_text}'
print("Testcase passed")
driver.quit()
