from utilities import *
from compile_codes import *

done = False
start = time.time()
if sys.platform == "linux":
    env = platform.freedesktop_os_release().get("ID")
else:
    env = platform.system()


if env.lower() == "ubuntu":
    kw = os.getcwd() + "/"
    data_path = kw + "_data/"
    source = kw + "_pages/"
    destination = kw + "kwfied/"
    print("IP Address:", subprocess.check_output("hostname -I | awk '{print $1}'", shell=True).rstrip().decode("utf-8"))

    passed, failed = compile_codes(source, destination, data_path)
    os.chdir(kw)
    # sudo snap remove firefox and then https://support.mozilla.org/en-US/kb/install-firefox-linux
    matched, unmatched = start_tests("firefox", data_path)
    # matched, unmatched = start_tests("chrome", data_path)
    done = True
elif env.lower() == "windows":
    data_path = "D:/kodingwindow.github.io/_data/"
    os.system("CLS")
    
    matched, unmatched = start_tests("chrome", data_path)
    # matched, unmatched = start_tests("msedge", data_path)
    done = True
else:
    print("Script works on Windows and Ubuntu only")


subprocess.run("pyclean kwtesting", shell=True, stderr=subprocess.DEVNULL)

# It prints the report if there are no exceptions.
if done:
    end = time.time()
    m, s = divmod(round(end - start), 60)
    h, m = divmod(m, 60)
    if matched + unmatched > 0:
        print("---------------------------------\nWebsite Report\n---------------------------------")
        print("Total Webpages Visited:", matched + unmatched)
        print("Total Titles Matched:", matched)
        print("Total Titles Unmatched:", unmatched)
    if passed  + failed > 0:
        print("---------------------------------\nCode Compilation Report\n---------------------------------")
        print("Total Files Compiled:", passed  + failed)
        print("Total Passed:", passed)
        print("Total Failed:", failed)
    print("---------------------------------")
    print("Total Execution Time:", f"{h:02d}:{m:02d}:{s:02d}")
