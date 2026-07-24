from api.base_api import BaseAPI
from endpoints.routes import Routes


class PostAPI(BaseAPI):

    def create_text_post(self, text):

        data = {
            "text": text
        }

        return self.post(
            endpoint=Routes.CREATE_POST,
            data=data
        )

    def create_image_post(self, text, image_path):

        data = {
            "text": text
        }

        import mimetypes
        import os
        mime_type, _ = mimetypes.guess_type(image_path)
        mime_type = mime_type or "image/png"
        files = {
            "image": (os.path.basename(image_path), open(image_path, "rb"), mime_type)
        }

        return self.post(
            endpoint=Routes.CREATE_POST,
            data=data,
            files=files
        )
    
    def react_to_post(self, post_id, payload= None):
        endpoint = Routes.REACT_POST.format(post_id=post_id)

        return self.post(
            endpoint=endpoint,
            json=payload
        )
    
    def comment_on_post(self, post_id, payload):
        endpoint = Routes.COMMENT_POST.format(post_id=post_id)
        return self.post(
            endpoint=endpoint,
            json=payload
        )