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
    clear()
    r = requests.get('https://mempool.space/api/blocks/tip/height')
    r.headers['Content-Type']
    n = r.text
    di = json.loads(n)
    a = di
    b = str(a)
    clear()
    print(ver)
    print("BLOCK")
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
        if x != str(a):
            clear()
            print(ver)
            print("BLOCK")
            output = render(str(a), colors=['white', 'black'], align='center', font='simple')
            print(output)
            print("PRICE")
            CoingeckoPP()
            b = str(a)


#t.sleep(5)
while True:
    try:
        blocks()
    except:
        print("\n")
        sys.exit(101)
