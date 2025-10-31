from ipaddress import *


net = ip_network("23.78.143.87/255.255.240.0", strict=False)

for adr in net:
    binadr = f"{adr:b}"

    byt1 = binadr[:8]
    byt2 = binadr[8:16]
    byt3 = binadr[16:24]
    byt4 = binadr[24:32]
    print(binadr)
    print(byt1, byt2, byt3, byt4, sep="\n")