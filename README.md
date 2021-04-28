REQUIEREMENTS:

1. Raspberry Pi Zero W
2. WaveShare 2.13 ink screen V2.
3. PiSugar2 battery.
4. 16 GB microSD Card high performance.

THIS VERSION WILL ONLY WORK WITH WIFI CONNECTION OR ETHERNET
---
CONNECT TO A WIFI NETWORK
---
* sudo apt update
* sudo apt upgrade
* sudo apt install tor
* sudo apt remove python3-pip python-pip
* sudo apt install python3-pip
---
* sudo apt install libopenjp2-7 libtiff5
* sudo pip3 install papertty
---
* sudo raspi-config

- Interfacing Options -> SPI -> Yes
- Set autologin to ON
  * Reboot
---
* sudo apt install ttf-mscorefonts-installer
---
* sudo apt install git
* git clone https://github.com/curly60e/pyblockmicro.git
* cd pyblockmicro
* sudo cp papertty.service /etc/systemd/system
* sudo systemctl daemon-reload
* sudo systemctl enable papertty
* sudo systemctl start papertty
---
* sudo cp .bashrc /home/pi/ 
* sudo cp clocks.py /home/pi/
* sudo cp -r .git/ ..
* cp start.sh /home/pi/
* cd /home/pi/
* sudo chown root:root start.sh;sudo chmod 700 start.sh
---
* cd /home/pi/pyblockmicro/
* sudo pip3 install -r requirements.txt
---
* cd pyblockmicro
* sudo cp torrc /etc/tor/
---
Setup PiSugar2 Battery (OPTIONAL)
* curl http://cdn.pisugar.com/release/Pisugar-power-manager.sh | sudo bash
---
* reboot


DONATE PYBLOCK

Samourai Wallet Paynym:

<img src="images/codeimage.png" width="30%" />

Lightning KeySend:

<img src="images/keysend.png" width="30%" />

Monero:

<img src="images/qrcode.png" width="20%" />
