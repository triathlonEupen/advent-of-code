M, O, T = [[]], [], []
throw1, throw2 = [], []
for line in open('input11.txt'):
    line = line.strip().split()
    if len(line)==0: M.append([])
    elif line[0]=='Starting':
        for k in range(2,len(line)):
            M[len(M)-1].append(int(line[k].split(',')[0]))
    elif line[0]=='Operation:':
        O.append(eval("lambda old:"+line[3]+line[4]+line[5]))
    elif line[0]=='Test:':
        T.append(int(line[3]))
    elif line[1]=='true:':
        throw1.append(int(line[5]))
    elif line[1]=='false:':
        throw2.append(int(line[5]))

counts = [0] * len(M)
for _ in range(20):
    for i in range(len(M)):
        for j in range(len(M[i])):
            item = O[i](M[i][j])
            item //= 3
            if item%T[i]==0:
                M[throw1[i]].append(item)
            else: M[throw2[i]].append(item)
        counts[i] += len(M[i])
        M[i] = []
counts.sort(reverse=True)
print(counts[0]*counts[1])