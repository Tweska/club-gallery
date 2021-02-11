# Name:         template.py
# Author:       ~tweska
# Description:  Fill template in template path with data.

import sys

TEMPLATE_PATH = 'template/'
OUTPUT_PATH = 'out/'

template_file = open("{}template.html".format(TEMPLATE_PATH))
template = template_file.read()
template_file.close()

item_file = open("{}item.html".format(TEMPLATE_PATH))
item = item_file.read()
item_file.close()

users = { 'a': [], 'b': [], 'c': [], 'd': [], 'e': [], 'f': [], 'g': [], \
          'h': [], 'i': [], 'j': [], 'k': [], 'l': [], 'm': [], 'n': [], \
          'o': [], 'p': [], 'q': [], 'r': [], 's': [], 't': [], 'u': [], \
          'v': [], 'w': [], 'x': [], 'y': [], 'z': [], 'other': [] }

# Read usernames from stdin.
for line in sys.stdin:
    user = line.strip()
    key = user[0]
    if key not in users.keys():
        key = 'other'
    users[key].append(user)

for key in users.keys():
    items = ""
    for user in users[key]:
        items += item.format(user, user, user)
    html = template.format(items)

    f = open('{}{}.html'.format(OUTPUT_PATH, key), 'w')
    f.write(html)
    f.close()
