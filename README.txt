THIS VERSION WILL ONLY WORK WITH WIFI CONNECTION OR ETHERNET
---
CONNECT TO A WIFI NETWORK
---
sudo apt update
sudo apt upgrade
sudo apt install tor
sudo apt remove python3-pip python-pip
sudo apt install python3-pip
---
sudo apt install libopenjp2-7 libtiff5
sudo pip3 install papertty
---
sudo raspi-config

Interfacing Options -> SPI -> Yes
Reboot
---
sudo apt install ttf-mscorefonts-installer
---
sudo cp papertty.service /etc/systemd/system
sudo systemctl daemon-reload
sudo systemctl enable papertty
sudo systemctl start papertty
---
sudo cp .bashrc /home/pi/ 
sudo cp clocks.py /home/pi/
cp start.sh /home/pi/
cd /home/pi/
sudo chown root:root start.sh;sudo chmod 700 start.sh
---
sudo pip3 install -r requirements.txt
---
sudo cp torrc /etc/tor/
---
reboot
