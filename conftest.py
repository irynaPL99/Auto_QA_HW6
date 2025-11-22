# HW6 conftest.py
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_step_one_page import CheckoutPage
from pages.checkout_step_two_page import CheckoutOverviewPage

@pytest.fixture(scope="function")   # новый чистый браузер для каждого теста
def driver():
    chrome_options = Options()

    # ──────── ЭТОТ БЛОК УБИВАЕТ ВСЕ ПОПАПЫ С ПАРОЛЯМИ, Chrom 140+ ────────
    prefs = {
        "credentials_enable_service": False,  # отключить службу паролей
        "profile.password_manager_enabled": False,  # отключить менеджер паролей
        "profile.password_manager_leak_detection": False,
        "autofill.profile_enabled": False,  # отключить автозаполнение профиля
        "autofill.credit_card_enabled": False,  # отключить автозаполнение карт
    }
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_argument("--disable-infobars")
    chrome_options.add_argument("--disable-notifications")
    # ─────────────────────────────────────────────────────────────

    # driver = webdriver.Chrome()
    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()

    # Привязываем страницы к драйверу
    driver.login_page = LoginPage(driver)
    driver.inventory_page = InventoryPage(driver)
    driver.cart_page = CartPage(driver)
    driver.checkout_step_one_page = CheckoutPage(driver)
    driver.checkout_step_two_page = CheckoutOverviewPage(driver)

    yield driver
    driver.quit()