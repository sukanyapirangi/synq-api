from api.profile_api import ProfileAPI

def test_get_following():

    api = ProfileAPI()

    user_id = "ulluka"

    response = api.get_following(user_id)

    print("Status:", response.status_code)
    print("Response:", response.json())

    assert response.status_code == 200