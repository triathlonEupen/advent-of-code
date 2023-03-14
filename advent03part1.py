answer = 0
for line in open('input03.txt'):
    current = line.strip()
    mysize = int(len(current)/2)
    for element in current[:mysize]:
        if current[mysize:].find(element) != -1:
            x = ord(element)-96
            if x<0: x = x + 58
            answer = answer + x
            break
print(answer)