import os, sys, yaml, time, re
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver

baseurl = "http://localhost:4000/"


def startup(browser):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
        driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    elif browser == "msedge":
        options = webdriver.EdgeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
        driver = webdriver.Edge(options=options, service=Service(EdgeChromiumDriverManager().install()))
    elif browser == "firefox":
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(options=options, service=Service(GeckoDriverManager().install()))
    return driver


def verify_title(driver, path, expected_title):
    driver.maximize_window()
    driver.get(baseurl + path)
    actual_title = driver.title
    if actual_title != expected_title:
        print("Title Unmatched: https://kodingwindow.com/" + path)


def verify_scrolling(driver):
    before_scroll = driver.execute_script("return document.body.scrollHeight")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(1)
    after_scroll = driver.execute_script("return document.body.scrollHeight")
    if after_scroll > before_scroll:
        element = driver.find_element(By.ID, "backtotop")
        element.click()
        time.sleep(1)
    back_to_top = after_scroll = driver.execute_script("return document.body.scrollHeight")
    if back_to_top != before_scroll:
        print("Back to top: Unsuccessful")


def read_file(driver, kwdata, kwfile, element):
    paths = []
    with open(kwdata + "%s" % kwfile) as file:
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


def start_tests(browser, kwdata):
    driver = startup(browser)
    for kwfile in os.listdir(kwdata):
        read_file(driver, kwdata, kwfile, "sidenav")
        read_file(driver, kwdata, kwfile, "grandparent")
    verify_title(driver, "", "Kodingwindow")
    verify_title(driver, "search/", "Kodingwindow's Search")
    verify_title(driver, "404/", "404 Page Not Found")
    verify_title(driver, "shubhamrdarda/", "Shubham Darda")
    driver.delete_all_cookies()
    driver.quit()
