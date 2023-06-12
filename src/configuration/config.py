#!/usr/bin/python3
# config.py

import time, sys, os, json


current_year = int(time.strftime("%Y"))


class NetpyConfig:
    __version__ = '1.0.0'
    __description__ = "The Network Python Package Tools"
    __author__ = "Sponton1x"
    __website__ = "https://xyz.sponton1x.repl.co"
    __copyright__ = f"(c) {current_year} Sponton1x"
    __license__ = "CC BY-SA 4.0"
    __module_dir__ = "modules"
    __config_dir__ = "config"

    def load_animation(self):
        lowerstr = f'starting at {configurationObject.__version__}'
        upperstr = lowerstr.upper()
        for x in range(len(lowerstr)):
            s = '\r' + lowerstr[0:x] + upperstr[x] + lowerstr[x+1:] + '\r'
            sys.stdout.write(s)
            sys.stdout.flush()
            time.sleep(0.1)


    def import_modules(self):
        for filename in os.listdir(configurationObject.__module_dir__):
            if filename.endswith(".py"):
                module_name = filename[:-3]
                try:
                    __import__(f"{config.__module_dir__}.{module_name}")
                except Exception as e:
                    print(f"Error during loading modules >> {e}")
                    sys.exit()

    def generate_json(self, filename, results):
        json_data = []

        for result in results:
            port_data = {
                "port": result["port"],
                "status": "Open" if result["open"] else "Closed",
                "service": result["service"],
                "protocol": result["protocol"]}
            json_data.append(port_data)

        with open(filename, "w") as file:
            json.dump(json_data, file, indent=4)

# Write findOS function
# Write function to calculate checksum SHA512


configurationObject = NetpyConfig()
