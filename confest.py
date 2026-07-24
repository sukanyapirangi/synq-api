import pytest

from api.auth_api import AuthAPI
from payloads.login_payload import login_payload
from utils.token_manager import TokenManager


@pytest.fixture(scope="session", autouse=True)
def login():
    """Log in once per test session and store the token in TokenManager."""
    api = AuthAPI()
    payload = login_payload()
    response = api.login(payload)

    assert response.status_code == 200, (
        f"Login failed during setup: {response.status_code} {response.text}"
    )

    body = response.json()
    assert body.get("success") is True, f"Login response had success=False: {body}"

    TokenManager.set_token(body["token"])
