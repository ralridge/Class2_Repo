#!/usr/bin/env/python

from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

extended_ping = 'ping'

cisco_r3 = {"host": "cisco3.lasthop.io",
            "username": "pyclass",
            "password": password,
            "device_type": "cisco_ios",
            "fast_cli": True,
}


net_connect = ConnectHandler(**cisco_r3)

print(net_connect.find_prompt())

ping_output = net_connect.send_command_timing(extended_ping,strip_command = False,strip_prompt = False)

ping_output += net_connect.send_command_timing('\n', strip_command = False, strip_prompt = False)

ping_output += net_connect.send_command_timing('8.8.8.8', strip_command = False, strip_prompt = False)


ping_output += net_connect.send_command_timing('\n', strip_command = False, strip_prompt = False)
ping_output += net_connect.send_command_timing('\n', strip_command = False, strip_prompt = False)
ping_output += net_connect.send_command_timing('\n', strip_command = False, strip_prompt = False)
ping_output += net_connect.send_command_timing('\n', strip_command = False, strip_prompt = False)
ping_output += net_connect.send_command_timing('\n', strip_command = False, strip_prompt = False)


print()
print(ping_output)
print()
net_connect.disconnect()
