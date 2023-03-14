import re

grid = []
readMore = True
for line in open('input22.txt'):
    if line == "\n": readMore = False
    if readMore: grid.append(line[:-1]) # remove the \n

i, j, facing = 0, 0, 0
while grid[i][j] != ".": j += 1

for x, y in re.findall(r"(\d+)([RL]?)", line): # line contains the instructions
    for _ in range(int(x)):
        if facing == 0:
            newrow, newcol = i, (j+1)%len(grid[i])
            while grid[newrow][newcol] == " ": newcol = (newcol+50)%len(grid[i])
        elif facing == 1:
            newrow, newcol = (i+1)%len(grid), j
            while newcol >= len(grid[newrow]) or grid[newrow][newcol] == " ": newrow = (newrow+50)%len(grid)
        elif facing == 2:
            newrow, newcol = i, (j-1)%len(grid[i])
            while grid[newrow][newcol] == " ": newcol = (newcol-50)%len(grid[i])
        else: # facing == 3
            newrow, newcol = (i-1)%len(grid), j
            while newcol >= len(grid[newrow]) or grid[newrow][newcol] == " ": newrow = (newrow-50)%len(grid)
        if grid[newrow][newcol] == "#":
            break
        i, j = newrow, newcol
    if y == "R": facing = (facing+1)%4
    elif y == "L": facing = (facing-1)%4

print(1000*(i+1) + 4*(j+1) + facing)