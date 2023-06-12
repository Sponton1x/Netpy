#! usr/bin/python
# args.py

import argparse
from modules.port_scanner import TcpScanner
from modules.monitor_traffic_network import MonitorTrafficNetwork
from modules.sniffer import Sniffer
from modules.network_topology import NetworkTopology


class CommandHandler:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="The Network Python Package Tools")
        self.subparsers = self.parser.add_subparsers(help='sub-command help')

        self.commands = {
            'port-scan': self.add_port_scan_subcommand,
            'ssh-brute': self.add_ssh_brute_subcommand,
            'monitor': self.add_monitor_subcommand,
            'network-scanner': self.add_network_scanner_subcommand,
            'sniffer': self.add_sniffer_subcommand
        }

        for command, func in self.commands.items():
            func()

    def add_port_scan_subcommand(self):
        parser = self.subparsers.add_parser('port-scan', help='port scanning help')
        parser.add_argument('-t', '--target', type=str, required=True, help='Target IP address or hostname')
        parser.add_argument('-p', '--ports', type=str, default='1-1024', required=True, help='Ports to scan (e.g. 22,80-100)')
        parser.add_argument('-r', '--report', type=str, required=True, choices=['On', 'Off'])
        # */ TODO parser.add_argument('--scan-type', choices=['Tcp', 'Udp'])
        parser.set_defaults(func=self.handle_port_scan)

    def handle_port_scan(self, args):
        TcpScannerObject = TcpScanner()
        TcpScannerObject.scan(args.target, args.ports, args.report)

    def add_ssh_brute_subcommand(self):
        parser = self.subparsers.add_parser('ssh-brute', help='SSH bruteforce help')
        parser.add_argument('-ip', '--ip-address', type=str, required=True, help='target IP address')
        parser.add_argument('-u', '--usernames', type=str, required=True, help='usernames to test')
        parser.add_argument('-p', '--passwords', type=str, required=True, help='passwords to test')
        parser.set_defaults(func=self.handle_ssh_brute)

    def handle_ssh_brute(self, args):
        brute = SshBrute()
        brute.brute_force(args.ip_address, args.usernames, args.passwords)

    def add_monitor_subcommand(self):
        parser = self.subparsers.add_parser('monitor', help="Simple monitor network traffic")
        parser.add_argument('-i', '--interface', type=str, required=True, help='Interface where program listens')
        parser.set_defaults(func=self.handle_monitor)

    def handle_monitor(self, args):
        monitor = MonitorTrafficNetwork()
        monitor.monitor_traffic(args.interface)

    def add_network_scanner_subcommand(self):
        parser = self.subparsers.add_parser('network-scanner', help='Simple network scanner topology.')
        parser.add_argument('-t', '--target', type=str, required=True, help='Target IP range to scan')
        parser.set_defaults(func=self.handle_network_scanner)

    def handle_network_scanner(self, args):
        scanner = NetworkTopology()
        scanner.scan_network(args.target)

    def add_sniffer_subcommand(self):
        parser = self.subparsers.add_parser('sniffer', help='Simple sniffer')
        parser.add_argument('-hn', '--hostname', type=str, required=True, help='Host to sniff')
        parser.set_defaults(func=self.handle_sniffer)

    def handle_sniffer(self, args):
        sniffer = Sniffer()
        sniffer.sniff(args.hostname)

    def run(self):
        args = self.parser.parse_args()
        if hasattr(args, 'func'):
            args.func(args)
        else:
            self.parser.print_help()

CommandHandlerObject = CommandHandler()
