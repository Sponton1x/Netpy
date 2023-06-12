#! usr/bin/python3
# parssing.py

def parse_ports(ports):
    ports_list = []
    for p in ports.split(','):
        if '-' in p:
            start, end = p.split('-')
            ports_list.extend(range(int(start), int(end)+1))
        else:
            ports_list.append(int(p))
    return ports_list
