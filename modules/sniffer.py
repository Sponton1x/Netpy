import socket
import os
import sys

def run(args):
    if os.name == "nt":
        socket_protocol = socket.IPPROTO_IP
    else:
        socket_protocol = socket.IPPROTO_ICMP
    try:
        sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
        sniffer.bind((args.hostname, 0))
        sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit()
    if os.name == "nt":
        try:
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
        except Exception as e:
            sys.exit()
    print(sniffer.recvfrom(65565))
    if os.name == "nt":
        try:
            sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
        except Exception as e:
            print(f"Error: {e}")
