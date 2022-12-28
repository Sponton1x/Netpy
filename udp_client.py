# /usr/bin/python2

# importing modules
import socket
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('-th', '--thost', type=str, required=True, help='type a host to send a message')
parser.add_argument('-tp', '--tport', type=int, required=True, help='type a port to send a message')

args = parser.parse_args()

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client.sendto("AAABBBCCC",(args.thost, args.tport))

# recive some data
data, addr = client.recvfrom(4096)

print data