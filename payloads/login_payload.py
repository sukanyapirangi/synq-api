from config.config import Config

def login_payload():
    return {
        "username": Config.USERNAME,
        "password": Config.PASSWORD
    }