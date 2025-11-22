from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutOverviewPage:
    TOTAL_PRICE = (By.CSS_SELECTOR, ".summary_total_label")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def get_total_price_text(self):
        #return self.driver.find_element(*self.TOTAL_PRICE).text
        total_element = self.wait.until(
            EC.presence_of_element_located(
                self.TOTAL_PRICE
            )
        )
        return total_element.text
