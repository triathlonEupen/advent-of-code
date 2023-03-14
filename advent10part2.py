def myprint(X, cycle):
    if X-1 <= cycle%40 <= X+1: print(end='#')
    else: print(end='.')
    if cycle%40==39: print()

X, cycle = 1, 0
for line in open('input10.txt'):
    current = line.strip()
    if current == 'noop':
        myprint(X, cycle)
        cycle +=1
    else:
        amount = int(current.split()[1])
        myprint(X, cycle)
        cycle +=1
        myprint(X, cycle)
        cycle +=1
        X += amount