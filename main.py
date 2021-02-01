from selenium import webdriver
import os
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome('chromedriver')

# Test usage of selenium
SLEEP_TIME = 5

# Access Site
try:
    driver.get('https://www.coingecko.com/account/candy?locale=en')
    print('Successful Access Site')
    time.sleep(SLEEP_TIME)
except BaseException:
    print('Could not access https://www.coingecko.com/account/candy?locale=en')
    exit(1001)

# Login
try:
    driver.find_element_by_id("user_email").send_keys(os.environ.get("USEREMAIL"))
    driver.find_element_by_id("user_password").send_keys(os.environ.get("PASSWORD"))
    time.sleep(SLEEP_TIME)
    driver.find_element_by_xpath('//*[@id="new_user"]/input[8]').click()
    print('Successful Login')
    time.sleep(SLEEP_TIME)
except BaseException:
    print('Cannot login')
    exit(1002)

# Click Daily Reward
try:
    driver.find_element_by_css_selector("body > div.container > div.row.mt-1 > div.col-lg-8.pl-lg-5.mt-lg-5.pt-lg-1 > div:nth-child(3) > div > form > input.btn.btn-primary.col-12.collect-candy-button").click()
    time.sleep(SLEEP_TIME)
    print('Successful click Daily Reward')
except Exception as e:
    print(e)
    print('Cannot access daily reward')
    exit(1003)

# Quit
driver.quit()
exit(0)


