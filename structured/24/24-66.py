s = open("24_66.txt").read()

# s = "KKКОТКОТКОТOKTKOKTTKOTOKOKOKOKTКОТКОТКОТTTTTКОТKKTTKKTKTOOKКОТКОТКОТКОТКОТOK"

s = s.replace("KOT", "*").replace("K", " ").replace("O", " ").replace("T", " ").split()

print(len(max(s, key=len)))