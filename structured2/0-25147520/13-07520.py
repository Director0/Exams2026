from ipaddress import *

cnt = 0

for m in range(1, 32 + 1):
    net1 = ip_network(f"175.122.80.13/{m}", False)
    net2 = ip_network(f"175.122.80.0/{m}", False)


    print(m, net1.num_addresses)

print(cnt)