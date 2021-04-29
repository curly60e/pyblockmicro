#!/bin/bash

echo " "
echo "Updating..."
echo " "
sudo apt update && sudo apt upgrade

echo "Enabling SPI port..."
echo " "
sudo sed -i 's/dtparam=spi=off/dtparam=spi=on/g' /boot/config.txt
sudo sed -i 's/#dtparam=spi=on/dtparam=spi=on/g' /boot/config.txt

echo "Installing packages required for the display to work..."
sudo apt remove python3-pip python-pip
sudo apt install tor python3-pip libopenjp2-7 libtiff5 ttf-mscorefonts-installer 
echo " "

sudo pip3 install -r requirements.txt
sudo cp torrc /etc/tor/
sudo cp .bashrc /home/pi/
sudo cp clocks.py /home/pi/
sudo cp boot.sh /home/pi/
sudo cp -r .git/ /home/pi/
sudo cp papertty.service /etc/systemd/system/
sudo cp start.sh /home/pi/
cd /home/pi/
sudo chown root:root start.sh;sudo chmod 700 start.sh
sudo systemctl daemon-reload
sudo systemctl enable papertty
sudo systemctl start papertty
echo " "
