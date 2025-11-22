# HW6: import in conftest.py
#from time import sleep


# Откройте сайт магазина: https://www.saucedemo.com/.
# Авторизуйтесь как пользователь standard_user.
def test_checkout_total_price(driver):
   driver.login_page.open()
   driver.login_page.enter_username("standard_user")
   driver.login_page.enter_password("secret_sauce")
   driver.login_page.click_on_login_button()

   assert "inventory.html" in driver.current_url, "Не удалось войти в систему."

# Добавьте в корзину товары:
   driver.inventory_page.click_add_backpack() # Sauce Labs Backpack
   driver.inventory_page.click_add_tshirt()   # Sauce Labs Bolt T-Shirt
   driver.inventory_page.click_add_onesie()   # Sauce Labs Onesie

   # Перейдите в корзину.
   driver.inventory_page.click_go_to_cart()

   # Нажмите Checkout.
   # print("Товаров в корзине:", driver.cart_page.check_count_items())
   driver.cart_page.click_checkout()

   # Заполните форму своими данными:
   # Имя, Фамилия, Почтовый индекс
   driver.checkout_step_one_page.enter_first_name("Ivan")
   driver.checkout_step_one_page.enter_last_name("Ivanov")
   driver.checkout_step_one_page.enter_post_code("1234")
   driver.checkout_step_one_page.click_continue()

   # Прочтите со страницы итоговую стоимость (Total).
   total_price_text = driver.checkout_step_two_page.get_total_price_text()
   #sleep(2)

   # Проверьте, что итоговая сумма равна $58.29
   assert "$58.29" in  total_price_text, "Prices do not match!"