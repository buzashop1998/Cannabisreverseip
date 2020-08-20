# -*- coding: utf-8 -*-
from itertools import cycle
import warnings,random,socket
import requests, re, sys, os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)
from time import time as timer  
import time
from colorama import init
from time import time as timer  
import time
init()
year = time.strftime("%y")
month = time.strftime("%m")
day = time.strftime("%d")
live = 0
proxy = ""

Headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_8; en-us) "
                      "AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50"
    }

def runit(ip):
    untile = 'https://api.hackertarget.com/reverseiplookup/?q='+ip
    print untile
    global live
    total = 0
    global proxy_cycle
    global proxy
    try:
      cepu = requests.get(untile, timeout=10, headers=Headers, proxies=proxy).text
      if 'error check your search parameter' in cepu:
        print '[!] '+ip + ' ====> Wrong List'
        open('broken_result.txt', 'a').write(ip + '\n')
      elif 'API count exceeded' in cepu:
        print '[!] '+ip + ' ====> Tryng Bypass With Proxy'
        soc = next(proxy_cycle)
        proxy = {"http":str(soc),"https":str(soc)}
        runit(ip)
      elif "Can't connect to api.hackertarget.com:443" in cepu:
        time.sleep(5)
        soc = next(proxy_cycle)
        proxy = {"http":str(soc),"https":str(soc)}
        runit(ip)
      elif "No DNS A records found" in cepu:
        print '[!] '+ip + ' ====> 0 Domain'
      else:
        resp = cepu.split('\n')
        for x in resp:
          open('rev_result.txt', 'a').write('http://' + x + '\n')

        print '[-] '+ip + ' ====> Get Grab site Available'
    except Exception as e:
      soc = next(proxy_cycle)
      proxy = {"http":str(soc),"https":str(soc)}
      runit(ip)

def prepare(sites):
    try:
      site = sites.strip()
      url = site.replace('http://', '').replace('https://', '').replace('/', '')
      ips = socket.gethostbyname(url)
      ip = ips + '\n'
      open('listip.txt', 'a')
      if ip not in open('listip.txt', 'r'):
        open('listip.txt', 'a').write(ips + '\n')
        runit(ips)
      else:
        print '[-] '+ip + ' ====> Same Ip'
    except Exception as e:
        print str(e)



def logo():
    clear = "\x1b[0m"

    x = """\033[1;32;40m
_________                         _     _     
\_   ___ \ __ _ _ __  _ __   __ _| |__ (_)___ 
/    \  \// _` | '_ \| '_ \ / _` | '_ \| / __|
\     \___ (_| | | | | | | | (_| | |_) | \__ \\
 \______  /__,_|_| |_|_| |_|\__,_|_.__/|_|___/
        \/ 
 \033[1;32;40mNot responsible for any illegal
 \033[1;32;40musage of this tool.\033[0;40m

 \033[1;30;40mAuthor   \033[1;40m: \033[1;33;40mICQ:https://icq.im/greatzcode
 \033[1;30;40mLink     \033[1;40m: \033[1;33;40mhttps://github.com/boters/Cannabis/
 \033[1;30;40mVersion  \033[1;40m: \033[1;33;40m0.1#First Edition
"""
    print x
    
logo()
Targetssa = raw_input("\033[1;33;40mInput Your List : \033[1;47m") #for date
aburamex = raw_input("\033[1;33;40mInput Your Proxy : \033[1;47m")

ip_list = open(Targetssa, 'r').read().split('\n')
aburame = open(aburamex).read()
hyuga = aburame.splitlines()
proxy_cycle = cycle(hyuga)

for sites in ip_list:
  prepare(sites)

