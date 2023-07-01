#! usr/bin/python3
# sniffer.py

import socket, os, sys


class Sniffer:
    def sniff(self, hostname: str):
        if os.name == "nt":
            socket_protocol = socket.IPPROTO_IP
        else:
            socket_protocol = socket.IPPROTO_ICMP

        try:
            sniffer = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket_protocol)
            sniffer.bind((hostname, 0))
            sniffer.setsockopt(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
        except Exception as e:
            print(f"Error: {e}")
            sys.exit()

        if os.name == "nt":
            try:
                sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
            except Exception as e:
                sys.exit()

        try:
            while True:
                raw_data, addr = sniffer.recvfrom(65535)
                print(f"Received packet from {addr[0]}")
                # Dodaj tutaj swoje operacje na odebranych pakietach
        except KeyboardInterrupt:
            print("Stopping...")
        finally:
            if os.name == "nt":
                try:
                    sniffer.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
                except Exception as e:
                    print(f"Error: {e}")
