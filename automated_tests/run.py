"""
Author: Shubham Darda
Description: The automated tests on the specified browser are started by this script.
"""

from utilities import *
from compile_codes import *

start = time.time()
if sys.version_info.major == 3 and sys.version_info.minor >= 4:
    try:
        print("Starting automated tests on: " + platform.platform())
        if ubuntu:
            kw = os.getcwd() + "/"
            data_path = kw + "_data/"
            source = kw + "_pages/"
            destination = kw + "kwfied/"

            # sudo snap remove firefox and then https://support.mozilla.org/en-US/kb/install-firefox-linux
            # matched, unmatched = start_tests("firefox", data_path)
            matched, unmatched = start_tests("chrome", data_path)
            passed, failed = compile_codes(source, destination, data_path)
            os.chdir(kw)
        elif not ubuntu:
            data_path = "D:/kodingwindow.github.io/_data/"        
            # matched, unmatched = start_tests("chrome", data_path)
            matched, unmatched = start_tests("msedge", data_path)
        else:
            print("Script works on Windows and Ubuntu only")
    except:
        print("The script execution aborted due to the following possible reasons: \n1. The local server isn't up and running. \n2. The required driver isn't found at the given location. \n3. Due to unsupported OS, browser and driver versions \n4. If you manually intervened in the execution.\n5. Due to code changes done locally.")
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
    print(subprocess.check_output("google-chrome --version", shell=True).rstrip().decode("utf-8"))
if compiled > 0:
    print("---------------------------------\nCode Compilation Report\n---------------------------------")
    print("Total Files Compiled:", compiled)
    print("Total Passed:", passed)
    print("Total Failed:", failed)
    print("---------------------------------\nCompilers Version Used\n---------------------------------")
    print("gcc/g++", subprocess.check_output("g++ -dumpfullversion", shell=True).rstrip().decode("utf-8"))
    print(subprocess.check_output("javac --version", shell=True).rstrip().decode("utf-8"))
    print(subprocess.check_output("python3 --version", shell=True).rstrip().decode("utf-8"))
    print(subprocess.check_output("rustc --version", shell=True).rstrip().decode("utf-8"))
    print(subprocess.check_output("nasm --version", shell=True).rstrip().decode("utf-8"))

end = time.time()
m, s = divmod(round(end - start), 60)
h, m = divmod(m, 60)

if m >= 1:
    print("---------------------------------")
    print("Total Execution Time:", f"{h:02d}:{m:02d}:{s:02d}")
subprocess.run("pyclean kwtesting", shell=True, stderr=subprocess.DEVNULL)
