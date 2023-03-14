def rightorder(x, y):
    if type(x) == int:
        if type(y) == int:
            if x<y: return True
            elif x>y: return False
            return None
        else:
            return rightorder([x], y)
    elif type(y) == int:
        return rightorder(x, [y])
    for m in range(min(len(x), len(y))):
        r = rightorder(x[m],y[m])
        if r == True: return True
        elif r == False: return False
    if len(x)<len(y): return True
    elif len(x)>len(y): return False
    return None

i, index, mysum = 0, 0, 0
for line in open('input13.txt'):
    line = line.strip()
    if line != "":
        if i%2 == 0:
            previous = eval(line)
        else:
            index +=1
            if rightorder(previous, eval(line)):
                mysum += index
        i += 1
print(mysum)