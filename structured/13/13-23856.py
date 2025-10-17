from ipaddress import *

huiminet = ip_network("172.95.116.174/255.255.192.0", False)

hub = []

for hui in huiminet:
    huib = f"{hui:b}"

    if huib.count("1") % 5 == 0:
        hub.append(hui)


print(min(hub))
