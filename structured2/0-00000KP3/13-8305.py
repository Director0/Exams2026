from ipaddress import *

print(ip_network("42.172.106.203/255.255.252.0", False)[1])