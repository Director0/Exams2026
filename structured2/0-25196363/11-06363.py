from math import *

for n in range(1, 16000):
    if ceil(ceil(log(n, 2)) * 123 / 8) * 65_536 >= 13.5 * 2**20:
        print(n)