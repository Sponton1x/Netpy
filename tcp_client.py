# tcp_client.py
# /usr/bin/python2

import socket
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-th', '--thost', type=str, required=True, help='type a host to send a message')
parser.add_argument('-tp', '--tport', type=int, required=True, help='type a port to send a message')

args = parser.parse_args()

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((args.thost, args.tport))
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

response = client.recv(4096)

print response