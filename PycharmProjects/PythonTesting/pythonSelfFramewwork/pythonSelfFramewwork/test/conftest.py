import time
import pytest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def setup(request):
    browser_name = request.config.getoption("--browser_name")
    if browser_name == "chrome":
        service_obj = Service(r"C:\Users\ELCOT\Downloads\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        TIMEOUT = 60  # Example: 60 seconds
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
        driver.implicitly_wait(5)
    elif browser_name == "firefox":
        service_obj = Service(r"C:\Users\ELCOT\Downloads\chromedriver-win64\chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        TIMEOUT = 60  # Example: 60 seconds
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
        driver.implicitly_wait(5)
    elif browser_name == "edge":
        service_obj = Service(r"C:\Users\ELCOT\Downloads\edgedriver_win64\msedgedriver.exe")
        driver = webdriver.Edge(service=service_obj)
        TIMEOUT = 60  # Example: 60 seconds
        driver.get("https://rahulshettyacademy.com/angularpractice/")
        driver.maximize_window()
        driver.implicitly_wait(5)




    request.cls.driver = driver
    yield
    driver.close()


