from ipaddress import *

print(ip_network("241.0.0.0/255.255.255.128", False).num_addresses)