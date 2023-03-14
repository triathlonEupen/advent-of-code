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
def bfs(queue, goal):
    while queue:
        depth, i, j = queue.pop(0)
        depth += 1
        if (i+1, j) == goal or (i-1, j) == goal:
            return depth
        for (x, y) in adjacents:
            if 0 <= i+x < ROW and 0 <= j+y < COL and (i+x, j+y) not in hb[depth%COL] and (i+x, j+y) not in vb[depth%ROW] and (depth, i+x, j+y) not in visited:
                visited.add((depth, i+x, j+y))
                queue.append((depth, i+x, j+y))

depth1 = bfs([(0, -1, 0)], (ROW, COL-1))
while (ROW-1, COL-1) in hb[(depth1+1)%COL]: depth1 += 1 # stay in place while door would be blocked by a blizzard
depth2 = bfs([(depth1, ROW, COL-1)], (-1, 0))
while (0, 0) in hb[(depth2+1)%COL]: depth2 += 1 # stay in place while door would be blocked by a blizzard
print(bfs([(depth2, -1, 0)], (ROW, COL-1)))