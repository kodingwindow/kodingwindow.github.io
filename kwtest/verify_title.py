import sys, yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
if sys.platform == 'linux':
    service = Service("/usr/bin/chromedriver")
    path = r'/home/kodingwindow/kodingwindow.github.io/_data/%s'
else:
    service = Service("D:\\Drivers\\chromedriver.exe")
    path = r'D:\kodingwindow.github.io\_data\%s'

driver = webdriver.Chrome(options=options, service=service)
driver.maximize_window()

def verify_title(url, expected_title):
    driver.get("http://localhost:4000/" + url)
    actual_title = driver.title
    if actual_title != expected_title:
        print("Actual Title  :", actual_title, "\nExpected Title:", expected_title, "\nURL:", url)
        print("Test Failed: Title Unmatched\n")

def read_file(kwfile, element):
    with open(path %kwfile) as file:
        document = yaml.safe_load(file)
        parent = document["sidenav"][0]
        element_title = parent["parent"]
        element_url = parent["url"]
        verify_title(element_url, element_title)
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
                    verify_title(element_url, element_title)

yml_files = ["c.yml", "cpp.yml", "java.yml", "csharp.yml", "python.yml", "r.yml", "julia.yml", "fsharp.yml", 
             "ds.yml", "octave.yml", "lisp.yml", "linux.yml", "dsa.yml", "mysql.yml", "mongodb.yml", "cg.yml",
             "selenium.yml", "rust.yml", "asm.yml", "cluster.yml", "about.yml"]
for filename in yml_files:
    read_file(filename, "sidenav")
    read_file(filename, "grandparent")

verify_title("", "Kodingwindow")
verify_title("search/", "Kodingwindow's Search")
verify_title("dashboard/", "Kodingwindow's Dashboard")
verify_title("404/", "404 Page Not Found")
verify_title("shubhamrdarda/", "Shubham Darda")
driver.close()