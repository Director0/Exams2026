from ipaddress import *

c = ip_network("191.128.66.83/255.192.0.0", strict=False)

print(c[-2])
