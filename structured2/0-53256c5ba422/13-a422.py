from ipaddress import *

for m in range(1, 32):
    net1 = ip_network(f"61.58.73.42/{m}", False)
    net2 = ip_network(f"61.58.75.135/{m}", False)

    if net1 == net2 and net1.network_address == net2.network_address:
        print(m)



net1 = ip_network(f"61.58.73.42/22", False)
cnt = 0

for adr in net1.hosts():
    binadr = f"{adr:b}"

    if binadr.count("1") % 2 != 0:
        cnt += 1


print(cnt)

