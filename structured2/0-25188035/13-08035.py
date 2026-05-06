from ipaddress import *

ipn = ip_network("192.168.31.80/255.255.255.240", False)

print(max([f"{ip:b}".count("1") for ip in ipn]))