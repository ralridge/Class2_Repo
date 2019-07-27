#!/usr/bin/env/python

from netmiko import ConnectHandler
from getpass import getpass
import time

password = getpass()

cisco_r4 = {"host": "cisco4.lasthop.io",
            "username": "pyclass",
            "password": password,
            "secret": password,
            "device_type": "cisco_ios",
            "session_log": "example6_output.txt",
}


net_connect = ConnectHandler(**cisco_r4)

print("\nCurrent Prompt: ")
print(net_connect.find_prompt())
print("*" * 80)

print("\nEntering Config Mode: ")
net_connect.config_mode()
print(net_connect.find_prompt())
print("*" * 80)

print("\nExiting Config Mode: ")
net_connect.exit_config_mode()
print(net_connect.find_prompt())
print("*" * 80)

print("\nExiting Privileged Exec Mode: ")
net_connect.write_channel("disable\n")
time.sleep(2)
output = net_connect.read_channel()
print(output)
print("*" * 80)

print("\nRe-Entering Privileged Exec Mode: ")
net_connect.enable()
print(net_connect.find_prompt())

net_connect.disconnect()
