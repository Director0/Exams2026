from ipaddress import *

ipn = ip_network("87.226.26.72/255.255.255.252", False)

print(len([x for x in ipn if f"{x:b}".count("1") % 2 == 0]))