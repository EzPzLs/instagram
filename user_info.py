from selenium.webdriver.common.by import By
from driver_setup import driver


def get_user_description():
    user_description = driver.find_element(By.CSS_SELECTOR, "meta[name='description']")
    literally_the_content = user_description.get_attribute("content")
    """
    it looks like this (EXAMPLE):
    988 Followers, 673 Following, 51 Posts - See Instagram photos and videos from Eyal Zohar | אייל זהר (@eyalzohar3)
    so when I split it, the followers is in the [0] place, following in the [2] and the posts in the [4] place
    """
    return literally_the_content.split()


def get_user_posts_number():
    return get_user_description()[4]


def get_user_followers_number():
    return get_user_description()[0]


def get_user_following_number():
    return get_user_description()[2]



