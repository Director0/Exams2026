from ipaddress import *


for m in range(1, 32):
    ipn1 = ip_network(f"175.122.80.13/{m}", False)

    print(ipn1)

