from view_user_profile import *
from user_info import check_for_changed_followers, get_current_user_followers_number, get_followers_list


def check_for_change(user):
    driver.refresh()
    sleep(2)
    check_for_followers_change(user)


def _number_without_comma(number):
    return number.replace(',', '')


def check_for_followers_change(user, new_followers_number=0, lost_followers_number=0):
    changed_followers = check_for_changed_followers(user)
    current_followers = user.get_followers_list()

    new_followers_list = []
    lost_followers_list = []

    current_followers_number = _number_without_comma(get_current_user_followers_number())

    if len(changed_followers) == 0:
        # It means no change
        print_light_purple("No changes since the last check")
    else:
        for follower in changed_followers:
            if follower in current_followers:
                # It Means that he was in the original followers list and he unfollowed :(
                lost_followers_number += 1
                user.lost_follower(follower)
                lost_followers_list.append(follower)
            else:
                # It Means that he was not in the original followers list and he followed :)
                new_followers_number += 1
                user.new_follower(follower)
                new_followers_list.append(follower)

    user.set_followers(current_followers_number)
    print_cyan(f"Number of new followers since the last check: {new_followers_number}")
    print("New followers: ")
    print(new_followers_list)
    print_yellow(f"Number of lost followers since the last check: {lost_followers_number}")
    print("Lost followers: ")
    print(lost_followers_list)

