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

ping_output = net_connect.send_command(extended_ping, expect_string = r'Protocol', strip_command = False,strip_prompt = False)

ping_output += net_connect.send_command('\n', expect_string = r'Target IP', strip_command = False, strip_prompt = False)

ping_output += net_connect.send_command('8.8.8.8', expect_string = r'Repeat count', strip_command = False, strip_prompt = False)

ping_output += net_connect.send_command('\n', expect_string = r'Datagram size', strip_command = False, strip_prompt = False)

ping_output += net_connect.send_command('\n', expect_string = r'Timeout in seconds', strip_command = False, strip_prompt = False)

ping_output += net_connect.send_command('\n', expect_string = r'Extended commands', strip_command = False, strip_prompt = False)

ping_output += net_connect.send_command('\n', expect_string = r'Sweep range of sizes', strip_command = False, strip_prompt = False)

ping_output += net_connect.send_command('\n', expect_string = r'#', strip_command = False, strip_prompt = False)


print()
print(ping_output)
print()
net_connect.disconnect()
