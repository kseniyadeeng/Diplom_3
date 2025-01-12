from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure
from page_objects.base_page import BasePage
from locators import *


class AuthorizationPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.authorization_url = 'https://stellarburgers.nomoreparties.site/login'
        self.home_url = 'https://stellarburgers.nomoreparties.site/'
        self.registration_email_entry_field = (By.XPATH, registration_email_entry_field)
        self.registration_password_entry_field = (By.XPATH, registration_password_entry_field)
        self.login_button = (By.XPATH, login_button)

    @allure.step("Открытие страницы авторизации")
    def opening_the_authorization_page(self):
        self.open_page(self.authorization_url)

    @allure.step("Ввод почты")
    def entering_email_in_the_login_form(self, email: str):
        self.send_keys(*self.registration_email_entry_field, email)

    @allure.step("Ввод пароля")
    def entering_password_in_the_login_form(self, password: str):
        self.send_keys(*self.registration_password_entry_field, password)

    @allure.step("Клик на кнопку войти")
    def click_on_the_login_button(self):
        self.click(*self.login_button)

    @allure.step("Проверка, что текущий url - https://stellarburgers.nomoreparties.site/")
    def wait_home_url(self):
        self.assert_current_url(self.home_url)