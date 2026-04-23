from ipaddress import *

ipn = ip_network("191.89.109.206/255.255.224.0", False)

print(ipn[-2])