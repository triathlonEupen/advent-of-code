X, cycle, S = 1, 0, 0
cycles = [20,60,100,140,180,220]
for line in open('input10.txt'):
    myline = line.strip()
    if myline == 'noop':
        cycle +=1
        if cycle in cycles: S += cycle*X
    else:
        amount = int(myline.split()[1])
        cycle +=1
        if cycle in cycles: S += cycle*X
        cycle +=1
        if cycle in cycles: S += cycle*X
        X += amount
print(S)