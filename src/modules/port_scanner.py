#! usr/bin/python3
# port_scanner.py

import socket, sys, json
import requests
from configuration.config import configurationObject
from other.parsing import parse_ports


class TcpScanner:

    def sendData(self, results):
        api_url = 'http://localhost:5000'
        headers = {"Content-Type": "application/json"}
        results_not_list = ' '.join(str(x) for x in results)
        response = requests.post(api_url, data=json.dumps(results_not_list), headers=headers)
        if response.status_code == 200:
            print('Data sent successfully')
        else:
            print('Failed to send data')

    def scan(self, target: str, ports: str, report):
        print(f'Scanning ports {ports} on {target}')
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)

        try:
            ports_list = parse_ports(ports)
        except Exception as e:
            print(f"Error while parsing ports >> {e}")
            return

        results = []


        for port in ports_list:
            try:
                result = sock.connect_ex((target, port))
            except Exception as e:
                print(f"Error >> {e}")
                return

            if result == 0:
                try:
                    service = socket.getservbyport(port)
                    print(f'Port {port} is open\nService is {service}')
                    results.append({"port": port, "open": True, "service": service, "protocol": "tcp"})
                except Exception as e:
                    print(f'The port {port} is open, but the service is unknown')
                    results.append({"port": port, "open": True, "service": "Unknown", "protocol": "tcp"})
            else:
                print(f'Port {port} is closed')
                results.append({"port": port, "open": False})

        sock.close()

        if report == 'On':
            configurationObject.generate_json("report.json", results)
            print("Report generated")

        self.sendData(results)
        return results

class UdpScanner:
    def scan(self, target, ports, report):
        # Implementation for UDP scanning
        pass
