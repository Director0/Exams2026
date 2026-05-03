from ipaddress import *

ipn = ip_network("68.203.243.87/255.255.224.0", False)

print(ipn[-2])