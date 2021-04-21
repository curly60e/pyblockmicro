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
import pickle


ndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}

ver = "PyBLOCK Micro v0.0.2"

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

def rpc(method, params=[]):
    payload = json.dumps({
        "jsonrpc": "2.0",
        "id": "minebet",
        "method": method,
        "params": params
    })
    path = {"ip_port":"", "rpcuser":"", "rpcpass":"", "bitcoincli":""}
    if os.path.isfile('bclock.conf'): # Check if the file 'bclock.conf' is in the same folder
        pathv = pickle.load(open("bclock.conf", "rb")) # Load the file 'bclock.conf'
        path = pathv # Copy the variable pathv to 'path'
    return requests.post(path['ip_port'], auth=(path['rpcuser'], path['rpcpass']), data=payload).json()['result']

def remotegetblock():
    try:
        b = rpc('getblockcount')
        c = str(b)
        a = c
        clear()
        pp = random.choice(list(faceslookaround.values())).encode('utf-8').decode('latin-1')
        output5 = subprocess.check_output(['sudo', 'iwgetid'])
        z = str(output5)
        print(ver + " ---> Connected to SSID: " + z.split('"')[1] + " & Tor")
        print("BLOCK " + str(pp))
        output = render(str(c), colors=['white', 'black'], align='center', font='simple')
        print(output)
        print("PRICE")
        CoingeckoPP()
        while True:
            x = a
            b = rpc('getblockcount')
            c = str(b)
            if c > a:
                clear()
                output5 = subprocess.check_output(['sudo', 'iwgetid'])
                z = str(output5)
                pp = random.choice(list(faceshappy.values())).encode('utf-8').decode('latin-1')
                print(ver + " ---> Connected to SSID: " + z.split('"')[1] + " & Tor")
                print("BLOCK " + str(pp))
                output = render(str(c), colors=['white', 'black'], align='center', font='simple')
                print(output)
                print("PRICE")
                CoingeckoPP()
                t.sleep(15)
                a = c
                pp = random.choice(list(faceslookaround.values())).encode('utf-8').decode('latin-1')
                clear()
                print(ver + " ---> Connected to SSID: " + z.split('"')[1] + " & Tor")
                print("BLOCK " + str(pp))
                output = render(str(a), colors=['white', 'black'], align='center', font='simple')
                print(output)
                print("PRICE")
                CoingeckoPP()
    except:
        pp = random.choice(list(facessad.values())).encode('utf-8').decode('latin-1')
        os.system("python3 clocks.py")
        print("Bad Connection... Restarting... " + str(pp))

pp = random.choice(list(faceslookaround.values())).encode('utf-8').decode('latin-1')
print(pp)
t.sleep(5)

while True:
    try:
        clear()
        path = {"ip_port":"", "rpcuser":"", "rpcpass":""}

        if os.path.isfile('bclock.conf') or os.path.isfile('blnclock.conf'): # Check if the file 'bclock.conf' is in the same folder
            pathv = pickle.load(open("bclock.conf", "rb")) # Load the file 'bclock.conf'
            path = pathv # Copy the variable pathv to 'path'
        else:
            print("Welcome to PyBLOCK Micro\n\n")
            print("\n\tIf you are going to use your local node leave IP:PORT/USER/PASSWORD in blank.\n")
            path['ip_port'] = "http://{}".format(input("Insert IP:PORT to access your remote Bitcoin-Cli node: "))
            path['rpcuser'] = input("RPC User: ")
            path['rpcpass'] = input("RPC Password: ")
            pickle.dump(path, open("bclock.conf", "wb"))

        remotegetblock()
    except:
        print("\n")
        sys.exit(101)
