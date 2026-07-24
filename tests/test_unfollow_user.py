from api.profile_api import ProfileAPI

def test_follow_user():
    api = ProfileAPI()

    username = "ranchod"
    response = api.unfollow_user(username)

    print("Status:", response.status_code)
    print("Response:", response.json())

    assert response.status_code in [201,200]
    assert response.json()["success"] is True