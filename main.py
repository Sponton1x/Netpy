# main.py
# usr/bin/python3

import argparse, sys
from config.config import config
from config.args import ParserObjClass

try:
    config.import_modules()
except Exception as e:
    print(f"Error while excuting function >> {e}")
    sys.exit()


if __name__ == '__main__':
    config.load_animation()
    parser = ParserObjClass.create_parser()
    args = parser.parse_args()
    args.func(args)
