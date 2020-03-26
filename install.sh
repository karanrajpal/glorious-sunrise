#!/bin/bash
set +eux
sudo apt-get update
sudo apt-get install imagemagick -y
sudo apt-get install gifsicle

cd ~
git clone https://github.com/karanrajpal/glorious-sunrise.git

# Make media folder which doesn't exist
mkdir -p glorious-sunrise/media

# Write to crontab to run every morning
(crontab -l 2>/dev/null; echo "40 6 * * * python /home/pi/glorious-sunrise/scripts/take_sunrise_pics.py -n=150 -i=30 -g=10 -c=TRUE") | crontab -
