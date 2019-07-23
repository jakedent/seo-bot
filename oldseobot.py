# OLD SCRIPT
# This is an old script, please use seo-bot.py instead for better results.
import time
import socks
import os
from stem import Signal
from stem.control import Controller


socks.set_default_proxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9150)
print("Proxy == Local Host at 127.0.0.1 port 9150.")
time.sleep(1)

socks_on = socks.socksocket()
print("Secure Socket Layer initialized with PySocks ...")
time.sleep(1)


def tor_start():
    try:
        os.system('open /Applications/TorBrowser.app')
    except Exception as e:
        print(str(e), 'path fail')


def ip_switch():
    with Controller.from_port(port=9151) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)


tor_start()
time.sleep(30)

for x in range(100):
    ip_switch()
    time.sleep(30)


quit()
