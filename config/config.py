#! usr/bin/python3
# config.py

import time
import sys
import os

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

def import_modules():
    module_dir = "modules"
    for filename in os.listdir(module_dir):
        if filename.endswith(".py"):
            module_name = filename[:-3]
            try:
                __import__(f"{module_dir}.{module_name}")
            except Exception as e:
                print(f"Error during loading modules >> {e}")
                sys.exit()
