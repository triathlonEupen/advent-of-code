d = open("input06.txt").readline()
for x in range(13, len(d)):
    if len(set(d[x - 14:x])) == 14:
        print(x)
        break