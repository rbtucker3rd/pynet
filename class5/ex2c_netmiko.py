from netmiko import ConnectHandler
from getpass import getpass

from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint

env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./template")

password = getpass()

devices = [
    {
        "host": "nxos1.lasthop.io",
        "username": "pyclass",
        "password": password,
        "device_type": "cisco_nxos",
        "intf1": "Ethernet1/1",
        "intf1_ip": "10.1.100.1",
        "intf1_mask": "24",
        "peer1_ip": "10.1.100.2",
    },
    {
        "host": "nxos2.lasthop.io",
        "username": "pyclass",
        "password": password,
        "device_type": "cisco_nxos",
        "intf1": "Ethernet1/1",
        "intf1_ip": "10.1.100.2",
        "intf1_mask": "24",
        "peer1_ip": "10.1.100.1",
    },
]

for device in devices:
    net_connect = ConnectHandler(**device)
    filename = "files/"+device["host"]+".txt"
    output = net_connect.send_config_from_file(filename)
    print()
    print("#" * 80)
    print("CFG Change: ")
    print(output)
    print("#" * 80)
    print()
    net_connect.save_config()
    net_connect.disconnect()

