#!/bin/bash

# Clean the output directory by... removing it
rm -r out/

# Create a brand new output directory
mkdir out/
mkdir out/screenshots/

# Scrape the usernames of all users 
python3 scrapenames.py > out/changed_usernames.txt

# Take screenshots of all pages
python3 screenshot.py < out/changed_usernames.txt

# Zip the screenshots
cd out/
zip -r screenshots.zip screenshots/
cd ../

# Create html pages from template
python3 template.py < out/changed_usernames.txt

# Copy a bunch of stuff into output
cp -r template/static/ out/static/
cp template/index.html out/index.html
