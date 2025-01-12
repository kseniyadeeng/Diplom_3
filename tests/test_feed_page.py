from page_objects.feed_page import FeedPage
from page_objects.authorization_page import AuthorizationPage
from page_objects.profile_page import ProfilePage
from page_objects.home_page import HomePage
import allure
from conftest import *
from fixtures import *


class TestFeedPage:
    @allure.title("если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_that_the_order_modal_window_is_visible(self, driver):
        authorization_page = AuthorizationPage(driver)
        authorization_page.opening_the_authorization_page()
        authorization_page.entering_email_in_the_login_form(test_email)
        authorization_page.entering_password_in_the_login_form(test_password)
        authorization_page.click_on_the_login_button()
        home_page = HomePage(driver)
        home_page.click_on_the_feed_orders()
        feed_page = FeedPage(driver)
        feed_page.click_on_the_first_order_on_the_list()
        feed_page.checking_that_the_order_modal_window_is_visible()

    @allure.title('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_registration_and_order_flow(self, driver, user_registration_and_delete):
        authorization_page = AuthorizationPage(driver)
        authorization_page.opening_the_authorization_page()
        authorization_page.entering_email_in_the_login_form(new_email)
        authorization_page.entering_password_in_the_login_form(test_password)
        authorization_page.click_on_the_login_button()
        home_page = HomePage(driver)
        home_page.move_bun()
        home_page.click_place_an_order()
        home_page.wait_cross_active()
        number1 = home_page.get_number_from_the_order_modal_window()
        home_page.click_cross_orders()
        profile_page = ProfilePage(driver)
        profile_page.click_on_the_personal_account_button()
        profile_page.click_on_the_history_orders_button()
        number2 = profile_page.get_number_from_the_order_history()
        profile_page.click_on_the_feed_orders()
        feed_page = FeedPage(driver)
        number3 = feed_page.get_number_from_the_order_number_in_the_order_feed()
        assert number3 == number2 == number1

    @allure.title("при создании нового заказа счётчик Выполнено за всё время увеличивается")
    def test_completed_for_all_time_counter_increases(self, driver):
        authorization_page = AuthorizationPage(driver)
        authorization_page.opening_the_authorization_page()
        authorization_page.entering_email_in_the_login_form(test_email)
        authorization_page.entering_password_in_the_login_form(test_password)
        authorization_page.click_on_the_login_button()
        home_page = HomePage(driver)
        home_page.click_on_the_feed_orders()
        feed_page = FeedPage(driver)
        number_before = feed_page.get_number_completed_for_all_time()
        home_page = HomePage(driver)
        home_page.click_on_the_button_constructor()
        home_page.move_bun()
        home_page.click_place_an_order()
        home_page.wait_cross_active()
        home_page.click_cross_orders()
        home_page.click_on_the_feed_orders()
        feed_page = FeedPage(driver)
        number_after = feed_page.get_number_completed_for_all_time()
        assert number_after == number_before + 1

    @allure.title("при создании нового заказа счётчик Выполнено за сегодня увеличивается")
    def test_completed_today_counter_increases(self, driver):
        authorization_page = AuthorizationPage(driver)
        authorization_page.opening_the_authorization_page()
        authorization_page.entering_email_in_the_login_form(test_email)
        authorization_page.entering_password_in_the_login_form(test_password)
        authorization_page.click_on_the_login_button()
        home_page = HomePage(driver)
        home_page.click_on_the_feed_orders()
        feed_page = FeedPage(driver)
        number_before = feed_page.get_number_completed_today()
        home_page = HomePage(driver)
        home_page.click_on_the_button_constructor()
        home_page.move_bun()
        home_page.click_place_an_order()
        home_page.wait_cross_active()
        home_page.click_cross_orders()
        home_page.click_on_the_feed_orders()
        feed_page = FeedPage(driver)
        number_after = feed_page.get_number_completed_today()
        assert number_after == number_before + 1

    @allure.title("после оформления заказа его номер появляется в разделе В работе")
    def test_number_appears_in_the_in_progress_section(self, driver):
        authorization_page = AuthorizationPage(driver)
        authorization_page.opening_the_authorization_page()
        authorization_page.entering_email_in_the_login_form(test_email)
        authorization_page.entering_password_in_the_login_form(test_password)
        authorization_page.click_on_the_login_button()
        home_page = HomePage(driver)
        home_page.move_bun()
        home_page.click_place_an_order()
        home_page.wait_cross_active()
        number1 = home_page.get_number_from_the_order_modal_window()
        home_page.click_cross_orders()
        home_page.click_on_the_feed_orders()
        feed_page = FeedPage(driver)
        number2 = feed_page.get_number_order_number_in_progress_1()
        assert number1 == number2