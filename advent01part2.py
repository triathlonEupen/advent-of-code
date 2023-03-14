mylist, current = [], 0
for line in open('input01.txt'):
    if line == '\n':
        mylist.append(current)
        current=0
    else:
        current = current+int(line.strip())
mylist.sort(reverse=True)
print(mylist[0]+mylist[1]+mylist[2]);