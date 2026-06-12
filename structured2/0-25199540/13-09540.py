from ipaddress import *

ipn = [x for x in ip_network("156.132.15.138/255.255.252.0", False)]

print(ipn.index(IPv4Address("156.132.15.138")))