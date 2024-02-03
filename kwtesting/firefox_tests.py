from utilities import *
from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_experimental_option("excludeSwitches", ["enable-automation"])
driver = webdriver.Firefox(options = options, service = firefox_driver)

start = time.time()
for filename in os.listdir(datapath):
    read_file(driver, filename, "sidenav")
    read_file(driver, filename, "grandparent")

verify_title(driver, "", "Kodingwindow")
verify_title(driver, "search/", "Kodingwindow's Search")
verify_title(driver, "dashboard/", "Kodingwindow's Dashboard")
verify_title(driver, "404/", "404 Page Not Found")
verify_title(driver, "shubhamrdarda/", "Shubham Darda")
driver.close()
end = time.time()
m, s = divmod(round(end - start), 60)
h, m = divmod(m, 60)
print("Total Execution Time: "+f'{h:02d}:{m:02d}:{s:02d}')