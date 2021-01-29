from netmiko import ConnectHandler
from getpass import getpass

device1 = {
    "host": 'cisco3.lasthop.io',
    "username": 'pyclass',
    "password": getpass(),
    "device_type": 'cisco_ios',
    "session_log": 'logs/my_session.txt',
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

command = 'delete bootflash:/rob_test1.txt'
# net_connect.send_command(command, expect_string=r'confirm')
# net_connect.send_command('y', expect_string=r'#')

output = net_connect.send_command_timing(command,
    strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing('\n',
    strip_prompt=False, strip_command=False)
output += net_connect.send_command_timing('y',
    strip_prompt=False, strip_command=False)

print(output)
