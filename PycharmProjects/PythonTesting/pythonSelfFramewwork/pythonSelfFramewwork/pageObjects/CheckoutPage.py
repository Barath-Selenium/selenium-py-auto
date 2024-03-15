from selenium.webdriver.common.by import By


class CheckOutPage:

    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    cardFooter = (By.CSS_SELECTOR, ".btn.btn-info")
    checkOut = (By.XPATH, "//a[@class='nav-link btn btn-primary']")
    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)


    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)


    def checkOutItems(self):
        return self.driver.find_element(*CheckOutPage.checkOut)





