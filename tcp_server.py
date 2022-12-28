# /usr/bin/python2

import socket
import threading
import argparse

parser = argparse.ArgumentParser()


# Add an argument
parser.add_argument('-bip', '--bind_ip', type=str, required=True, help='type a ip to start a tcp server')
parser.add_argument('-bp', '--bind_port', type=int, required=True, help='type an port to start tcp server')

# Parse the argument
args = parser.parse_args()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((args.bind_ip, args.bind_port))

server.listen(5)

print "[*] Listening on %s:%d" % (args.bind_ip, args.bind_port)

def handle_client(client_socket):
	request = client_socket.recv(1024)

	print "[*] Recived: %s" % request

	client_socket.send("ACK!")
	client_socket.close()

while True:
	client,addr = server.accept()
	print "[*] Accepted connection from: %s:%d" % (addr[0], addr[1])
	client_handler = threading.Thread(target=handle_client, args=(client,))
	client_handler.start()