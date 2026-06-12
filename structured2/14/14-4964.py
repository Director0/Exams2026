for x in "0123456789ABCDEFGHIJK":
    if all((int(f"12{str(y)}{x}9", 21) + int(f"36{str(y)}99", 21)) % 18 == 0 for y in range(0, 100)):
        print(x, (int(f"125{x}9", 21) + int(f"36599", 21)) // 18)