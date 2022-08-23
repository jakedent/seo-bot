from utils import *
import time


# browse for infinity
def browse_by_infinity(url: str):
    start_browse(url)
    i = 2
    while True:
        print("Times: {}".format(i))
        change_ip()
        i += 1


# browse for times
def browse_by_times(times: int, url: str):
    start_browse(url)
    for i in range(1, times):
        print("Times: {} / {}".format((i + 1), times))
        change_ip()
    tor_quit()


# change ip
def change_ip():
    ip_switch()
    generated_bytes()
    time.sleep(50)


# open tor and browse url
def start_browse(url: str):
    print("quit Tor")
    tor_quit()
    # set default proxy
    set_default_proxy()
    # start tor
    tor_start()
    time.sleep(10)
    # create new tab and go to url
    print("target for {}".format(url))
    tor_target(url)
    time.sleep(50)
