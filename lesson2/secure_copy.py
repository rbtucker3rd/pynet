#!/usr/bin/env python
from getpass import getpass
from netmiko import ConnectHandler, file_transfer

password = getpass()

nxos1 = {
    "device_type": "cisco_nxos",
    "host": "nxos1.lasthop.io",
    "username": "pyclass",
    "password": password,
    "session_log": 'logs/my_session.txt',
}

source_file = "test456.txt"
dest_file = "test456.txt"
direction = "get"
file_system = "bootflash:"

ssh_conn = ConnectHandler(**nxos1)
transfer_dict = file_transfer(
    ssh_conn,
    source_file=source_file,
    dest_file=dest_file,
    file_system=file_system,
    overwrite_file=True,
)

print(transfer_dict)