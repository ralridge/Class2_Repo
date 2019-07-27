#!/usr/bin/env/python

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

password = getpass()

def display_output(config_output):
    print()
    print("*" * 80)
    print("Config change: ")
    print(config_output)
    print("*" * 80)

#start_time = datetime.now()
nxos_1 = {"host": "nxos1.lasthop.io",
            "username": "pyclass",
            "password": password,
            "device_type": "cisco_nxos",
            #"fast_cli": True,
           }


nxos_2 = {"host": "nxos2.lasthop.io",
            "username": "pyclass",
            "password": password,
            "device_type": "cisco_nxos",
            #"fast_cli": True,
           }

nxos_devices = [nxos_1, nxos_2]

for device in nxos_devices:
    net_connect = ConnectHandler(**device)
    config_output = net_connect.send_config_from_file(config_file = 'vlan_list_ex5.txt')
    display_output(config_output)
    net_connect.disconnect()

#end_time = datetime.now()
#print("Total Execution time: {}\n".format(end_time - start_time))
