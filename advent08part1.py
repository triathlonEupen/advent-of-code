mymap = [list(map(int, line)) for line in open('input08.txt').read().splitlines()]
x=len(mymap)
y=len(mymap[0])
visible = 0
for i in range(0,x):
    for j in range(0,y):
        if all(mymap[i][k] < mymap[i][j] for k in range(j)) or all(mymap[i][k] < mymap[i][j] for k in range(j + 1, y)) or all(mymap[k][j] < mymap[i][j] for k in range(i)) or all(mymap[k][j] < mymap[i][j] for k in range(i + 1, x)):
            visible += 1
print(visible)