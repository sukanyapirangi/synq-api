import pytest
from api.auth_api import AuthAPI
from payloads.login_payload import login_payload
from utils.token_manager import TokenManager


@pytest.fixture(scope="session", autouse=True)
def login():

    print("\n===== LOGIN FIXTURE STARTED =====")

    response = AuthAPI().login(login_payload())

    print("Login Status:", response.status_code)
    print("Login Response:", response.json())

    assert response.status_code == 200

    TokenManager.set_token(response.json()["token"])

    print("Token Stored:", TokenManager.get_token()[:20], "...")