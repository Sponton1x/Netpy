#! usr/bin/python3
# monitor_traffic_network.py

from scapy.all import *

def packet_callback(packet):
    print(packet.summary())


def run(args):
    print(f"Starting scanning on interface {args.interface}...")
    try:
        sniff(iface=args.interface, prn=packet_callback)
    except Exception as e:
        print(f"Error: {e}")
