from ipaddress import *

n = ip_network("192.168.32.64/255.255.255.192", False)

print(len([x for x in n if f"{x:b}"[-3:] == "101"]))