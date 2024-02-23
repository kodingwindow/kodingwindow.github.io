from utilities import *
from selenium import webdriver

options = webdriver.EdgeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Edge(options=options, service=msedge_driver)
start_tests(driver)
