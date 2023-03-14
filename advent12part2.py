grid = [list(x) for x in open('input12.txt').read().strip().splitlines()]
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == 'S':
            grid[i][j] = 'a'
        elif grid[i][j] == 'E':
            goal = (i,j)

# breath-first search algorithm
visited=set()
queue = [(0,goal)]
while queue:
    depth, (i, j) = queue.pop(0)
    for (x, y) in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
        if (x, y) not in visited and 0 <= x < len(grid) and 0 <= y < len(grid[0]) and ord(grid[x][y])-ord(grid[i][j])>=-1:
            if grid[x][y] == 'a':
                print(depth+1)
                exit(0)
            visited.add((x, y))
            queue.append((depth+1, (x, y)))