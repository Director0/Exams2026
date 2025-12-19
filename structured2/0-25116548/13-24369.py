from ipaddress import *

net = ip_network("202.54.79.201/255.255.254.0", strict=False)

print(net[-2])