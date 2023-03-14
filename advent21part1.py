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

print(rec('root'))