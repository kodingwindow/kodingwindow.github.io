from utilities import *
from compile_codes import *

done = False
username = os.getlogin()
kw = "/home/"+username+"/kodingwindow.github.io/"
data_path = kw + "_data/"
source = kw + "_pages/"
destination = kw + "kwfied/"

start = time.time()

try:
    os.system("clear")
    # sudo snap remove firefox and then https://support.mozilla.org/en-US/kb/install-firefox-linux
    matched, unmatched = start_tests("firefox", data_path)
    # matched, unmatched = start_tests("chrome", data_path)
    passed, failed = compile_codes(source, destination, data_path)
    done = True
except:
    print("The script execution was aborted due to the following reasons: \n1. The local server isn't up and running. \n2. The required driver isn't found at the given location. \n3. Due to the mismatch of browser and driver versions \n4. If you manually intervened in the execution.\n5. Due to code changes done locally.")

os.chdir(kw)
subprocess.run("pyclean kwtesting", shell=True, stderr=subprocess.DEVNULL)

# It prints the report if there are no exceptions.
if done:
    end = time.time()
    m, s = divmod(round(end - start), 60)
    h, m = divmod(m, 60)
    print("---------------------------------\nWebsite Report\n---------------------------------")
    print("Total Webpages Visited:", matched + unmatched)
    print("Total Titles Matched:", matched)
    print("Total Titles Unmatched:", unmatched)
    print("---------------------------------\nCode Compilation Report\n---------------------------------")
    print("Total Files Compiled:", passed  + failed)
    print("Total Passed:", passed)
    print("Total Failed:", failed)
    print("---------------------------------")
    print("Total Execution Time:", f"{h:02d}:{m:02d}:{s:02d}")
