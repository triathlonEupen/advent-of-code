H, T = [0,0], [0,0]
myset={(0,0)}
for line in open('input09.txt'):
    direction,amount = line.strip().split()
    for x in range(0,int(amount)):
        if direction=='U':
            H[0]+=1
            if H[0]-T[0]==2:
                T[0]+=1
                if H[1]==T[1]+1:
                    T[1]+=1
                elif H[1]==T[1]-1:
                    T[1]-=1
                myset.add((T[0],T[1]))
        elif direction=='D':
            H[0]-=1
            if H[0]-T[0]==-2:
                T[0]-=1
                if H[1]==T[1]+1:
                    T[1]+=1
                elif H[1]==T[1]-1:
                    T[1]-=1
                myset.add((T[0],T[1]))
        elif direction=='L':
            H[1]+=1
            if H[1]-T[1]==2:
                T[1]+=1
                if H[0]==T[0]+1:
                    T[0]+=1
                elif H[0]==T[0]-1:
                    T[0]-=1
                myset.add((T[0],T[1]))
        elif direction=='R':
            H[1]-=1
            if H[1]-T[1]==-2:
                T[1]-=1
                if H[0]==T[0]+1:
                    T[0]+=1
                elif H[0]==T[0]-1:
                    T[0]-=1
                myset.add((T[0],T[1]))
print(len(myset))