from api.auth_api import AuthAPI
from payloads.login_payload import login_payload
from utils.token_manager import TokenManager

def test_login():
    api = AuthAPI()

    payload = login_payload() 
    print(payload) 

    response = api.login(payload)

    assert response.status_code == 200

    body = response.json()

    assert body["success"] is True

    TokenManager.set_token(body["token"])