from ipaddress import *

for m in range(31, 1, -1):
    ipn = ip_network(f"156.38.155.174/{m}", False)

    if len([x for x in ipn if f"{x:b}".count("1") == 12]) == 45:
        print(m)