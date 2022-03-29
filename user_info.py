from selenium.webdriver.common.by import By
from driver_setup import driver
from time import sleep


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


def click_button(info_object):
    driver.find_element(By.XPATH, f"//a[contains(@href, '/{info_object}')]").click()


def get_followers_list():
    click_button("followers")
    sleep(2)
    scroll_box = driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[2]")
    last_ht, = 0
    ht = 1
    while last_ht != ht:
        last_ht = ht
        sleep(2)
        # scroll down and retrun the height of scroll (JS script)
        ht = driver.execute_script(
            """ 
            arguments[0].scrollTo(0, arguments[0].scrollHeight);
            return arguments[0].scrollHeight; """, scroll_box)
    # ------------------
    sleep(5)
    links = scroll_box.find_elements(By.TAG_NAME, 'a')
    sleep(2)
    names = [name.text for name in links if name.text != '']
    return names


# the next function is not best practice, when new follower add, he is at the top of the followers list,
# this function takes the top of the list by the new_followers number
def check_who_followed(new_followers_number):
    for i in range(1, new_followers_number + 1):
        x = f"/html/body/div[6]/div/div/div/div[2]/ul/div/li[{i}]"
        y = driver.find_element(By.XPATH, x)
        print("new follower: " + y.text)
    #x = driver.find_elements(By.XPATH, f"//li/*[position()<={new_followers_number}]")
    # links = x.find_elements(By.TAG_NAME, 'a')
    sleep(2)
    # names = [name.text for name in links if name.text != '']
    # print(names)
