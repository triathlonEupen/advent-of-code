answer = 0
for line in open('input04.txt'):
    current = line.strip().split(",")
    left = current[0].split("-")
    right = current[1].split("-")
    a1 = int(left[0])
    a2 = int(left[1])
    b1 = int(right[0])
    b2 = int(right[1])
    if (a1<=b1 and a2>=b2) or (a1>=b1 and a2<=b2): answer = answer + 1
print(answer)