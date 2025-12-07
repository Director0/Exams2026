from itertools import *

s1 = "4 56 67 156 2467 2345 35".split()
s2 = "ca ab bf fe ec cd db dg ".split()

print(* range(1,9))

for p in permutations("abcdefg"):
    if all(str(p.index(x)+1) in s1[p.index(y)] for x , y in s2):
        print(*p)
