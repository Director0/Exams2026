from string import ascii_uppercase

for x in "0123456789" + ascii_uppercase[:11]:
        if all((int(f"32{y}{x}A", 21) + int(f"16{y}18", 21)) % 12 == 0 for y in "13579" + ascii_uppercase[1:11:2]):
            print(x,(int(f"327{x}A", 21) + int(f"16718", 21)) / 12)