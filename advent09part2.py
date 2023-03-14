def mymove(p1,p2):
    if p1[0]-p2[0]==2:
        p2[0]+=1
        if p1[1]>=p2[1]+1:
            p2[1]+=1
        elif p1[1]<=p2[1]-1:
            p2[1]-=1
    elif p1[0]-p2[0]==-2:
        p2[0]-=1
        if p1[1]>=p2[1]+1:
            p2[1]+=1
        elif p1[1]<=p2[1]-1:
            p2[1]-=1
    elif p1[1]-p2[1]==2:
        p2[1]+=1
        if p1[0]>=p2[0]+1:
            p2[0]+=1
        elif p1[0]<=p2[0]-1:
            p2[0]-=1
    elif p1[1]-p2[1]==-2:
        p2[1]-=1
        if p1[0]>=p2[0]+1:
            p2[0]+=1
        elif p1[0]<=p2[0]-1:
            p2[0]-=1

H, T = [0,0], [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]]
myset={(0,0)}
for line in open('input09.txt'):
    direction,amount = line.strip().split()
    for x in range(0,int(amount)):
        if   direction=='U': H[0]+=1
        elif direction=='D': H[0]-=1
        elif direction=='L': H[1]+=1
        elif direction=='R': H[1]-=1
        mymove(H,T[0])
        for k in range(1,9):
            mymove(T[k-1],T[k])
        myset.add((T[8][0],T[8][1]))
print(len(myset))