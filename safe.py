#!/usr/bin/python3
import os
try:
    import requests
except ImportError:
    print('\n [âœ“] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [âœ“] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [âœ“] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as sarfrazssb
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;97m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo ="""

  \033[1;37;1m╭━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━╮
  \033[1;36;1m╰━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━╯
  
  \033[1;31;1m███    ███ ██████     ██████  ██ ████████ ██    ██ ██      
  \033[1;32;1m████  ████ ██   ██    ██   ██ ██    ██    ██    ██ ██      
  \033[1;33;1m██ ████ ██ ██████     ██████  ██    ██    ██    ██ ██      
  \033[1;34;1m██  ██  ██ ██   ██    ██   ██ ██    ██    ██    ██ ██      
  \033[1;35;1m██      ██ ██   ██ ██ ██████  ██    ██     ██████  ███████ 
  \033[1;92m╔════════════════════════════╗╔══════════════════════════╗
  \033[1;91;1m█ \033[1;37m [•] \033[1;31;1mTOOLS OWNER     \033[1;37m [•]  \033[1;32m║║ \033[1;37m [•] \033[1;31;1m BITUL AHMED \033[1;37m  [•]  \033[1;31m█ 
  \033[1;31;1m█ \033[1;37m [•] \033[1;32;1mFACEBOOK PAGE   \033[1;37m [•]\033[1;32m  ║║ \033[1;37m [•] \033[1;32m  MR. BITUL    \033[1;37m[•]  \033[1;31m█ 
  \033[1;31;1m█ \033[1;37m [•] \033[1;33;1mGITHUB USER     \033[1;37m [•]\033[1;32m  ║║ \033[1;37m [•] \033[1;33m  bitulvau     \033[1;37m[•]  \033[1;31m█ 
  \033[1;31;1m█ \033[1;37m [•] \033[1;34;1mWHATS APP NUMBER\033[1;37m [•]  \033[1;32m║║ \033[1;37m [•] \033[1;34m+8801903624823 \033[1;37m[•]  \033[1;31m█ 
  \033[1;31;1m█ \033[1;37m [•] \033[1;35;1mTOOLS VERTION   \033[1;37m [•]  \033[1;32m║║ \033[1;37m [•] \033[1;35m     1.0.0     \033[1;37m[•]  \033[1;31m█ 
  \033[1;31;1m█ \033[1;37m [•] \033[1;36;1mTOOLS STATUS    \033[1;37m [•] \033[1;32m ║║ \033[1;37m [•] \033[1;36m    FREE       \033[1;37m[•]  \033[1;31m█ 
  \033[1;31;1m█ \033[1;37m [•] \033[1;37;1mTOOLS NAME      \033[1;37m [•] \033[1;32m ║║ \033[1;37m [•] \033[1;37m  Encode Store \033[1;37m[•]  \033[1;31m█
  \033[1;92m╚════════════════════════════╝╚══════════════════════════╝          
  \033[1;36;1m╭━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━┳━━╮
  \033[1;37;1m╰━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━┻━━╯
""" 

def bitul():

    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print('───────────────────────────────────────────────────────────')
    print(' \033[33;1m[1] ENCODE MARSHAL Py3')
    print(' \033[32;1m[2] ENCODE EMOJI ')
    print(' \033[34;1m[3] Encode Lambda ')
    print(' \033[34;1m[4] Encode  ')
    print('\033[31;1m [E] EXIT ')
    print('───────────────────────────────────────────────────────────')
    print('')
    bitul_brand = input('\033[34;1m \033[92;1m[\033[91;1m●\033[92;1m] CHOOSE : ')
    if bitul_brand in ('1', '01'):
        os.system(' python Encode.py')
    if bitul_brand in ('2', '02'):
        os.system(' python Emoji-Enc.py')
    if bitul_brand in ('3', '03'):
        os.system(' python Lambda.py')
    if bitul_brand in ('4', '04'):
        os.system(' dpkg -i enc_1.0_aarch64.deb')
        os.system('enc')
    if bitul_brand in ('E', 'ee'):
        pass

bitul()
