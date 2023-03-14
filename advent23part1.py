elves = set()
for i, line in enumerate(open('input23.txt')):
    for j, elem in enumerate(line[:-1]): # remove the \n
        if elem == "#": elves.add((i, j))

directions = [[(-1,0),(-1,-1),(-1,1)], [(1,0),(1,-1),(1,1)], [(0,-1),(-1,-1),(1,-1)], [(0,1),(-1,1),(1,1)]]
adjacents = [(-1, 0), (-1, -1), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

for d in range(10):
    seen, blocked = {}, set()
    for (i, j) in elves:
        if any((i+x, j+y) in elves for (x, y) in adjacents):
            for nd in range(4):
                if all((i+x, j+y) not in elves for (x, y) in directions[(d+nd)%4]):
                    (ni, nj) = directions[(d+nd)%4][0]
                    new_pos = (i+ni, j+nj)
                    if new_pos in seen:
                        blocked.add(new_pos)
                    else:
                        seen[new_pos] = (i, j)
                    break
    for key in seen.keys():
        if not key in blocked:
            elves.remove(seen[key])
            elves.add(key)

xlist, ylist = list(x for (x, _) in elves), list(y for (_, y) in elves)
print((max(xlist)-min(xlist)+1)*(max(ylist)-min(ylist)+1)-len(elves))