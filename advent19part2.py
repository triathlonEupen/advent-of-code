from functools import lru_cache
from datetime import datetime
start_time = datetime.now()

b1_cost = [] # ore bot cost
b2_cost = [] # clay bot cost
b3_cost = [] # obsidians bot cost
b4_cost = [] # geode bot cost
for line in open('input19.txt'):
    blueprint = line.strip().split()
    b1_cost.append(int(blueprint[6]))
    b2_cost.append(int(blueprint[12]))
    b3_cost.append((int(blueprint[18]), int(blueprint[21])))
    b4_cost.append((int(blueprint[27]), int(blueprint[30])))

answer = 1
for bpID in range(3):

    print(bpID,end=' ')

    @lru_cache(maxsize=None)
    def rec(time, b1, b2, b3, b4, r1, r2, r3, r4):

        if time == 32: return b4+r4

        # always construct geode bot if there is enough ores and obsidians
        if r1 >= b4_cost[bpID][0] and r3 >= b4_cost[bpID][1]:
            return rec(time+1, b1, b2, b3, b4+1, r1+b1-b4_cost[bpID][0], r2+b2, r3+b3-b4_cost[bpID][1], r4+b4)

        # always construct obsidian bot if there is enough ores and clays
        if r1 >= b3_cost[bpID][0] and r2 >= b3_cost[bpID][1]:
            return rec(time+1, b1, b2, b3+1, b4, r1+b1-b3_cost[bpID][0], r2+b2-b3_cost[bpID][1], r3+b3, r4+b4)

        # maybe construct clay bot if there is enough ores
        current_max = 0
        if r1 >= b2_cost[bpID]:
            current_max = rec(time+1, b1, b2+1, b3, b4, r1+b1-b2_cost[bpID], r2+b2, r3+b3, r4+b4)

        # maybe construct ore bot if there is enough ores
        if r1 >= b1_cost[bpID]:
            current_max = max(current_max, rec(time+1, b1+1, b2, b3, b4, r1+b1-b1_cost[bpID], r2+b2, r3+b3, r4+b4))

        # maybe don't construct anything
        current_max = max(current_max, rec(time+1, b1, b2, b3, b4, r1+b1, r2+b2, r3+b3, r4+b4))

        return current_max

    answer *= rec(1, 1, 0, 0, 0, 0, 0, 0, 0)

print('\nAnswer=', answer, '\nDuration: {}'.format(datetime.now() - start_time))