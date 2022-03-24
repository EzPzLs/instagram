from selenium.webdriver.common.by import By
from driver_setup import driver
from time import sleep
from config_parser import CONFIG

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


def enter_user_profile(user):
    driver.get(URL + user)
