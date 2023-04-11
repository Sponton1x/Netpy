#! usr/bin/python3
import time
import sys

class NetpyConfig:
    VERSION = '1.0.0'
    DESCRIPTION = "The Network Python Package Tools"
    AUTHOR = "Sponton1x"
    WEBSITE = "https://xyz.sponton1x.repl.co"
    COPYRIGHT = "(c) 2023 Sponton1x"
    LICENSE = "CC BY-SA 4.0"


def load_animation():
    lowerstr = 'starting the netpy tool...'
    upperstr = lowerstr.upper()
    for x in range(len(lowerstr)):
         s = '\r' + lowerstr[0:x] + upperstr[x] + lowerstr[x+1:] + '\r'
         sys.stdout.write(s)
         sys.stdout.flush()
         time.sleep(0.1)
