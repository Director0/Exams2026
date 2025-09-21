from ipaddress import *

net1 = ip_network(f"101.157.240.0/255.255.252.0")

bin_adr = [f"{ip1:b}" for ip1 in net1]
cnt = 0

for ip in bin_adr:
    if ip[0:16].count("1") > ip[16:].count("1"):
        cnt += 1

print(cnt)