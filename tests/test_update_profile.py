from api.profile_api import ProfileAPI
from payloads.update_profile_payload import update_profile_payload


def test_update_profile():

    api = ProfileAPI()

    payload = update_profile_payload()

    response = api.update_profile(payload)

    print("Status:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 200

    body = response.json()

    assert body["success"] is True

    profile = body["profile"]

    assert profile["displayName"] == payload["displayName"]
    assert profile["bio"] == payload["bio"]
    assert profile["location"] == payload["location"]
    assert profile["did"] == payload["did"]