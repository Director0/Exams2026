for x in range(0, 23):
    n = (int(f"7{x}38596", 23) + int(f"14{x}36", 23) + int(f"61{x}7", 23))
    if n % 22 == 0:
        print(x, n // 22)