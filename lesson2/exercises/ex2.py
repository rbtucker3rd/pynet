#!/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler
from datetime import datetime

nxos2 = {
    "device_type": "cisco_nxos",
    "host": "nxos2.lasthop.io",
    "username": "pyclass",
    "password": '88newclass',
    "session_log": 'logs/my_session.txt',
    "global_delay_factor": 2,
}

net_conn = ConnectHandler(**nxos2)
#print(net_conn.find_prompt())

cmd = "show lldp neighbors detail"

start_time = datetime.now()
output = net_conn.send_command(cmd)
end_time = datetime.now()
print("#" * 80)
print(output)
print("#" * 80)
print("\n\nExecution Time: {}".format(end_time - start_time))
print()

start_time = datetime.now()
output = net_conn.send_command(cmd, delay_factor=8)
end_time = datetime.now()
print("#" * 80)
print(output)
print("#" * 80)
print("\n\nExecution Time: {}".format(end_time - start_time))
print()

net_conn.disconnect()

