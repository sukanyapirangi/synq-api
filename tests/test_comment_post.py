from api.post_api import PostAPI
from payloads.comment_payload import comment_payload

def test_comment_post():

    api = PostAPI()
    post_id = "b8ae0757-0a86-493e-86d6-9749dd89ee2b"

    response = api.comment_on_post(
        post_id,
        comment_payload("test comment")
    )

    print("status", response.status_code)
    print("Response", response.json())

    assert response.status_code == 201
    body = response.json()
    assert body["success"] is True
    assert response.json()["success"] is True
