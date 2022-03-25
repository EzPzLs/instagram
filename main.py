from consts import USER
from view_user_profile import *
from config_parser import CONFIG
from user_listener import check_for_change
from instagram_user import User
from user_info import *

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
    posts = get_current_user_posts_number()
    followers = get_current_user_followers_number()
    following = get_current_user_following_number()
    # user instance
    user = User(posts, followers, following)
    print_purple(f"number of {USER} posts. {user.posts} posts")
    print_cyan(f"number of {USER} followers. {user.followers} followers")
    print_yellow(f"number of {USER} following. {user.following} following")
    check_for_change(user)


if __name__ == '__main__':
    main()
