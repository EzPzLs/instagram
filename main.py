from consts import USER
from time import sleep
from view_user_profile import enter_user_profile, site_login
from config_parser import CONFIG

USERNAME = CONFIG['CREDENTIALS']['USERNAME']
PASSWORD = CONFIG['CREDENTIALS']['PASSWORD']


def main():
    site_login(USERNAME, PASSWORD)
    sleep(2)
    enter_user_profile(USER)


if __name__ == '__main__':
    main()
