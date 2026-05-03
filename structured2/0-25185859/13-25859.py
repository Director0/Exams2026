from ipaddress import *

for a in range(1, 255):
    ipn = ip_network(f"248.112.{a}.35/255.255.255.240", False)

    if all(f"{ip:b}"[:16].count("0") <= f"{ip:b}"[16:].count("0") for ip in ipn):
        print(a)