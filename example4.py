#!/usr/bin/env/python

from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

password = getpass()

start_time = datetime.now()
cisco_3 = {"host": "cisco3.lasthop.io",
            "username": "pyclass",
            "password": password,
            "device_type": "cisco_ios",
            "fast_cli": True,
           }


net_connect = ConnectHandler(**cisco_3)

config_cmds = ['ip name-server 1.1.1.1', 'ip name-server 1.0.0.1', 'ip domain-lookup']
config_output = net_connect.send_config_set(config_cmds)
print()
print("*" * 80)
print("Config change: ")
print(config_output)
print("*" * 80)


ping_output = net_connect.send_command("ping google.com")
if "!!" in ping_output:
    print("Ping is successfull")
    print("\n\nPing output: {}\n\n".format(ping_output))
else:
    raise ValueError("\n\nPing failed: {}\n\n".format(ping_output))

net_connect.disconnect()


end_time = datetime.now()
print("Total Execution time: {}\n".format(end_time - start_time))
