# Search Engine Optimisation bot
Simple SEO bot written in Python. Runs on OSX with Tor Browser Bundle Installed. 

Refactor by [MorrisLin](https://github.com/UranusLin)

# Requirements:
```commandline
pip install -r requirements.txt 
```

# How to Use
1. Download or clone this repository.
2. Update Tor Browser - open your Tor Browser as you normally would, or download from here: https://www.torproject.org
   - Tor Browser should update automatically on open. If it does not, check your preferences in the Tor Browser.
3. Open Terminal and cd to the seo-bot-python respository downloaded in step 1.
4. Run: pip install -r requirements.txt  
5. Run: python main.py
6. choose mode times or infinity
7. input times(when choose times mode)
8. input URL
9. Sit back and grab a coffee.

# How seobot works
1. Sets up a default proxy at local host.
2. Initialises SSL. 
3. Takes a target URL from user input.
4. Opens Tor Browser, waits to load.
5. Opens target URL in new tab, waits to load.
6. Changes identity every 50 seconds through port 9151, previously initialised in steps 1 and 2.
7. Returns read and write bytes generated after each switch.

# History
* 0.1.1 (2022/08/23)
  * Refactor project architecture
  * Add requirement.txt
  * Add two mode for browse
  * Fix Mac open Tor not found 
  * Fix change IP connection refused
  

# Future updates 
1) support Windows
