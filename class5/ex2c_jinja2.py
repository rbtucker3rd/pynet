from __future__ import unicode_literals, print_function
from jinja2 import FileSystemLoader, StrictUndefined
from jinja2.environment import Environment
from pprint import pprint

from netmiko import ConnectHandler
from getpass import getpass


env = Environment(undefined=StrictUndefined)
env.loader = FileSystemLoader("./template")

password = getpass()

template_vars = [
    {
        "host": "nxos1.lasthop.io",
        "intf1": "Ethernet1/4",
        "intf1_ip": "10.4.100.1",
        "intf1_mask": "24",
        "peer1_ip": "10.4.100.2",
    },
    {
        "host": "nxos2.lasthop.io",
        "intf1": "Ethernet1/4",
        "intf1_ip": "10.4.100.2",
        "intf1_mask": "24",
        "peer1_ip": "10.4.100.1",
    },
]

devices = [
    {
        "host": "nxos1.lasthop.io",
        "username": "pyclass",
        "password": password,
        "device_type": "cisco_nxos",
    },
    {
        "host": "nxos2.lasthop.io",
        "username": "pyclass",
        "password": password,
        "device_type": "cisco_nxos",
    },
]

for template_var in template_vars:
    template_file = 'nxos_template.j2'
    template = env.get_template(template_file)
    output = template.render(**template_var)   
    filename = 'files/'+template_var["host"]+'.txt'
    f=open(filename,"w+")
    f.write(output)
    f.close()
    print(output)

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

