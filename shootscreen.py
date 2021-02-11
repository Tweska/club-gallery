# Name:         shootscreen.py
# Author:       ~tweska
# Description:  Take a screenshot of all personal tilde club pages
#               that have been changed.

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from PIL import Image

from scrapenames import users

BASE_URL = 'https://tilde.club/'
SCREENSHOT_PATH = 'screenshots/'

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)
driver.set_window_size(800, 600)

def shootscreen(username, verbose=True):
    url = "{}{}".format(BASE_URL, username)
    path = "{}{}.png".format(SCREENSHOT_PATH, username[1:])
    
    print("Taking screenshot of: '{}'".format(url))
    
    try:
        driver.get(url)
        driver.get_screenshot_as_file(path)
    except:
        print("Error occured while taking screenshot of: '{}'".format(url))
        return
    
    img = Image.open(path)
    img = img.resize((240, 180))
    img.save(path)

for user in users:
    shootscreen(user)

driver.quit()
