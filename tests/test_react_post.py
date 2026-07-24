from api.post_api import PostAPI
from payloads.react_payload import react_payload

def test_react_post():
    api = PostAPI()

    post_id = "b8ae0757-0a86-493e-86d6-9749dd89ee2b"

    response = api.react_to_post(
        post_id,
        react_payload("like")
    )
    print("status",response.status_code)
    print("Response", response.json())

    assert response.status_code == 200

