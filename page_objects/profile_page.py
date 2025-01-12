from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure
from page_objects.base_page import BasePage
from locators import *


class ProfilePage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.profile_url = 'https://stellarburgers.nomoreparties.site/account/profile'
        self.order_history_url = 'https://stellarburgers.nomoreparties.site/account/order-history'
        self.personal_account_button = (By.XPATH, personal_account_button)
        self.login_url = 'https://stellarburgers.nomoreparties.site/login'
        self.exit_button = (By.XPATH, exit_button)
        self.history_orders_button = (By.XPATH, history_orders_button)
        self.order_number_in_order_history = (By.XPATH, order_number_in_order_history)
        self.feed_orders = (By.XPATH, feed_orders)

    @allure.step("Клик на кнопку 'личный кабинет'")
    def click_on_the_personal_account_button(self):
        self.click(*self.personal_account_button)

    @allure.step("Проверка, что текущий урл - https://stellarburgers.nomoreparties.site/account/profile")
    def assert_profile_url(self):
        self.wait_for_url(self.profile_url)
        self.assert_current_url(self.profile_url)

    @allure.step("Клик на историю заказов")
    def click_on_the_history_orders_button(self):
        self.click(*self.history_orders_button)

    @allure.step("Проверка на то, что текущий урл - https://stellarburgers.nomoreparties.site/account/order-history")
    def assert_order_history_url(self):
        self.wait_for_url(self.order_history_url)
        self.assert_current_url(self.order_history_url)

    @allure.step("Клик на кнопку выйти")
    def click_on_the_exit_button(self):
        self.click(*self.exit_button)

    @allure.step("Проверка на то, что текущий урл - https://stellarburgers.nomoreparties.site/login")
    def assert_login_url(self):
        self.wait_for_url(self.login_url)
        self.assert_current_url(self.login_url)

    @allure.step("Получение номера заказа")
    def get_number_from_the_order_history(self) -> int:
        return self.get_number(*self.order_number_in_order_history)

    @allure.step("Клик на ленту заказов")
    def click_on_the_feed_orders(self):
        self.click(*self.feed_orders)