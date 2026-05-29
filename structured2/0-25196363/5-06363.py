
rs = []

for n in range(1, 1000):
    n1 = f"{n:o}"

    if n1[0] == "5":
        n1 = "11" +  n1.replace("2", "*").replace("1", "2").replace("*", "1")
    else:
        n1 = "2" + n1[1:] + "10"

    r = int(n1, 8)

    if r < 1354:
        rs.append((n, r))



print(sorted(rs, key=lambda x:x[1], reverse=True))