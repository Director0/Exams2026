from ipaddress import *

ipn = ip_network("112.160.0.0/255.240.0.0", False)

print(len([ip for ip in ipn if f"{ip:b}".count("1") % 5 == 0]))