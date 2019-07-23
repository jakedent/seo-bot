# seo-bot-python
Simple SEO bot written in Python. Runs on OSX with Tor Browser Bundle Installed. 

# Requirements:
Time, Os, (Py)Socks, Stem, Subprocess
- pip3 install pysocks && pip3 install stem

# Using seobot.py
1. Download or clone this repository.
2. Update Tor Browser - open your Tor Browser as you normally would, or download from here: https://www.torproject.org
   - Tor Browser should update automatically on open. If it does not, check your preferences in the Tor Browser.
3. Close Tor Browser completley.
4. Open Terminal and cd to the seo-bot-python respository downloaded in step 1.
5. Run: sudo python3 seobot.py
6. Enter target URL.
7. Sit back and grab a coffee.

![gr](https://user-images.githubusercontent.com/10816773/61674548-2dabbd80-acec-11e9-841e-a2bdcf0cb6af.png)
 
# How seobot.py works
1. Sets up a default proxy at local host.
2. Initialises SSL. 
3. Takes a target URL from user input.
4. Opens Tor Browser, waits to load.
5. Opens target URL in new tab, waits to load.
6. Changes identity every 30 seconds through port 9051, previously initialised in steps 1 and 2.
7. Returns read and write bytes generated after each switch.

# Future updates 
1) Crawling the target URL pages as each Tor identity. 

# OLD Script is oldseobot.py
See https://jacobdent.com/blog/search-engine-optimisation-bot for information on how the bot works.
- Note, the blog post above contains instsructions meant only for the old version of the seobot now called, oldseobot.py.
