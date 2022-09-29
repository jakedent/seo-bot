import socks
import os
from stem import Signal
from stem.control import Controller
import subprocess

port = 9151


def set_default_proxy():
    # Set default proxy
    try:
        socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", port)
        print("Proxy set for Local Host at 127.0.0.1 port {}.".format(port))
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
        os.system('open /Applications/Tor\ Browser.app')
    except Exception as s:
        print("Unable to start Tor Browser: {0}".format(s))


# Go to target URL in new tab
def tor_target(url: str):
    try:
        subprocess.call(['open', '-a', 'Tor Browser', url])
    except Exception as t:
        print("Unable to start TOR: {0}".format(t))


def tor_quit():
    try:
        os.system('osascript -e \'quit app "Tor Browser.app"\'')
    except Exception as s:
        print("Unable to quit Tor Browser: {0}".format(s))


# Request new identity from TOR
def ip_switch():
    try:
        with Controller.from_port(port=port) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)
            print("Identity Switched.")
    except Exception as i:
        print("Unable to switch Identity: {0}".format(i))


# See generated read and write bytes
def generated_bytes():
    with Controller.from_port(port=port) as controller:
        controller.authenticate()
        bytes_read = controller.get_info("traffic/read")
        bytes_written = controller.get_info("traffic/written")
        print("BOT generated read %s bytes and written %s." % (bytes_read, bytes_written))
