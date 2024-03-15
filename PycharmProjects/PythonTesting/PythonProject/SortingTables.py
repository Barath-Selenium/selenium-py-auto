import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headlesss")

TIMEOUT = 60  # Example: 60 seconds

service_obj = Service(r"C:\Users\ELCOT\Downloads\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
browserStoredVeggie = []

driver.find_element(By.XPATH, "//span[text()='Veg/fruit name']").click()
veggieWebElements = driver.find_elements(By.XPATH, "//tr/td[1]")
for ele in veggieWebElements:
    browserStoredVeggie.append(ele.text)

originalBrowserSortedList = browserStoredVeggie.copy()
browserStoredVeggie.sort()

assert browserStoredVeggie == originalBrowserSortedList




