#!usr/bin/python3
# main.py

import argparse, sys
from configuration.config import configurationObject
from configuration.commandhandler import CommandHandlerObject



if __name__ == '__main__':
    configurationObject.load_animation()
    CommandHandlerObject.run()
