from utilities import *

start = time.time()
if sys.platform == "linux":
    import chrome_tests
    import firefox_tests
    import linux_tests
else:
    import msedge_tests
end = time.time()
m, s = divmod(round(end - start), 60)
h, m = divmod(m, 60)
print("Total Execution Time: " + f"{h:02d}:{m:02d}:{s:02d}")

# https://support.mozilla.org/en-US/kb/install-firefox-linux
