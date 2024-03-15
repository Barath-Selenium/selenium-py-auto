import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

TIMEOUT = 60  # Example: 60 seconds

service_obj = Service(r"C:\Users\ELCOT\Downloads\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)

action = ActionChains(driver)
# action.click_and_hold()   # like a long press in mobile.
# action.context_click()    # to right click on a element.
# action.double_click(driver.find_element())
# action.drag_and_drop()  # like a drag and drop options needs to provide path.
# action.move_to_element()  # Like hovering a cursor it don't do any actions.

action.move_to_element(driver.find_element(By.ID, "mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT, "Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT, "Reload")).click().perform()
time.sleep(5)





