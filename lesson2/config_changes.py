from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    "global_delay_factor": 2,
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

#cfg = 'logging buffered 20000'
cfg = [
    'logging buffered 20000',
    'no logging console',
    'clock timezone GMT 0 0'
]

output = net_connect.send_config_set(cfg)
print(output)

net_connect.disconnect()
