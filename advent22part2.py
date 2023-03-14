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
            if j == 149:
                newrow, newcol, newfacing = 149-i, 99, 2
            elif j == 99 and 50 <= i < 100:
                newrow, newcol, newfacing = 49, i+50, 3
            elif j == 99 and 100 <= i < 150:
                newrow, newcol, newfacing = 149-i, 149, 2
            elif j == 49 and 150 <= i < 200:
                newrow, newcol, newfacing = 149, i-100, 3
            else:
                newrow, newcol, newfacing = i, j+1, 0
        elif facing == 1:
            if i == 49 and j >= 100:
                newrow, newcol, newfacing = j-50, 99, 2
            elif i == 149 and j >= 50:
                newrow, newcol, newfacing = j+100, 49, 2
            elif i == 199:
                newrow, newcol, newfacing = 0, 100+j, 1
            else:
                newrow, newcol, newfacing = i+1, j, 1
        elif facing == 2:
            if j == 50 and i <= 49:
                newrow, newcol, newfacing = 149-i, 0, 0
            elif j == 50 and i <= 99:
                newrow, newcol, newfacing = 100, i-50, 1
            elif j == 0 and i <= 149:
                newrow, newcol, newfacing = 149-i, 50, 0
            elif j == 0:
                newrow, newcol, newfacing = 0, i-100, 1
            else:
                newrow, newcol, newfacing = i, j-1, 2
        else: # facing == 3
            if i == 0 and 50 <= j < 100:
                newrow, newcol, newfacing = j+100, 0, 0
            elif i == 0 and j >= 100:
                newrow, newcol, newfacing = 199, j-100, 3
            elif i == 100 and j < 50:
                newrow, newcol, newfacing = j+50, 50, 0
            else:
                newrow, newcol, newfacing = i-1, j, 3
        if grid[newrow][newcol] == "#":
            break
        i, j, facing = newrow, newcol, newfacing
    if y == "R": facing = (facing+1)%4
    elif y == "L": facing = (facing-1)%4

print(1000*(i+1) + 4*(j+1) + facing)