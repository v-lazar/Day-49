import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import dotenv




dotenv.load_dotenv(dotenv_path="C:/Users/vlazar/OneDrive/v$cfg/smtepy/.env")

JOB_AREA = "Oxfordshire, England, United Kingdom"
JOB_TITLE = "Junior Network Engineer"
ACCOUNT_EMAIL = os.environ.get("LINKEDIN_TEST_ACCOUNT_USERNAME")
ACCOUNT_PASSWORD =  os.environ.get("LINKEDIN_TEST_ACCOUNT_PASSWORD")

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/")

# Click 'Reject Cookies' Button
time.sleep(6)
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()

# Sign in
time.sleep(2)
sign_in_button = driver.find_element(by=By.CSS_SELECTOR, value='.nav__button-secondary.btn-secondary-emphasis.btn-md')
sign_in_button.click()

## Insert credentials
time.sleep(5)
### Username
username = driver.find_element(by=By.NAME, value='session_key')
username.send_keys(ACCOUNT_EMAIL)
### Password
password = driver.find_element(by=By.NAME, value='session_password')
password.send_keys(ACCOUNT_PASSWORD)
### Press 'Enter' to sign in
password.send_keys(Keys.ENTER)

time.sleep(4)
show_more = driver.find_element(by=By.XPATH,
                                value='/html/body/div[6]/div[3]/div/div[3]'
                                      '/div/div/main/div/div/div[1]/div[1]'
                                      '/div/div/div/section/div[2]/a')
show_more.click()

time.sleep(3)
job_title_input_box = driver.find_element(By.XPATH, value='//*[@id="jobs-search-box-keyword-id-ember517"]')
job_title_input_box.send_keys(JOB_TITLE)

time.sleep(3)
location_input_box = driver.find_element(By.XPATH, value='//*[@id="jobs-search-box-location-id-ember517"]')
location_input_box.send_keys(JOB_AREA)
location_input_box.send_keys(Keys.ENTER)