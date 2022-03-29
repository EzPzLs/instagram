from view_user_profile import *
from user_info import *


def check_for_change(user):
    count = 0
    while True:
        check_for_followers_change(user)
        sleep(10)
        count += 10
        print(count)


def grammar_check(difference):
    if difference > 1:
        return "s"
    return ""


def number_without_comma(number):
    return number.replace(',', '')


def check_for_followers_change(user):
    current_followers = number_without_comma(get_current_user_followers_number())
    last_time_checked_followers = number_without_comma(user.followers)
    difference = abs(int(current_followers) - int(last_time_checked_followers))
    plural = grammar_check(difference)
    if current_followers > last_time_checked_followers:
        print_cyan(f"You got {difference} new follower{plural} since the last check!")
        check_who_followed(difference)
    elif current_followers < last_time_checked_followers:
        print_yellow(f"You lost {difference} new follower{plural} since the last check!")
    else:
        print_light_purple("No changes since the last check")
    user.set_followers(current_followers)


def check_who_unfollowed():
    pass
