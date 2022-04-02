from selenium.webdriver.common.by import By
from driver_setup import driver
from time import sleep
from config_parser import CONFIG
from colors import *

# import requests

URL = CONFIG['INSTAGRAM']['URL']


def site_login(username, password):
    driver.get(URL)
    sleep(2)
    username_input = driver.find_element(By.CSS_SELECTOR, "input[name='username']")
    password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password']")
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()
    check_login(username, password)


def check_login(username, password):
    sleep(2)
    error = driver.find_elements(By.CSS_SELECTOR, "p[id='slfErrorAlert']")
    if len(error) == 0:
        print_green("nice login bro, no internet failure :)")
        return
    else:
        print_red("login failed, bad internet connection :(")
        print_yellow("lets try again")
        site_login(username, password)


def enter_user_profile(username):
    check_for_net_error()
    driver.get(URL + username)


def check_for_net_error():
    error = driver.find_elements(By.ID, "t")
    if len(error) != 0:
        print_red("DANG IT")
        print_red("we got some internet fails here")
        driver.close()
        exit()


# TODO
"""
def check_user(user):
    sleep(5)
    print(URL + user)
    response = requests.get(url=URL + user + "/")
    if ("404" not in response):
        print(response)
        print("yoyoyo")
        return True
    print("iuwqiwyeiuywevfyuifvo8iyv2e")
    return False
"""
