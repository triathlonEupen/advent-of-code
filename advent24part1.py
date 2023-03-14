blizzards = set()
for i, line in enumerate(open('input24.txt')):
    for j, elem in enumerate(line[:-1]): # remove the \n
        if elem in ">v<^": blizzards.add((i-1, j-1, elem)) # -1 to work inside the valley
ROW, COL = i-1, j # amount of rows and columns inside the valley

hb, vb = [set() for _ in range(COL)], [set() for _ in range(ROW)] # horizontal/vertical blizzards
for x, y, facing in blizzards:
    if facing == ">":
        for k in range(COL): hb[k].add((x, (y+k)%COL))
    elif facing == "v":
        for k in range(ROW): vb[k].add(((x+k)%ROW, y))
    elif facing == "<":
        for k in range(COL): hb[k].add((x, (y-k)%COL))
    else:
        for k in range(ROW): vb[k].add(((x-k)%ROW, y))

# breath-first search algorithm
visited=set()
adjacents = [(0, 1), (1, 0), (-1, 0), (0, -1), (0, 0)]
queue = [(0, -1, 0)]
while queue:
    depth, i, j = queue.pop(0)
    depth += 1
    if (i+1, j) == (ROW, COL-1):
        print(depth)
        break
    for (x, y) in adjacents:
        if 0 <= i+x < ROW and 0 <= j+y < COL and (i+x, j+y) not in hb[depth%COL] and (i+x, j+y) not in vb[depth%ROW] and (depth, i+x, j+y) not in visited:
            visited.add((depth, i+x, j+y))
            queue.append((depth, i+x, j+y))