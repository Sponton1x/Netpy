#! usr/bin/python3
# port_scanner.py

import socket, sys

def run(args):
    print(f'Scanning ports {args.ports} on {args.target}...')
    try:
        ports_list = parse_ports(args.ports)
    except Exception as e:
        print(e)
        sys.exit()

    for port in ports_list:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        try:
            result = sock.connect_ex((args.target, port))
        except Exception as e:
            print(f"Error: {e}")
            sys.exit()
        if result == 0:
            print(f'Port {port} is open')
        else:
            print(f'Port {port} is closed')
            sock.close()

def parse_ports(ports):
    ports_list = []
    for p in ports.split(','):
        if '-' in p:
            start, end = p.split('-')
            ports_list.extend(range(int(start), int(end)+1))
        else:
            ports_list.append(int(p))
    return ports_list
