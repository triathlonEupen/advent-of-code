cubes = []
for line in open('input18.txt'):
    cubes.append(tuple(map(int, line.split(","))))

water = set()
queue = [(0, 0, 0)]
while queue:
    wx, wy, wz = queue.pop()
    if (wx, wy, wz) in water or (wx, wy, wz) in cubes:
        continue
    water.add((wx, wy, wz))
    for dx,dy,dz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
        if 0 <= wx+dx <= 22 and 0 <= wy+dy <= 22 and 0 <= wz+dz <= 22: queue.append((wx+dx, wy+dy, wz+dz))

answer = 0
for x,y,z in cubes:
    for dx,dy,dz in [(-1,0,0),(1,0,0),(0,-1,0),(0,1,0),(0,0,-1),(0,0,1)]:
        if (x+dx,y+dy,z+dz) in water: answer += 1
print(answer)