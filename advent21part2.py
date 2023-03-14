monkeys = {}
for line in open('input21.txt'):
    monkey = line.strip().split()
    if len(monkey) == 2:
        monkeys[monkey[0][:-1]] = int(monkey[1])
    else:
        monkeys[monkey[0][:-1]] = monkey[1:]

def rec(monkey):
    yell = monkeys[monkey]
    if isinstance(yell, int):
        return yell
    else:
        rec1, rec2 = rec(yell[0]), rec(yell[2]) #@UnusedVariable rec1 and rec2 are actually used in eval
        return eval('rec1'+yell[1]+'rec2')

mymax = 10000000000000
mymin = -mymax

while(1):
    mid = (mymax+mymin)//2
    monkeys['humn'] = mid
    rec1, rec2 = rec(monkeys['root'][0]), rec(monkeys['root'][2])
    if rec1 == rec2:
        print(mid)
        break
    elif rec1 < rec2:
        mymax = mid
    else:
        mymin = mid