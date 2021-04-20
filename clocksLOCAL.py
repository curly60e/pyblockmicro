import base64, codecs, json, requests
import pickle
import os
import sys
import simplejson as json
from pycoingecko import CoinGeckoAPI
from cfonts import render, say
import time as t
import requests

ver = "PyBLOCK Micro v0.0.1"

ndconnectload = {"ip_port":"", "tls":"", "macaroon":"", "ln":""}
settingsClock = {"gradient":"", "design":"", "colorA":"", "colorB":""}


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
    b = rpc('getblockcount')
    c = str(b)
    a = c
    clear()
    print(ver)
    print("BLOCK")
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
            print(ver)
            print("BLOCK")
            output = render(str(c), colors=['white', 'black'], align='center', font='simple')
            print(output)
            print("PRICE")
            CoingeckoPP()
            a = c

t.sleep(5)
while True:
    try:
        remotegetblock()
    except:
        print("\n")
        sys.exit(101)
