from api.profile_api import ProfileAPI

def test_get_followers():
    api = ProfileAPI()

    user_id = "ranchod"

    response = api.get_followers(user_id)

    print("status:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 200