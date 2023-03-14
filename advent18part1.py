faces = {}
for line in open('input18.txt'):
    x, y, z = map(int, line.split(","))
    for dx, dy, dz in [(0, 0, 0.5), (0, 0.5, 0), (0.5, 0, 0), (0, 0, -0.5), (0, -0.5, 0), (-0.5, 0, 0)]:
        k = (x + dx, y + dy, z + dz)
        if k not in faces: faces[k] = 1
        else: faces[k] += 1
print(list(faces.values()).count(1))