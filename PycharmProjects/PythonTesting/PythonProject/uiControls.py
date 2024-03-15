import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

TIMEOUT = 60  # Example: 60 seconds

service_obj = Service(r"C:\Users\ELCOT\Downloads\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
values = driver.find_elements(By.XPATH, "//input[@type='radio']")

print(len(values))

for value in values:
    if value.get_attribute("value") == "radio2":
        value.click()
        assert value.is_selected()
        break
time.sleep(5)

assert driver.find_element(By.ID, "displayed-text").is_displayed()
driver.find_element(By.ID, "hide-textbox").click()
assert not driver.find_element(By.ID, "displayed-text").is_displayed()









