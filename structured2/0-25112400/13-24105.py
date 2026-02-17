from ipaddress import *


n = ip_network("150.122.11.21/255.255.254.0", False)
print(f"{[x for x in n.hosts()][0]:b}".count("1"))

