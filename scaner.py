# /usr/bin/python3

import socket
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-th', '--thost', type=str, required=True, help='enter a ip target to scan port')
parser.add_argument('-tp', '--tport', type=int, required=True, help='enter a port target to scan')

args = parser.parse_args()

def portScanner(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(5)
    if args.port in None:
        if s.connect_ex((host, for port in range(100))):
            print(f"{args.thost} tcp/ {str(args.tport)} is closed")
        else:
            print(f"{args.thost} tcp/ {str(args.tport)} is open")
    else:
        if s.connect_ex((host, port)):
            print(f"{args.thost} tcp/ {str(args.tport)} is closed")
        else:
            print(f"{args.thost} tcp/ {str(args.tport)} is open")


portScanner(args.thost, args.tport)