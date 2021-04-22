import base64, codecs, json, requests
import pickle
import os
import sys
import simplejson as json
from pycoingecko import CoinGeckoAPI
from cfonts import render, say
import time as t
import requests
import subprocess 
import random
from stem import Signal
from stem.control import Controller

ver = "PyBLOCK Micro v0.0.4"

faceshappy = {
    "SLEEP" : '(⇀‿‿↼)',
    "SLEEP2" : '(≖‿‿≖)',
    "AWAKE" : '(◕‿‿◕)',
    "INTENSE" : '(°▃▃°)',
    "COOL" : '(⌐■_■)',
    "HAPPY" : '(•‿‿•)',
    "GRATEFUL" : '(^‿‿^)',
    "EXCITED" : '(ᵔ◡◡ᵔ)',
    "MOTIVATED" : '(☼‿‿☼)',
    "SMART" : '(✜‿‿✜)',
    "FRIEND" : '(♥‿‿♥)'
    }

faceslookaround = {
    "LOOK_R" : '( ⚆_⚆)',
    "LOOK_L" : '(☉_☉ )',
    "LOOK_R_HAPPY" : '( ◕‿◕)',
    "LOOK_L_HAPPY" : '(◕‿◕ )'
    }

facessad = {
    "BORED" : '(-__-)',
    "DEMOTIVATED" : '(≖__≖)',
    "LONELY" : '(ب__ب)',
    "SAD" : '(╥☁╥ )',
    "ANGRY" : '(-_-)',
    "BROKEN" : '(☓‿‿☓)'
    }

def clear(): # clear the screen
    os.system('cls' if os.name=='nt' else 'clear')

#-----------------------------COINGECKO--------------------------------

def CoingeckoPP():
    btcInfo = CoinGeckoAPI()
    n = btcInfo.get_price(ids='bitcoin', vs_currencies='usd')
    q = n['bitcoin']
    usd = q['usd']
    output = render(str(usd), colors=['white', 'black'], align='center', font='simple')
    print("\a\x1b[?25l" + output)


#-----------------------------END COINGECKO--------------------------------

def blocks():
    try:
        clear()
        r = requests.get('https://mempool.space/api/blocks/tip/height')
        r.headers['Content-Type']
        n = r.text
        di = json.loads(n)
        a = di
        b = str(a)
        clear()
        pp = random.choice(list(faceslookaround.values())).encode('utf-8').decode('latin-1')
        output5 = subprocess.check_output(['sudo', 'iwgetid'])
        z = str(output5)
        print(ver + " ---> Connected to: " + z.split('"')[1] + " & Tor")
        print("BLOCK " + str(pp))
        output = render(str(b), colors=['white', 'black'], align='center', font='simple')
        print(output)
        print("PRICE")
        CoingeckoPP()
        while True:
            x = b
            r = requests.get('https://mempool.space/api/blocks/tip/height')
            r.headers['Content-Type']
            n = r.text
            di = json.loads(n)
            a = di
            if x < str(a):
                clear()
                output5 = subprocess.check_output(['sudo', 'iwgetid'])
                z = str(output5)
                pp = random.choice(list(faceshappy.values())).encode('utf-8').decode('latin-1')
                print(ver + " ---> Connected to: " + z.split('"')[1] + " & Tor")
                print("BLOCK " + str(pp))
                output = render(str(a), colors=['white', 'black'], align='center', font='simple')
                print(output)
                print("PRICE")
                CoingeckoPP()
                b = str(a) 
    except:
        pp = random.choice(list(facessad.values())).encode('utf-8').decode('latin-1')
        os.system("python3 clocks.py")
        print("Bad Connection... Restarting... " + str(pp))

while True:
    try:
        clear()
        with Controller.from_port(port = 9051) as controller:
            controller.authenticate(password='B4C0D10DB03D880260505745B66DA5595E5E98543990DF5404728B2927')    
            clear()
            print("Success!")
            controller.signal(Signal.NEWNYM)
            print("New Tor connection processed")
            t.sleep(3)
            r = requests.get('https://raw.githubusercontent.com/curly60e/pyblockmicro/main/ver.txt')
            r.headers['Content-Type']
            n = r.text
            di = json.loads(n)
            if di['version'] == ver:
                q = print(" ")
            else:
                gitfetch = "git fetch"
                gitchekcout = "git checkout origin/main -- .bashrc README.txt clocks.py clocksLOCAL.py papertty.service requirements.txt start.sh torrc "
                clear()
                b = os.popen(gitfetch).read()
                a = os.popen(gitchekcout).read()
                print(b)
                print(a)
                os.system("pip3 install -r requirements.txt")
                os.system("python3 clocks.py")
            print("Starting PyBLOCK Micro")
            pp = random.choice(list(faceslookaround.values())).encode('utf-8').decode('latin-1')
            print(pp)
            t.sleep(5)
        blocks()
    except:
        print("\n")
        sys.exit(101)
