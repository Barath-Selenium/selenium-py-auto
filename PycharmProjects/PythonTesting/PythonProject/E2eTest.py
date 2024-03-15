import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

TIMEOUT = 60  # Example: 60 seconds

service_obj = Service(r"C:\Users\ELCOT\Downloads\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)

#   a[href*='/angularpractice/shop'] -- css, //a[contains(@href,'shop')] -- xpath.
driver.find_element(By.XPATH, "//a[contains(@href,'shop')]").click()
products = driver.find_elements(By.XPATH, "//div[@class='card h-100']")

for product in products:
    productName = product.find_element(By.XPATH, "div/h4/a").text
    if productName == "Blackberry":
        product.find_element(By.CSS_SELECTOR, ".btn.btn-info").click()

driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
time.sleep(5)
driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
driver.find_element(By.ID, "country").send_keys("ind")
wait = WebDriverWait(driver,  10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
driver.find_element(By.LINK_TEXT, "India").click()
driver.find_element(By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()
