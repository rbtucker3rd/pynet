from netmiko import ConnectHandler
from getpass import getpass


devices = [
    {
        "host": "nxos1.lasthop.io",
        "username": "pyclass",
        "password": '88newclass',
        "device_type": "cisco_nxos",
    },
    {
        "host": "nxos2.lasthop.io",
        "username": "pyclass",
        "password": '88newclass',
        "device_type": "cisco_nxos",
    },
]

for device in (devices):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_config_from_file("files/vlans.txt")
    print()
    print("#" * 80)
    print("CFG Change: ")
    print(output)
    print("#" * 80)
    print()
    net_connect.save_config()
    net_connect.disconnect()

