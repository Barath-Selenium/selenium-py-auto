import time
import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        homePage= HomePage(self.driver)
        homePage.shopItems().click()
        checkOutPage= CheckOutPage(self.driver)
        products = checkOutPage.getCardTitles()
        i = -1
        for product in products:
            i = i + 1
            productName = product.find_element(By.XPATH, "div/h4/a").text
            if productName == "Blackberry":
                checkOutPage.getCardFooter()[i].click()

        self.driver.find_element(By.XPATH, "//a[@class='nav-link btn btn-primary']").click()
        time.sleep(5)
        self.driver.find_element(By.CSS_SELECTOR, "button[class='btn btn-success']").click()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.CSS_SELECTOR, "div[class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.XPATH, "//input[@class='btn btn-success btn-lg']").click()



