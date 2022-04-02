from selenium.webdriver.common.by import By
from driver_setup import driver
from time import sleep

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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


def get_followers_list():
    driver.find_element(By.XPATH, f"//a[contains(@href, '/followers')]").click()
    sleep(2)
    scroll_box = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[2]")
    last_ht = 0
    ht = 1

    x = len(driver.find_elements(By.XPATH, "/html/body/div[6]/div/div/div/div[2]/div[1]/h4"))

    while last_ht != ht and x == 0:
        x = len(driver.find_elements(By.XPATH, "/html/body/div[6]/div/div/div/div[2]/div[1]/h4"))
        last_ht = ht
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "PZuss"))
            # this element appears when the followers are fully loaded
        )
        # scroll down and retrun the height of scroll (JS script)
        ht = driver.execute_script(
            """ 
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight; """, scroll_box)
    # ------------------
    followers_list = driver.find_element(By.CLASS_NAME, "PZuss")
    links = followers_list.find_elements(By.TAG_NAME, 'a')
    # driver.execute_script("window.history.go(-1)")
    names = [name.text for name in links if name.text != '']
    return names


# This functions returns the followers the followed and unfollowed as a list
def check_for_changed_followers(user):
    current_followers = user.get_followers_list()
    after_check_followers = get_followers_list()

    difference_1 = set(current_followers).difference(set(after_check_followers))
    difference_2 = set(after_check_followers).difference(set(current_followers))

    changed_followers = list(difference_1.union(difference_2))

    return changed_followers


def check_who_unfollowed(user):
    pass


# the next function is not best practice, when new follower add, he is at the top of the followers list,
# this function takes the top of the list by the new_followers number

# TODO change logic
def check_who_followed2(new_followers_number):
    new_followers = []
    # click_button("followers")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "PZuss"))
        # this element appears when the followers are fully loaded
    )
    for i in range(1, new_followers_number + 1):
        follower = f"/html/body/div[6]/div/div/div/div[2]/ul/div/li[{i}]"
        new_followers.append(driver.find_element(By.XPATH, follower).text)
    driver.execute_script("window.history.go(-1)")
    print("new followers: ")
    print(new_followers)
    return new_followers
