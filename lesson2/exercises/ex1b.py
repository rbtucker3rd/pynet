from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

device1 = {
    "host": 'cisco4.lasthop.io',
    "username": 'pyclass',
    "password": password,
    "device_type": 'cisco_ios',
    "session_log": 'logs/my_session.txt',
}

net_connect = ConnectHandler(**device1)
print(net_connect.find_prompt())

# command = 'delete bootflash:/rob_test1.txt'
# net_connect.send_command(command, expect_string=r'confirm')
# net_connect.send_command('y', expect_string=r'#')

output = net_connect.send_command('ping', expect_string=r'ip', strip_prompt=False, strip_command=False)
output += net_connect.send_command('\n', expect_string=r'Target IP', strip_prompt=False, strip_command=False)
output += net_connect.send_command('8.8.8.8', expect_string=r'Repeat', strip_prompt=False, strip_command=False)
output += net_connect.send_command('\n', expect_string=r'Datagram', strip_prompt=False, strip_command=False)
output += net_connect.send_command('\n', expect_string=r'Timeout', strip_prompt=False, strip_command=False)
output += net_connect.send_command('\n', expect_string=r'Extended', strip_prompt=False, strip_command=False)
output += net_connect.send_command('\n', expect_string=r'Sweep', strip_prompt=False, strip_command=False)
output += net_connect.send_command('\n', expect_string=r'#', strip_prompt=False, strip_command=False)

print(output)

net_connect.disconnect()
