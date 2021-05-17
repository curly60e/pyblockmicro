REQUIEREMENTS:

1. Raspberry Pi Zero W
2. WaveShare 2.13 ink screen V2.
3. PiSugar2 battery.
4. 16 GB microSD Card high performance.

THIS VERSION WILL ONLY WORK WITH WIFI CONNECTION OR ETHERNET
---
CONNECT TO A WIFI NETWORK

---
EASY WAY

``* sudo apt install git``

``* git clone https://github.com/curly60e/pyblockmicro.git``

``* cd pyblockmicro``

``* sudo sh first.sh``

---

``* sudo raspi-config``

- Set autologin to ON
  * Reboot
---
MANUAL WAY

``* sudo apt install git``

``* git clone https://github.com/curly60e/pyblockmicro.git``

``* cd pyblockmicro``

``* sudo apt update``

``* sudo apt upgrade``

``* sudo apt install tor``

``* sudo apt remove python3-pip python-pip``

``* sudo apt install python3-pip``

---

``* sudo apt install libopenjp2-7 libtiff5``

---

``* sudo raspi-config``

- Interfacing Options -> SPI -> Yes
- Set autologin to ON
  * Reboot
---

``* sudo apt install ttf-mscorefonts-installer``

---
``* sudo apt install git``

``* git clone https://github.com/curly60e/pyblockmicro.git``

``* cd pyblockmicro``

``* sudo pip3 install -r requirements.txt``

``* sudo cp torrc /etc/tor/``

``* sudo cp .bashrc /home/pi/ ``

``* sudo cp clocks.py /home/pi/``

``* sudo cp -r .git/ /home/pi/``

``* sudo cp papertty.service /etc/systemd/system``

``* sudo cp start.sh /home/pi/``

``* cd /home/pi/``

``* sudo chown root:root start.sh;sudo chmod 700 start.sh``

``* sudo systemctl daemon-reload``

``* sudo systemctl enable papertty``

``* sudo systemctl start papertty``

---

Setup PiSugar2 Battery (OPTIONAL)

``* curl http://cdn.pisugar.com/release/Pisugar-power-manager.sh | sudo bash``

---

``* sudo reboot``

---
Mobile Phone tethering to your PyBLOCK micro over Bluetooth ONLY ANDROID.

``* sudo apt-get install bluetooth bluez-utils bluez-compat``

``* sudo apt install python-dbus``

``* git clone https://github.com/WayneKeenan/RaspberryPi_BTPAN_AutoConnect.git``

``* sudo nano /etc/dhcpcd.conf``

  --- Add these lines ---
  
 ``interface bnep0``
  
 ``static ip_address=192.168.44.49/24``
  
 ``static routers=192.168.44.1``
  
 ``static domain_name_servers=192.168.44.1``
  
  --- Save and Exit ---
  
``* cd RaspberryPi_BTPAN_AutoConnect``

``* nano check-and-connect-bt-pan.sh``

  --- Edit the MAC address line and put your phone's MAC address ---
  
  ``BT_MAC_ADDR=YOURPHONESADDRESS``
  
  --- Save and Exit ---
  
``* sudo nano /etc/systemd/system/btpan.service``

  --- Create a Bluetooth service so it can start automatically on every boot and put these lines ---
  
  ``[Unit]``
  
  ``Description=BtPan``
  
  ``DefaultDependencies=no``

  ``[Service]``
  
  ``Type=simple``
  
  ``KillSignal=SIGINT``
  
  ``TimeoutStopSec=8``
  
  ``Restart=on-failure``

  ``### Change the paths below to match yours``
  
  ``WorkingDirectory=/home/pi/``
  
  ``ExecStart=/home/pi/startbt.sh``
  
  ``###``

  ``[Install]``
  
  ``WantedBy=sysinit.target``
  
  --- Save and Exit ---
  
``* sudo systemctl daemon-reload``

``* sudo systemctl enable btpan.service``

``* sudo systemctl start btpan.service``

``* sudo nano /home/pi/startbt.sh``


  --- Create a bash script to execute the service on every boot ---
  
  ``#!/bin/sh``

  ``## Put your options here - the service unit will run this script, so that``
  
  ``## you don't need to 'daemon-reload' every time you want to change settings.``
  
  ``##``
  
  ``## It's a good idea to allow only root to write to this file:``
  
  ``##``
  
  ``## sudo chown root:root check-and-connect-bt-pan.sh; sudo chmod 700 check-and-connect-bt-pan.sh``
  
  ``##``

  ``/home/pi/bin/check-and-connect-bt-pan.sh``
  
  --- Save and Exit ---
  
START YOUR MOBILE PHONE BLUETOOTH AND ALLOW INTERNET TETHERING OVER BLUETOOTH
 
ON YOUR RPI TYPE...
  
``* sudo chown root:root check-and-connect-bt-pan.sh; sudo chmod 700 check-and-connect-bt-pan.sh ``

``* sudo bluetoothctl``

``* [bluetooth]# scan on``

``* --- Search for your Phone MAC address ---``

``* [bluetooth]# pair YOURPHONEMACADDRESS``

``* [bluetooth]# trust YOURPHONEMACADDRESS``

``* [bluetooth]# exit``

``* sudo reboot"``



DONATE PYBLOCK

Samourai Wallet Paynym:

<img src="images/codeimage.png" width="30%" />

Lightning KeySend:

<img src="images/keysend.png" width="30%" />

Monero:

<img src="images/qrcode.png" width="20%" />
