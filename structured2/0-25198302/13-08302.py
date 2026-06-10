from ipaddress import *

cnt = 0
ls = []

for m in range(1, 32):
    net1 = ip_network(f"115.53.128.88/{m}", False)
    net2 = ip_network(f"115.53.128.0/{m}", False)

    if net1 == net2 and net1.network_address == net2.network_address and net2.num_addresses >= 1000:
        ls.append("1" * m + "0" * (32-m))
        cnt += 1


for i in range(len(ls)):
    ls[i] = ls[i][16:24]

print(set(ls))
print(len(set(ls)))