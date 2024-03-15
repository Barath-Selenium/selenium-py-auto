import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

TIMEOUT = 60  # Example: 60 seconds

service_obj = Service(r"C:\Users\ELCOT\Downloads\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

name = "Krishna"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.ID, "name").send_keys(name)
driver.find_element(By.ID, "alertbtn").click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()
time.sleep(5)



