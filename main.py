# main.py
# usr/bin/python3

import argparse, sys
from config.config import load_animation, import_modules
from config.args import create_parser

try:
    import_modules()
except Exception as e:
    print(f"Error while excuting function >> {e}")
    sys.exit()


if __name__ == '__main__':
    load_animation()
    parser = create_parser()
    args = parser.parse_args()
    args.func(args)
