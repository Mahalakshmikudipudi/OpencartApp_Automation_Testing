from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service("C:/drivers/chromedriver-win32/chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.shopify.com/in")


wait = WebDriverWait(driver, 10)

wait.until(EC.presence_of_element_located((By.XPATH, "//span[normalize-space()='Log in']"))).click()

driver.find_element(By.XPATH, "//span[normalize-space()='Log in']").click()

time.sleep(15)