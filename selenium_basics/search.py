# 1:
"""
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("http://www.ebay.com")
print(driver.current_url)
driver.quit()
"""

# 2:
"""
from selenium import webdriver
driver = webdriver.Chrome()
driver.get('https://www.ebay.com')
import time
time.sleep(10)
driver.quit()
"""

#3
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver_path = '/opt/homebrew/bin/chromedriver'  

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.get("http://www.ebay.com")

search_field = driver.find_element(By.ID, 'gh-ac')
search_field.send_keys("women watch")

search_button = driver.find_element(By.ID, 'gh-btn')
search_button.click()

driver.quit()
"""

#3:
"""
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chromedriver_path = '/opt/homebrew/bin/chromedriver'  

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service)

driver.get("http://www.ebay.com")

wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.ID, 'gh-ac')))  

search_field = driver.find_element(By.ID, 'gh-ac')
search_field.send_keys("women watch")

search_button = driver.find_element(By.ID, 'gh-btn')  
search_button.click()

wait.until(EC.presence_of_element_located((By.XPATH, '//h1[contains(text(), "results for women watch")]')))

header_text = driver.find_element(By.XPATH, '//h1[contains(text(), "results for women watch")]').text
assert "results for women watch" in header_text.lower()

driver.quit()
"""