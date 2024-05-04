import os, sys, platform, yaml, time, re, subprocess, unittest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.edge.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.common.by import By
from selenium import webdriver

if "CI" in os.environ:
    baseurl = "http://localhost:4000/"
else:
    baseurl = "https://kodingwindow.com/"

website = "kodingwindow.com/"
matched = unmatched = 0


# It opens up the mentioned browser to start the automated tests.
def open_browser(browser):
    if browser == "chrome":
        options = webdriver.ChromeOptions()
        if "CI" in os.environ:
            options.add_argument('--headless')
            print("Headless automated tests are started...")
        else:
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


# It verifies the title of each page and returns the total count of matched and unmatched titles.
def verify_title(driver, path, expected_title):
    global matched, unmatched
    driver.maximize_window()
    driver.get(baseurl + path)
    actual_title = driver.title
    if actual_title != expected_title:
        print("Title Unmatched: " + website + path)
        unmatched += 1
    else:
        print("Title Matched: " + website + path)
        matched += 1


# It verifies the back-to-top button is working on each segment and passes if the scroll bar is at the top.
def verify_scrolling(driver):
    try:
        before_scroll = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        after_scroll = driver.execute_script("return document.body.scrollHeight")
        if after_scroll > before_scroll:
            driver.find_element(By.ID, "backtotop").click()
            time.sleep(1)
        back_to_top = after_scroll = driver.execute_script("return document.body.scrollHeight")
        if back_to_top != before_scroll:
            print("Back to top: Unsuccessful")
    except:
        pass


''' It reads the segment files from the _data folder and extracts the URLs to navigate. 
Lastly, it returns the list of paths (which is required in compile_codes.py). '''
def read_file(driver, data_path, file_name, element):
    paths = []
    with open(data_path + "%s" % file_name) as file:
        document = yaml.safe_load(file)
        try:
            element_size = len(document[element])
            for i in range(0, element_size):
                parent = document[element][i]
                if element == "sidenav":
                    element_title = parent["parent"]
                    element_url = parent["url"]
                    if driver is not None:
                        verify_title(driver, element_url, element_title)
                        verify_scrolling(driver)
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


''' It starts the test by taking the name of the browser and the location of the data folder and 
performs automated tests such as verifying the title of each page and scrolling. 
In the end, it returns the total count of matched and unmatched titles. '''
def start_tests(browser, data_path):
    driver = open_browser(browser)
    for file_name in os.listdir(data_path):
        read_file(driver, data_path, file_name, "sidenav")
        read_file(driver, data_path, file_name, "grandparent")
    verify_title(driver, "", "Kodingwindow")
    verify_title(driver, "search/", "Kodingwindow's Search")
    verify_title(driver, "404/", "404 Page Not Found")
    verify_title(driver, "shubhamrdarda/", "Shubham Darda")
    driver.delete_all_cookies()
    driver.quit()
    return matched, unmatched
