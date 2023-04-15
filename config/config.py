#!/usr/bin/python3
# config.py

import time
import sys
import os


current_year = int(time.strftime("%Y"))


class NetpyConfig:
    __version__ = '1.0.0'
    __description__ = "The Network Python Package Tools"
    __author__ = "Sponton1x"
    __website__ = "https://xyz.sponton1x.repl.co"
    __copyright__ = f"(c) {current_year} Sponton1x"
    __license__ = "CC BY-SA 4.0"
    __module_dir__ = "modules"

    def load_animation(self):
        lowerstr = f'starting the netpy tool >> version >> {config.__version__}'
        upperstr = lowerstr.upper()
        for x in range(len(lowerstr)):
            s = '\r' + lowerstr[0:x] + upperstr[x] + lowerstr[x+1:] + '\r'
            sys.stdout.write(s)
            sys.stdout.flush()
            time.sleep(0.1)

    def import_modules(self):
        for filename in os.listdir(config.__module_dir__):
            if filename.endswith(".py"):
                module_name = filename[:-3]
                try:
                    __import__(f"{config.__module_dir__}.{module_name}")
                except Exception as e:
                    print(f"Error during loading modules >> {e}")
                    sys.exit()


config = NetpyConfig()
