from utilities import *
from compile_codes import *

success = False
username = os.getlogin()
kw = "/home/"+username+"/kodingwindow.github.io/"
kwdata = kw + "_data/"
source = kw + "_pages/"
destination = kw + "kwfied/"

start = time.time()
try:
    start_tests("chrome", kwdata)
    start_tests("firefox", kwdata)
    compile_all(source, destination, kwdata)
    os.system("pyclean kwtesting >/dev/null 2>&1")
    success = True
except:
    print("The script execution was aborted due to the following reasons: \n1. The local server isn't up and running. \n2. The required driver isn't found at the given location. \n3. Due to the mismatch of browser and driver versions \n4. If you manually intervened in the execution.")

if success:
    end = time.time()
    m, s = divmod(round(end - start), 60)
    h, m = divmod(m, 60)
    print("Total Execution Time: " + f"{h:02d}:{m:02d}:{s:02d}")

# https://support.mozilla.org/en-US/kb/install-firefox-linux
