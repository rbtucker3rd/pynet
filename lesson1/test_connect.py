from netmiko import ConnectHandler
from getpass import getpass

net_connect = ConnectHandler(
    host='cisco1.lasthop.io',
    username='pyclass',
    password=getpass(),
    device_type='cisco_ios',
    session_log='logs/my_session.txt',
)

print(net_connect.find_prompt())

