# Name:         screenshots.py
# Author:       ~tweska
# Description:  Take a screenshot of all personal tilde club pages.

import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image

BASE_URL = 'https://tilde.club/'
OUTPUT_PATH = 'out/screenshots/'
CHROME_BINARY = '/home/tweska/.local/bin/chromium/chrome'

options = webdriver.ChromeOptions()
options.headless = True
options.binary_location = CHROME_BINARY
driver = webdriver.Chrome(options=options)
driver.set_window_size(800, 600)

# Read usernames from stdin.
for line in sys.stdin:
    user = line.strip()
    url = "{}~{}".format(BASE_URL, user)
    path = "{}{}.png".format(OUTPUT_PATH, user)

    print("Taking screenshot of: '{}'".format(url))

    try:
        driver.get(url)
        driver.get_screenshot_as_file(path)
    except:
        print("Error occured while taking screenshot of: '{}'".format(url))
        continue
    
    img = Image.open(path)
    img = img.resize((240, 180))
    img.save(path)

driver.quit()
