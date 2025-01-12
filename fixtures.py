import requests
import pytest
from data import *

URL_registration = "https://stellarburgers.nomoreparties.site/api/auth/register"
URL_delete = "https://stellarburgers.nomoreparties.site/api/auth/user"
URL_login = "https://stellarburgers.nomoreparties.site/api/auth/login"
test_data = {
    "email": new_email,
    "password": test_password,
    "name": test_name
}

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