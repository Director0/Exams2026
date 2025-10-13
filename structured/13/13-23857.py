from ipaddress import *

net = ip_network("192.168.12.207/255.192.0.0", False)
a = []

for hui in net:
    huib = f"{hui:b}"

    if huib.count("1") == huib.count("0"):
        a.append(hui)

print(a)
print(max(a))
# print(str(max(a)).replace(".", ""))