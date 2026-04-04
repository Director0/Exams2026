from ipaddress import *

ipn = ip_network("119.124.96.0/255.255.240.0", False)

print(len([x for x in ipn if f"{x:b}"[-1] == "0"]))