from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure
from page_objects.base_page import BasePage
from locators import *


class FeedPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.the_first_order_on_the_list = (By.XPATH, the_first_order_on_the_list)
        self.order_modal_window = (By.XPATH, order_modal_window)
        self.order_number_in_the_order_feed = (By.XPATH, order_number_in_the_order_feed)
        self.completed_for_all_time = (By.XPATH, completed_for_all_time)
        self.completed_today = (By.XPATH, completed_today)
        self.order_number_in_progress_1 = (By.XPATH, order_number_in_progress_1)

    @allure.step("Клик на первый заказ")
    def click_on_the_first_order_on_the_list(self):
        self.click(*self.the_first_order_on_the_list)

    @allure.step("Проверка на видимость модального окна")
    def checking_that_the_order_modal_window_is_visible(self):
        self.wait_until_visible(*self.order_modal_window)

    @allure.step("Получение номера заказа на странице заказов")
    def get_number_from_the_order_number_in_the_order_feed(self) -> int:
        return self.get_number(*self.order_number_in_the_order_feed)

    @allure.step("Получение количества заказов за все время")
    def get_number_completed_for_all_time(self) -> int:
        return self.get_number(*self.completed_for_all_time)

    @allure.step("Получение количества заказов за сегодня")
    def get_number_completed_today(self) -> int:
        return self.get_number(*self.completed_today)

    @allure.step("Получение первого номера в статусе 'В работе'")
    def get_number_order_number_in_progress_1(self) -> int:
        return self.get_number(*self.order_number_in_progress_1)