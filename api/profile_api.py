from api.base_api import BaseAPI
from endpoints.routes import Routes

class ProfileAPI(BaseAPI):

    def follow_user(self, username):
        endpoint = Routes.FOLLOW_USER.format(username=username)
        return self.post(endpoint=endpoint)
    
    def unfollow_user(self, username):
        endpoint = Routes.FOLLOW_USER.format(username=username)
        return self.delete(endpoint=endpoint)
    def get_user(self, username):
        endpoint = Routes.GET_USER.format(username=username)
        return self.get(endpoint=endpoint)
    
    def get_followers(self, user_id):
        endpoint = Routes.FOLLOWERS.format(user_id=user_id)
        return self.get(endpoint=endpoint)
    
    def get_following(self, user_id):
        endpoint = Routes.FOLLOWING.format(user_id=user_id)
        return self.get(endpoint=endpoint)
    
    def get_user_posts(self, username):
        endpoint = Routes.USER_POSTS.format(username=username)
        return self.get(endpoint=endpoint)
    
    def update_profile(self, payload):
        return self.put(
            endpoint=Routes.UPDATE_PROFILE,
            json=payload
        )