from netmiko import ConnectHandler
from getpass import getpass

devices = [
    {
        "host": 'nxos1.lasthop.io',
        "username": 'pyclass',
        "password": '88newclass',
        "device_type": 'cisco_nxos',
        "session_log": 'logs/nxos1.txt',
    },
    {
        "host": 'nxos2.lasthop.io',
        "username": 'pyclass',
        "password": '88newclass',
        "device_type": 'cisco_nxos',
        "session_log": 'logs/nxos2.txt',
    }
]

for device in devices:
    net_connect = ConnectHandler(**device)
    # print(net_connect.find_prompt())
    # output = net_connect.send_command("show version")
    net_connect.send_command("show version")
    # print(output)

    
