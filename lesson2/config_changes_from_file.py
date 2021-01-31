from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

device1 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    # "global_delay_factor": 2,
    #'fast_cli': True,
    # use fast_cli to speed up but at the sacrifice of reliability
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_config_from_file(config_file='config.txt')
print(output)

save_out = net_connect.save_config()
print(save_out)

net_connect.disconnect()
