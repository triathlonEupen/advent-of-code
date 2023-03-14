mymax, current = 0, 0
for line in open('input01.txt'):
    if line == '\n':
        mymax = max(mymax, current)
        current=0
    else:
        current = current+int(line.strip())
print(mymax);