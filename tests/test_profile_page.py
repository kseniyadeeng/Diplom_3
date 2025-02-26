from page_objects.profile_page import ProfilePage
from page_objects.authorization_page import AuthorizationPage
import allure
from conftest import *
from data import *

class TestProfilePage:
    @allure.title("переход по клику на Личный кабинет»")
    def test_the_transition_by_clicking_on_personal_account(self, driver):
        authorization_page = AuthorizationPage(driver)
        authorization_page.opening_the_authorization_page()
        authorization_page.entering_email_in_the_login_form(test_email)
        authorization_page.entering_password_in_the_login_form(test_password)
        authorization_page.click_on_the_login_button()
        profile_page = ProfilePage(driver)
        profile_page.click_on_the_personal_account_button()
        profile_page.assert_profile_url()

    @allure.title("переход в раздел История заказов»")
    def test_the_transition_by_clicking_on_history_orders(self, driver):
        authorization_page = AuthorizationPage(driver)
        authorization_page.opening_the_authorization_page()
        authorization_page.entering_email_in_the_login_form(test_email)
        authorization_page.entering_password_in_the_login_form(test_password)
        authorization_page.click_on_the_login_button()
        profile_page = ProfilePage(driver)
        profile_page.click_on_the_personal_account_button()
        profile_page.click_on_the_history_orders_button()
        profile_page.assert_order_history_url()

    @allure.title("выход из аккаунта")
    def test_the_logout(self, driver):
        authorization_page = AuthorizationPage(driver)
        authorization_page.opening_the_authorization_page()
        authorization_page.entering_email_in_the_login_form(test_email)
        authorization_page.entering_password_in_the_login_form(test_password)
        authorization_page.click_on_the_login_button()
        profile_page = ProfilePage(driver)
        profile_page.click_on_the_personal_account_button()
        profile_page.click_on_the_exit_button()
        profile_page.assert_login_url()