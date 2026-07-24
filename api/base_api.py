import requests

from config.config import Config

from utils.token_manager import TokenManager


class BaseAPI:

    def __init__(self):

        self.base_url = Config.BASE_URL

    def get_headers(self):

        headers = {
            "Content-Type": "application/json"
        }

        token = TokenManager.get_token()

        if token:
            headers["Authorization"] = f"Bearer {token}"

        return headers

    def get(self, endpoint, params=None):

        return requests.get(
            self.base_url + endpoint,
            headers=self.get_headers(),
            params=params,
            timeout=Config.TIMEOUT
        )

    def post(self, endpoint, json=None, data=None, files=None):

        headers = self.get_headers()

        if files:
            headers.pop("Content-Type", None)

        return requests.post(
            self.base_url + endpoint,
            headers=headers,
            json=json,
            data=data,
            files=files,
            timeout=Config.UPLOAD_TIMEOUT if files else Config.TIMEOUT
        )

    def put(self, endpoint, json=None):

        return requests.put(
            self.base_url + endpoint,
            headers=self.get_headers(),
            json=json,
            timeout=Config.TIMEOUT
        )

    def delete(self, endpoint):

        return requests.delete(
            self.base_url + endpoint,
            headers=self.get_headers(),
            timeout=Config.TIMEOUT
        )