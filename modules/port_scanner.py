# port_scanner.py
# usr/bin/python3

import socket

def run(args):
    print(f'Scanning ports {args.ports} on {args.target}...')
    ports_list = parse_ports(args.ports)
    for port in ports_list:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((args.target, port))
            if result == 0:
                print(f'Port {port} is open')
            else:
                print(f'Port {port} is closed')
                sock.close()
        except KeyboardInterrupt:
            exit()
        except socker.error:
            print(f"\nCould not connect to port {port}")

def parse_ports(ports):
    ports_list = []
    for p in ports.split(','):
        if '-' in p:
            start, end = p.split('-')
            ports_list.extend(range(int(start), int(end)+1))
        else:
            ports_list.append(int(p))
    return ports_list
