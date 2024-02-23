from utilities import *
from selenium import webdriver

options = webdriver.FirefoxOptions()
driver = webdriver.Firefox(options=options, service=firefox_driver)
start_tests(driver)
