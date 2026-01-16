from ipaddress import *

net = ip_network("208.192.226.58/255.240.0.0", False)

for adr in net.hosts():
    binadr = f"{adr:b}"

    if binadr.count("1") % 5 == 0:
        print(adr)