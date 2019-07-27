#!/usr/bin/env/python

from netmiko import ConnectHandler
from getpass import getpass


password = getpass()

show_intb = "show ip int brief"

cisco_r3 = {"host": "cisco3.lasthop.io",
            "username": "pyclass",
            "password": password,
            "device_type": "cisco_ios",
}


net_connect = ConnectHandler(**cisco_r3)

print(net_connect.find_prompt())

output = net_connect.send_command(show_intb, use_textfsm=True)

print(output)

show_intb_dict = output

net_connect.disconnect()
