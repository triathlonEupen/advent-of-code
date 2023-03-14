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

a,b = 1,2
for line in open('input13.txt'):
    line = line.strip()
    if line != "":
        c = eval(line)
        if rightorder(c,[[2]]): 
            a += 1
            b += 1
        elif rightorder(c,[[6]]): 
            b += 1
print(a*b)