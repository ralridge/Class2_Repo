#!/usr/bin/env/python

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

password = getpass()

lldp_nei = 'show lldp neighbors'

nxos_2 = {"host": "nxos2.lasthop.io",
            "username": "pyclass",
            "password": password,
            "device_type": "cisco_ios",
            "global_delay_factor": 2,
}


net_connect = ConnectHandler(**nxos_2)

print(net_connect.find_prompt())

start_time = datetime.now()
lldp_output = net_connect.send_command(lldp_nei,strip_command = False, strip_prompt = False)
end_time = datetime.now()

print("*" * 80)
print(lldp_output)
print("*" * 80)
print("\n\n Execution Time: {}".format(end_time - start_time))


start_time = datetime.now()
lldp_output = net_connect.send_command_timing(lldp_nei, strip_command = False, strip_prompt = False, delay_factor = 8)
net_connect.disconnect()
end_time = datetime.now()

print("*" * 80)
print(lldp_output)
print("*" * 80)
print("\n\n Execution Time: {}".format(end_time - start_time))
