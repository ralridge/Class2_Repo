#!/usr/bin/env/python

from netmiko import ConnectHandler
from getpass import getpass
from pprint import pprint

password = getpass()

show_cmds = ['show version', 'show lldp neighbors']

cisco_4 = {"host": "cisco4.lasthop.io",
            "username": "pyclass",
            "password": password,
            "device_type": "cisco_ios",
           }


net_connect = ConnectHandler(**cisco_4)

print(net_connect.find_prompt())

print()

for cmd in show_cmds:
    show_output = net_connect.send_command(cmd, use_textfsm = True)
    print('*' * 80)
    print(cmd)
    print('*' * 80)
    pprint(show_output)
    print('*' * 80)
    print()
    
    if cmd == 'show lldp neighbors':
        print('LLDP Data Structure Type: {}'.format(type(show_output)))
        print('HPE Switch connection port: {}'.format(show_output[0]['neighbor_interface']))

print()
net_connect.disconnect()
