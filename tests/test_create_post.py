from api.post_api import PostAPI


def test_create_image_post():

    api = PostAPI()

    response = api.create_image_post(
        text="Uploaded through automation",
        image_path="testdata/sampleimg.png"   # 
    )

    print("Status:", response.status_code)
    print("Response:", response.json())

    assert response.status_code in [200, 201]
    assert response.json()["success"] is True

    post_id = response.json()["post"]["id"]

    print("Created Post ID:", post_id)