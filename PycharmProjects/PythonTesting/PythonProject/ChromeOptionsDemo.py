import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")
chrome_options.add_argument("headless")
chrome_options.add_argument("--ignore-certificate-errors")

TIMEOUT = 60  # Example: 60 seconds

service_obj = Service(r"C:\Users\ELCOT\Downloads\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj,options=chrome_options)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
print(driver.title)


