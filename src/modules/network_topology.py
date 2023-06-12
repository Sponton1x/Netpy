#! /usr/bin/python3
# network_topology.py

import argparse, sys
from scapy.all import ARP, Ether, srp

class NetworkTopology:

    def scan_network(self, target):
        arp = ARP(pdst=target)
        ether = Ether(dst="ff:ff:ff:ff:ff:ff")
        packet = ether / arp

        result = srp(packet, timeout=3, verbose=0)[0]

        clients = []
        for sent, received in result:
            try:
                clients.append({'ip': received.psrc, 'mac': received.hwsrc})
            except Exception as e:
                print(f"Error: {e}")
                sys.exit()

        print("Scanning network...")
        print("IP\t\t\tMAC Address")
        print("-------------------------------------------")
        for client in clients:
            print(f"{client['ip']}\t\t{client['mac']}")
            print("-------------------------------------------")
