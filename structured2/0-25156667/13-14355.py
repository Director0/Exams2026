from ipaddress import *

for a in [int("00000000", 2), int("10000000", 2), int("11000000", 2), int("11100000", 2), int("11110000", 2), int("11111000", 2), int("11111100", 2), int("11111110", 2), int("11111111", 2)]:
    net = ip_network(f"127.63.67.1/255.255.{a}.0", False)

    if all(f"{adr:b}"[:16].count("1") >= f"{adr:b}"[16:].count("1") for adr in net):
        print(a)
