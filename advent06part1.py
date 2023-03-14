d = open("input06.txt").readline()
for i in range(3,len(d)):
    if (d[i]!=d[i-1]) and (d[i]!=d[i-2]) and (d[i]!=d[i-3]) and (d[i-1]!=d[i-2]) and (d[i-1]!=d[i-3]) and (d[i-2]!=d[i-3]):
        print(i+1)
        break