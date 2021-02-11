# Name:         scrapenames.py
# Author:       ~tweska
# Description:  Scrape all usernames of users that changed their
#               personal tilde club page.

from lxml import html
import requests

URL = 'https://tilde.club/'
SELECTOR = "descendant-or-self::ul[@class and contains(concat(' ', normalize-space(@class), ' '), ' user-list ')]/descendant-or-self::*/li/descendant-or-self::*/a/text()"

page = requests.get(URL)
tree = html.fromstring(page.content)

users = tree.xpath(SELECTOR)


if __name__ == '__main__':
    # Print all usernames to stdout.
    for user in users:
        print(user)
