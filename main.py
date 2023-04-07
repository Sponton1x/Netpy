# main.py
# usr/bin/python3

import argparse
from modules import port_scanner, ssh_brute, monitor_traffic_network, network_topology, sniffer

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="The Network Python Package Tools")

    subparsers = parser.add_subparsers(help='sub-command help')

    port_scan_parser = subparsers.add_parser('port-scan', help='port scanning help')
    port_scan_parser.add_argument('-t', '--target', type=str, required=True, help='Target IP address or hostname')
    port_scan_parser.add_argument('-p', '--ports', type=str, default='1-1024', help='Ports to scan (e.g. 22,80-100)')
    port_scan_parser.set_defaults(func=port_scanner.run)

    ssh_brute_parser = subparsers.add_parser('ssh-brute', help='SSH bruteforce help')
    ssh_brute_parser.add_argument('-ip', '--ip-address', type=str, required=True, help='target IP address')
    ssh_brute_parser.add_argument('-u', '--usernames', type=str, required=True, help='usernames to test')
    ssh_brute_parser.add_argument('-p', '--passwords', type=str, required=True, help='passwords to test')
    ssh_brute_parser.set_defaults(func=ssh_brute.run)

    monitor_parser = subparsers.add_parser('monitor', help="Simple monitor network traffic")
    monitor_parser.add_argument('-i', '--interface', type=str, required=True, help='Interface where program listiner')
    monitor_parser.set_defaults(func=monitor_traffic_network.run)

    network_scanner_parser = subparsers.add_parser('network-scanner', help='Simple network scanner topology.')
    network_scanner_parser.add_argument('-t', '--target', type=str, required=True, help='Target IP range to scan')
    network_scanner_parser.set_defaults(func=network_topology.run)

    sniffer_parser = subparsers.add_parser('sniffer', help='Simple sniffer')
    sniffer_parser.add_argument('-hn' , '--hostname', type=str, required=True, help='Host to sniff.')
    sniffer_parser.set_defaults(func=sniffer.run)

    args = parser.parse_args()

    args.func(args)
