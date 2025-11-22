from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POST_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def enter_first_name(self, first_name_value: str):
        self.driver.find_element(*self.FIRST_NAME_INPUT).send_keys(first_name_value)

    def enter_last_name(self, last_name_value: str):
        self.driver.find_element(*self.LAST_NAME_INPUT).send_keys(last_name_value)

    def enter_post_code(self, post_code_value: str):
        self.driver.find_element(*self.POST_CODE_INPUT).send_keys(post_code_value)

    def click_continue(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
