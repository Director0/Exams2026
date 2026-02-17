from ipaddress import *

net = ip_network("112.160.0.0/255.240.0.0", False)
cnt = 0


for adr in net:
    binadr = f"{adr:b}"

    if binadr.count("1") % 5 == 0:
        cnt += 1

print(cnt)