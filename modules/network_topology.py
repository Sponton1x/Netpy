# network_topology.py
# /usr/bin/python3

import argparse
from scapy.all import ARP, Ether, srp

def run(args):
    arp = ARP(pdst=args.target)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=3, verbose=0)[0]

    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})

    print("Scanning network...")
    print("IP\t\t\tMAC Address")
    print("-------------------------------------------")
    for client in clients:
        print(f"{client['ip']}\t\t{client['mac']}")
    print("-------------------------------------------")
