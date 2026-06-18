from ipaddress import *

ips1 = [p for p in ip_network("202.71.92.91/255.255.192.0", False).hosts() if len([x for x in str(p).split(".") if int(x) % 2 != 0]) == 2][-1]


print(ips1)