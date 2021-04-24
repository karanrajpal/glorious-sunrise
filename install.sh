#!/bin/bash

# Please note: This install script is roughly cobbled together for a new raspberry pi and might fail on re-install.
# Just re-install stuff as needed from below
set +eux
sudo apt-get update
sudo apt-get install imagemagick -y
sudo apt-get install gifsicle

# cd ~
# git clone https://github.com/karanrajpal/glorious-sunrise.git


# Install pip
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py

rm get-pip.py

cd scripts
pip install picamera
cd ..

# Make media folder which doesn't exist
mkdir -p media


# Installing node
# https://www.instructables.com/Install-Nodejs-and-Npm-on-Raspberry-Pi/
echo "Install nodejs following the instructions in the article above and then continue"
exit 1
#sudo apt install nodejs -y
# sudo apt install npm -y

# We also want to prevent permission errors, so we need following operations (credits to https://stackoverflow.com/questions/49894620/npx-command-not-found):
mkdir ~/.npm-global # create folder where npm will install packages
npm config set prefix '~/.npm-global' # configure npm
echo 'export PATH=~/.npm-global/bin:$PATH' >> ~/.profile # add folder to path in user profile
source ~/.profile # reload current user profile

# Installing n8n
npm install n8n -g
n8n

# Write to crontab to run every morning
(crontab -l 2>/dev/null; echo "10 6 * * * python /home/pi/glorious-sunrise/scripts/take_sunrise_pics.py -n=150 -i=40 -g=10 -c=TRUE") | crontab -
