#! usr/bin/python3
# monitor_traffic_network.py

import argparse
from scapy.all import *


class MonitorTrafficNetwork():

    def packet_callback(self, packet):
        print(packet.summary())

    def monitor_traffic(self, interface: str):
        print(f"Starting scanning on interface {interface}...")
        try:
            sniff(iface=interface, prn=self.packet_callback)
        except Exception as e:
            print(f"Error: {e}")
