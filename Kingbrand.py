#coding=utf-8

import os, sys, platform

try:

    import requests

except:

    os.system('pip install requests')

import requests

if not os.path.isfile('King.so'):

    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/Kingbrand/nomi/King.cpython-310.so > King.so')

    os.system('clear')

if not os.path.isfile('brand.so'):

    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/Kingbrand/nomi/brand.cpython-310.so > brand.so')

    os.system('clear')

bit=platform.architecture()[0]

go = requests.get('https://raw.githubusercontent.com/SHOOTER-MAKER/KingBadshah/nomi/update.txt').text

if 'Juttbrand' in go:

    if bit == '64bit':

        from King import reg

        reg()

    elif bit == '32bit':

        from brand import reg

        reg()

else:

    os.system('rm -rf King.so brand.so')

    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/Kingbrand/nomi/King.cpython-310.so > King.so')

    os.system('curl -L https://raw.githubusercontent.com/SHOOTER-MAKER/Nomibrand/nomi/brand.cpython-310.so > brand.so')

    if bit == '64bit':

        from King import reg

        reg()

    elif bit == '32bit':

        from brand import reg

        reg()

