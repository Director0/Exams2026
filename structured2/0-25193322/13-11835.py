from ipaddress import *

cnt = 0

for a in range(1, 256):
    ipn = ip_network(f"207.0.{a}.167/255.255.255.192", False)

    if all(f"{x:b}"[:16].count("0") > f"{x:b}"[16:].count("0") for x in ipn):
        print(a)
        cnt += 1


print(f"cnt: {cnt}")