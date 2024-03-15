import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

TIMEOUT = 60  # Example: 60 seconds

service_obj = Service(r"C:\Users\ELCOT\Downloads\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, ".blinkingText").click()
windowsOpened = driver.window_handles

driver.switch_to.window(windowsOpened[1])
message = driver.find_element(By.CSS_SELECTOR, ".red").text
var = message.split("at")[1].strip().split(" ")[0]
driver.close()
driver.switch_to.window(windowsOpened[0])
driver.find_element(By.ID, "username").send_keys(var)
driver.find_element(By.ID, "password").send_keys(var)
driver.find_element(By.ID, "signInBtn").click()

wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR, ".alert-danger").text)

