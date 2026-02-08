flag = 0
f = open("hi.txt", "r", encoding="utf-8")
for line in f:
    line = line.strip()
    flag += line.count("ha")
f.close()
print(flag)
