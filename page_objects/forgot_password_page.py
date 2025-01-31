from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
import allure

import locators
from page_objects.base_page import BasePage
from locators import *


class ForgotPasswordPage(BasePage):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)
        self.login_url = 'https://stellarburgers.nomoreparties.site/login'
        self.forgot_password_url = 'https://stellarburgers.nomoreparties.site/forgot-password'
        self.reset_password_url = 'https://stellarburgers.nomoreparties.site/reset-password'
        self.recover_password_button = (By.XPATH, recover_password_button)
        self.password_recovery_input_field = (By.XPATH, password_recovery_input_field)
        self.active_password_entry_field_window_in_the_password_recovery_form = (By.XPATH, active_password_entry_field_window_in_the_password_recovery_form)
        self.reset_password_button_on_the_recovery_page = (By.XPATH, reset_password_button_on_the_recovery_page)
        self.entering_password_in_the_password_recovery_form = (By.XPATH, entering_password_in_the_password_recovery_form)
        self.eye_button = (By.XPATH, eye_button)
        self.password_recovery_input_field_hidden = (By.XPATH, password_recovery_input_field_hidden)

    @allure.step("Открытие страницы авторизации")
    def opening_the_login_page(self):
        self.open_page(self.login_url)

    @allure.step("Клик на кнопку 'восстановить пароль'")
    def click_on_the_reset_password_button(self):
        self.click(*self.recover_password_button)

    @allure.step("Проверка на то, что текущий урл - https://stellarburgers.nomoreparties.site/forgot-password")
    def assert_forgot_password_url(self):
        self.assert_current_url(self.forgot_password_url)

    @allure.step("Ввод почты в форму восстановления пароля")
    def entering_email_in_the_password_recovery_form(self, email: str):
        self.send_keys(*self.password_recovery_input_field, email)

    @allure.step("Ввод пароля в форму восстановления пароля")
    def click_on_the_reset_password_button_on_the_recovery_page(self):
        self.click(*self.reset_password_button_on_the_recovery_page)

    @allure.step("Проверка на то, что текущий урл https://stellarburgers.nomoreparties.site/reset-password")
    def assert_reset_password_url(self):
        self.wait_for_url(self.reset_password_url)
        self.assert_current_url(self.reset_password_url)

    @allure.step("Ввод пароля")
    def entering_password_in_the_password_recovery(self, password: str):
        self.send_keys(*self.entering_password_in_the_password_recovery_form, password)

    @allure.step("Клик на кнопку с глазом")
    def click_on_the_eye_button(self):
        self.long_press(*self.eye_button, 1)

    @allure.step("Проверка на то, что пароль виден")
    def assert_checking_that_the_hidden_password_is_visible(self):
        assert self.wait_until_visible(*self.password_recovery_input_field_hidden).is_displayed()

    @allure.step("Проверка на то, что форма активна")
    def checking_that_the_recovery_form_is_active(self):
        self.wait_until_visible(*self.active_password_entry_field_window_in_the_password_recovery_form)

    @allure.step('Проверка на то, что форма видна')
    def assert_checking_that_the_recovery_form_is_active(self):
        assert self.wait_until_visible(*self.active_password_entry_field_window_in_the_password_recovery_form).is_displayed()
