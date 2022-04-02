from consts import USER
from view_user_profile import *
from config_parser import CONFIG
from user_listener import check_for_change
from instagram_user import User
from user_info import *

USERNAME = CONFIG['CREDENTIALS']['USERNAME']
PASSWORD = CONFIG['CREDENTIALS']['PASSWORD']


def get_into_the_user(username, password):
    site_login(username, password)
    sleep(2)
    enter_user_profile(username)


def menu(user):
    print_light_purple("Menu:")
    print_light_purple("Press 0 to exit")
    print_light_purple("Press 1 to check for change")
    option = int(input("Your choice: "))
    while option != 0:
        if option == 1:
            check_for_change(user)
        option = int(input("Your choice: "))
    driver.close()
    exit()


def main():
    # user instance
    get_into_the_user(USERNAME, PASSWORD)
    posts = get_current_user_posts_number()
    followers = get_current_user_followers_number()
    following = get_current_user_following_number()
    followers_list = get_followers_list()
    user = User(posts, followers, following, followers_list)
    # ------------
    print_purple(f"number of {USERNAME} posts. {user.posts} posts")
    print_cyan(f"number of {USERNAME} followers. {user.followers} followers")
    print_yellow(f"number of {USERNAME} following. {user.following} following")
    print("#######################################################")
    menu(user)


if __name__ == '__main__':
    main()
