class Routes:

    LOGIN = "/auth/login"

    REGISTER = "/auth/register"

    GLOBAL_FEED = "/feeds/global"

    CREATE_POST = "/posts"

    REACT_POST = "/posts/{post_id}/react"

    COMMENT_POST = "/comments/post/{post_id}"
    FOLLOW_USER = "/follows/{username}"
    GET_USER = "/users/{username}"
    FOLLOWERS="/FOLLOWS/{user_id}/followers"
    FOLLOWING = "/follows/{user_id}/following"
    USER_POSTS = "/users/{username}/posts"
    UPDATE_PROFILE = "/users/profile"