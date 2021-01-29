from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    # "global_delay_factor": 4,
    # 2 doubles, 2 = 4x, don't go hire than 10
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

output = net_connect.send_command("show ip int brief", delay_factor=4)
# output = net_connect.send_command("show ip int brief", delay_factor=10, max_loops=1000)
# if global_delay_factor and delay_factor are both used, highest number will be used

print(output)