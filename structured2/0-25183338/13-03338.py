from ipaddress import *

ipn = ip_network("202.71.92.91/255.255.192.0", False)

ipp = [p for p in ipn if len([x for x in str(p).split(".") if int(x) % 2 != 0]) == 2]

print(ipp)