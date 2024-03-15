import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

TIMEOUT = 60  # Example: 60 seconds

service_obj = Service(r"C:\Users\ELCOT\Downloads\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()

# types of locaters - ID, Xpath, CSSSelector, Classname, name, linktext.

# driver.set_page_load_timeout(TIMEOUT)
driver.find_element(By.NAME, "email").send_keys("barath@gmail.com")
driver.find_element(By.ID, "exampleInputPassword1").send_keys("Password")
driver.find_element(By.ID, "exampleCheck1").click()

#Static dropdown
dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
dropdown.select_by_index(0)
dropdown.select_by_visible_text("Female")
# dropdown.select_by_value()   --- Doubt.
# Syntax for XPath - //tagname[@attribute='value']  //input[@type='submit']
# Syntax for CSSSelector - tagname[attribute='value']  //input[@type='submit'],  #ID, .Classname - its is also cssselector.
driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("Barath")
driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
driver.find_element(By.XPATH, "//input[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, "alert-success").text
print(message)
assert "Success" in message
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").send_keys("Barath againnn")
driver.find_element(By.XPATH, "(//input[@type='text'])[3]").clear()
time.sleep(4)


