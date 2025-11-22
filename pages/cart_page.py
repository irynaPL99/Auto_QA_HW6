from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:
    CHECKOUT_BUTTON = (By.ID, "checkout")
    COUNT_ITEMS = (By.CLASS_NAME, "shopping_cart_badge")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


    def click_checkout(self):
        self.driver.find_element(*self.CHECKOUT_BUTTON).click()

    def check_count_items(self):
        return self.driver.find_element(*self.COUNT_ITEMS).text