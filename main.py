from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver = webdriver.Chrome();
driver.get('https://www.livechat.com/typing-speed-test/#/')
#tst-input-wrapper
elem = driver.find_element(By.ID,'test-input')
for x in range(1,320):
    word = driver.find_element(By.XPATH, '//span[@class="u-pl-0 u-pr-2xs"]')

    elem.send_keys(word.text+' ')
time.sleep(5)
