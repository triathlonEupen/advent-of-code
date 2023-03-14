mymap = [list(map(int, line)) for line in open('input08.txt').read().splitlines()]
x=len(mymap)
y=len(mymap[0])
maxscenic = 0
for i in range(0,x):
    for j in range(0,y):
        a = b = c = d = 0
        for k in range(i-1,-1,-1):
            a += 1
            if mymap[k][j] >= mymap[i][j]:
                break
        for k in range(i+1,x):
            b += 1
            if mymap[k][j] >= mymap[i][j]:
                break
        for k in range(j-1,-1,-1):
            c += 1
            if mymap[i][k] >= mymap[i][j]:
                break
        for k in range(j+1,y):
            d += 1
            if mymap[i][k] >= mymap[i][j]:
                break
        current = a*b*c*d
        if (current>maxscenic): maxscenic=current
print(maxscenic)

