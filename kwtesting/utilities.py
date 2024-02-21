import os, sys, yaml, time, re
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

baseurl = "http://localhost:4000/"
if sys.platform == 'linux':
    chrome_driver = Service("/usr/bin/chromedriver")
    firefox_driver = Service("/usr/bin/geckodriver")
    msedge_driver = Service("/usr/bin/msedgedriver")
    kw = '/home/kodingwindow/kodingwindow.github.io/'
    datapath = kw + '_data/'
    kwtesting = "/home/kodingwindow/kwtesting/"
else:
    chrome_driver = Service("D:\\Drivers\\chromedriver.exe")
    firefox_driver = Service("D:\\Drivers\\geckodriver.exe")
    msedge_driver = Service("D:\\Drivers\\msedgedriver.exe")
    datapath = 'D:/kodingwindow.github.io/_data/'

def verify_title(driver, path, expected_title):
    driver.maximize_window()
    driver.get(baseurl + path)   
    actual_title = driver.title
    if actual_title != expected_title:
        print("Actual Title  :", actual_title, "\nExpected Title:", expected_title, "\nPath:", path)
        print("Test Failed: Title Unmatched\n")

def verify_scrolling(driver):
    before_scroll = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    after_scroll = driver.execute_script("return document.body.scrollHeight")
    if after_scroll > before_scroll:
        element = driver.find_element(By.ID, "back-to-top")
        element.click()
        time.sleep(1)
    back_to_top = after_scroll = driver.execute_script("return document.body.scrollHeight")
    if back_to_top != before_scroll:
        print("Back to top: Unsuccessful")

def read_file(driver, kwfile, element):
    paths = []
    with open(datapath+'%s'%kwfile) as file:
        document = yaml.safe_load(file)
        try:
            parent = document["sidenav"][0]
            element_title = parent["parent"]
            element_url = parent["url"]
            if driver is not None:
                verify_title(driver, element_url, element_title)
                verify_scrolling(driver)
            element_size = len(document[element])
            for i in range(0, element_size):
                parent = document[element][i]
                try:
                    children = parent["children"]
                except KeyError:
                    pass
                else:
                    for child in children:
                        element_title = child["title"]
                        element_url = child["url"]
                        paths.append(element_url)
                        if driver is not None:
                            verify_title(driver, element_url, element_title)
        except KeyError:
            pass
    return paths