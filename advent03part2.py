answer = 0
with open('input03.txt') as f:
    x, first, second = 0, "", ""
    for line in f.readlines():
        current = line.strip()
        if x == 0:
            first = current
            x = 1
        elif x == 1:
            for element in current:
                if first.find(element) != -1:
                    second += element
            x = 2
        elif x == 2:
            for element in current:
                if second.find(element) != -1:
                    x = ord(element)-96
                    if x<0: x = x + 58
                    answer = answer + x
                    break
            second = ""
            x = 0
print(answer)