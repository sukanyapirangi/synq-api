from api.base_api import BaseAPI
from endpoints.routes import Routes

class AuthAPI(BaseAPI):
    def login(self, payload):
        return self.post(
            endpoint=Routes.LOGIN,
            json=payload
        )