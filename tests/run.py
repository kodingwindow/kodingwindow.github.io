"""
Author: Shubham Darda
Description: The automated tests on the specified browser are started by this script.
"""

from utilities import *
from compile import *

start = time.time()
if sys.version_info.major == 3 and sys.version_info.minor >= 4:
    try:
        print("Starting automated tests on: " + platform.platform())
        if ubuntu:
            gd = os.getcwd() + "/"
            data_path = gd + "_data/"
            source = gd + "pages/"
            destination = gd + "gdfied/"
            browser = "chrome" # firefox
            # sudo snap remove firefox and then https://support.mozilla.org/en-US/kb/install-firefox-linux
            matched, unmatched = start_tests(browser, data_path)
            passed, failed = compile_codes(source, destination, data_path)
            os.chdir(gd)
        elif not ubuntu:
            data_path = "D:/godarda.github.io/_data/"
            browser = "msedge" # chrome
            matched, unmatched = start_tests(browser, data_path)
        else:
            print("Script works on Windows and Ubuntu only")
    except:
        print("The script execution aborted due to the following possible reason(s): \n1. The local server isn't up and running. \n2. The required driver isn't found at the given location. \n3. Due to unsupported OS, browser and driver versions \n4. If you manually intervened in the execution.\n5. Due to code changes done locally.")
else:
    print("Python 3.4 or later is needed for execution.")


visited = matched + unmatched
compiled = passed  + failed
# It prints the report based on the number of pages visted and codes compiled.

if visited > 0:
    print("---------------------------------\nWebsite Report\n---------------------------------")
    print("Total Webpages Visited:", visited)
    print("Total Titles Matched:", matched)
    print("Total Titles Unmatched:", unmatched)
if compiled > 0:
    print("---------------------------------\nCode Compilation Report\n---------------------------------")
    print("Total Files Compiled:", compiled)
    print("Total Passed:", passed)
    print("Total Failed:", failed)
    print("---------------------------------\nResources Version\n---------------------------------")
    print("gcc/g++", subprocess.check_output("g++ -dumpfullversion", shell=True).rstrip().decode("utf-8"))
    print(subprocess.check_output("javac --version", shell=True).rstrip().decode("utf-8"))
    print(subprocess.check_output("python3 --version", shell=True).rstrip().decode("utf-8"))
    print(subprocess.check_output("rustc --version", shell=True).rstrip().decode("utf-8"))
    print(subprocess.check_output("nasm --version", shell=True).rstrip().decode("utf-8"))
    if browser == "firefox":
        print(subprocess.check_output("firefox --version", shell=True).rstrip().decode("utf-8"))
    elif browser == "msedge":
        print(subprocess.check_output("msedge --version", shell=True).rstrip().decode("utf-8"))
    elif browser == "chrome":
        print(subprocess.check_output("google-chrome --version", shell=True).rstrip().decode("utf-8"))
end = time.time()
m, s = divmod(round(end - start), 60)
h, m = divmod(m, 60)

if m >= 1:
    print("---------------------------------")
    print("Total Execution Time:", f"{h:02d}:{m:02d}:{s:02d}")
shutil.rmtree("tests/__pycache__", ignore_errors=True)
