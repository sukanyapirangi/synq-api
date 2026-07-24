from api.profile_api import ProfileAPI

def test_get_user():
    api = ProfileAPI()

    username = "ulluka"

    response = api.get_user(username)

    print("Status", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 200