from selenium.webdriver.common.by import By
from driver_setup import driver


def get_user_info():
    info_array = driver.find_elements(By.CLASS_NAME, "g47SY ")
    return {
        "posts": info_array[0].text,
        "followers": info_array[1].text,
        "following": info_array[2].text
    }


def get_current_user_posts_number():
    return get_user_info()["posts"]


def get_current_user_followers_number():
    return get_user_info()["followers"]


def get_current_user_following_number():
    return get_user_info()["following"]
