rocks = set()
depth = 0
for line in open('input14.txt'):
    line = line.strip().split('->')
    prev = None
    for elem in line:
        p = list(map(int, elem.split(",")))
        if prev != None:
            a1 = min(prev[0],p[0])
            b1 = min(prev[1],p[1])
            a2 = max(prev[0],p[0])
            b2 = max(prev[1],p[1])
            depth = max(depth, b2)
            for i in range(a1,a2+1):
                for j in range(b1,b2+1):
                    rocks.add((i,j))
        prev = p

depth += 1
sand = 0
while (500,0) not in rocks:
    x,y = 500,0
    while True:
        if y == depth:
            rocks.add((x,y))
            sand += 1
            break
        elif (x,y+1) not in rocks:
            y += 1
        elif (x-1,y+1) not in rocks:
            x -= 1
            y += 1
        elif (x+1,y+1) not in rocks:
            x += 1
            y += 1
        else:
            rocks.add((x,y))
            sand += 1
            break
print(sand)