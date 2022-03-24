from selenium import webdriver
from consts import PATH

driver = webdriver.Chrome(executable_path=PATH)
driver.maximize_window()
