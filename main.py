import os, time, dotenv
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

dotenv.load_dotenv(dotenv_path="C:/Users/vlazar/OneDrive/v$cfg/smtepy/.env")

# JOB_AREA = "Oxfordshire, England, United Kingdom"
# JOB_TITLE = "Junior Network Engineer"
ACCOUNT_EMAIL = os.environ.get("LINKEDIN_TEST_ACCOUNT_USERNAME")
ACCOUNT_PASSWORD =  os.environ.get("LINKEDIN_TEST_ACCOUNT_PASSWORD")

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/")

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

time.sleep(3)
# Switch and navigate to new url which has parameters for location and Job Title search
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4088290002&geoId=107161656&"
           "keywords=Junior%20Network%20Engineer&origin=JOB_COLLECTION_PAGE_SEARCH_BUTTON&refresh=true")


time.sleep(4)
job_cards = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for card in job_cards:
    try:
        card.click()
        time.sleep(4)
        save_button = driver.find_element(by=By.CSS_SELECTOR,
                                          value='.jobs-save-button')
        save_button.click()
        time.sleep(3)

    except Exception as e:
        print("Error processing job:", e)


