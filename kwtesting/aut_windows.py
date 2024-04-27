from utilities import *

done = False
kwdata = "D:/kodingwindow.github.io/_data/"

start = time.time()
try:
    start_tests("chrome", kwdata)
    start_tests("msedge", kwdata)
    done = True
except:
    print("The script execution was aborted due to the following reasons: \n1. The local server isn't up and running. \n2. The required driver isn't found at the given location. \n3. Due to the mismatch of browser and driver versions \n4. If you manually intervened in the execution.\n5. Due to code changes done locally.")

os.system("pyclean kwtesting")

if done:
    end = time.time()
    m, s = divmod(round(end - start), 60)
    h, m = divmod(m, 60)
    print("---------------------------------\nWebsite Report\n---------------------------------")
    print("Total Webpages Visited:", matched + unmatched)
    print("Total Titles Matched:", matched)
    print("Total Titles Unmatched:", unmatched)
    print("---------------------------------")
    print("Total Execution Time:", f"{h:02d}:{m:02d}:{s:02d}")

