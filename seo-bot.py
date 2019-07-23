import time
import socks
import os
from stem import Signal
from stem.control import Controller
import subprocess

target = input("Please enter FULL target URL: ")  # Target URL including http(s):// and www

# Set default proxy
try:
    socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9051)
    print("Proxy set for Local Host at 127.0.0.1 port 9051.")
except Exception as e:
    print("Error setting default proxy: {0}".format(e))
# Initialise Secure Socket Layer
try:
    socks_on = socks.socksocket()
    print("Secure Socket Layer initialized.")
except Exception as e:
    print("Unable to initialise Secure Socket Layer: {0}".format(e))


# Start TOR Browser - is best to start TOR, let it load and then go to target URL in the next function in a new tab
def tor_start():
    try:
        os.system('open /Applications/TorBrowser.app')
    except Exception as s:
        print("Unable to start Tor Browser: {0}".format(s))


# Go to target URL in new tab
def tor_target():
    try:
        subprocess.call(['open', '-a', 'TorBrowser', target])
    except Exception as t:
        print("Unable to start TOR: {0}".format(t))


# Request new identity from TOR
def ip_switch():
    try:
        with Controller.from_port(port=9051) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)
            print("Identity Switched.")
    except Exception as i:
        print("Unable to switch Identity: {0}".format(i))


# See generated read and write bytes
def generated_bytes():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        bytes_read = controller.get_info("traffic/read")
        bytes_written = controller.get_info("traffic/written")
        print("BOT generated read %s bytes and written %s." % (bytes_read, bytes_written))


tor_start()  # Call start Tor Browser function
time.sleep(30)  # Wait for TOR to load
tor_target()  # Call target URL function
time.sleep(45)  # Wait for website to load
generated_bytes()  # Initial read and write bytes

while True:  # Run forever, press Ctrl+C to quit
    ip_switch()
    generated_bytes()
    time.sleep(30)
