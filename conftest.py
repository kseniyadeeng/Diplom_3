import pytest
import requests

from helpers import WebdriverFactory
from Urls import *
from data import *
from page_objects.authorization_page import AuthorizationPage


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    driver = WebdriverFactory.getWebdriver(browser)
    yield driver
    driver.quit()

@pytest.fixture(scope="function")
def user_registration_and_delete():
    response = requests.post(URL_registration, json=test_data)
    assert response.status_code == 200
    assert response.json()["success"] is True

    access_token = response.json()["accessToken"]
    yield access_token

    delete_response = requests.delete(URL_delete, headers={"Authorization": access_token})
    assert delete_response.status_code == 202
    assert delete_response.json()["success"] is True

@pytest.fixture
def authorization():
    authorization_page = AuthorizationPage(driver)
    authorization_page.opening_the_authorization_page()
    authorization_page.entering_email_in_the_login_form(test_email)
    authorization_page.entering_password_in_the_login_form(test_password)
    authorization_page.click_on_the_login_button()

