from consts import USER
from view_user_profile import *
from config_parser import CONFIG
from user_info import *
from instagram_user import User

USERNAME = CONFIG['CREDENTIALS']['USERNAME']
PASSWORD = CONFIG['CREDENTIALS']['PASSWORD']


def get_into_the_user(user, username, password):
    # check_user(user)
    site_login(username, password)
    check_login()
    sleep(2)
    enter_user_profile(user)
    sleep(2)


def main():
    get_into_the_user(USER, USERNAME, PASSWORD)
    posts = get_user_posts_number()
    followers = get_user_followers_number()
    following = get_user_following_number()
    # -------------------
    user = User(posts, followers, following)
    print(f"number of {USER} posts. {user.posts} posts")
    print(f"number of {USER} followers. {user.followers} followers")
    print(f"number of {USER} following. {user.following} following")


if __name__ == '__main__':
    main()
