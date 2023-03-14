jets = open("input17.txt").readline()
rocks =[[(2, 4), (3, 4), (4, 4), (5, 4)],
        [(2, 5), (3, 4), (3, 5), (3, 6), (4, 5)],
        [(2, 4), (3, 4), (4, 4), (4, 5), (4, 6)],
        [(2, 4), (2, 5), (2, 6), (2, 7)],
        [(2, 4), (2, 5), (3, 4), (3, 5)]]

depth, jet, height = 0, 0, 0
rest_rocks = [{0}, {0}, {0}, {0}, {0}, {0}, {0}]
rock = rocks[0].copy()

while depth < 2023:
    if jets[jet] == '>':
        if all(rock[x][0]<6 and rock[x][1] not in rest_rocks[rock[x][0]+1] for x in range(len(rock))):
            for i in range(len(rock)):
                rock[i] = (rock[i][0]+1, rock[i][1])
    elif all(rock[x][0]>0 and rock[x][1] not in rest_rocks[rock[x][0]-1] for x in range(len(rock))):
        for i in range(len(rock)):
            rock[i] = (rock[i][0]-1, rock[i][1])
    if all(rock[x][1]-1 not in rest_rocks[rock[x][0]] for x in range(len(rock))):
        for i in range(len(rock)):
            rock[i] = (rock[i][0], rock[i][1]-1)
    else:
        for i in range(len(rock)):
            rest_rocks[rock[i][0]].add(rock[i][1])
            height = max(height, rock[i][1])
        depth += 1
        rock = rocks[depth%5].copy()
        for i in range(len(rock)):
            rock[i] = (rock[i][0], rock[i][1]+height)        
    jet = (jet+1)%len(jets)
print(height)