myvar = [['G','J','Z'],
         ['C','V','F','W','P','R','L','Q'],
         ['R','G','L','C','M','P','F'],
         ['M','H','P','W','B','F','L'],
         ['Q','V','S','F','C','G'],
         ['L','T','Q','M','Z','J','H','W'],
         ['V','B','S','F','H'],
         ['S','Z','J','F'],
         ['T','B','H','F','P','D','C','M']]

for line in open('input05.txt'):
    current = line.strip().split()
    amount = int(current[1])
    orig = int(current[3])-1
    dest = int(current[5])-1
    for i in range(amount):
        myvar[dest].insert(0,myvar[orig][amount-i-1])
    for i in range(amount):
        del myvar[orig][0]
print(myvar)