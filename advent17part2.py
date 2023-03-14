jets = open("input17.txt").readline()
rocks =[[(2, 4), (3, 4), (4, 4), (5, 4)],
        [(2, 5), (3, 4), (3, 5), (3, 6), (4, 5)],
        [(2, 4), (3, 4), (4, 4), (4, 5), (4, 6)],
        [(2, 4), (2, 5), (2, 6), (2, 7)],
        [(2, 4), (2, 5), (3, 4), (3, 5)]]

max_depth = 1000000000000
rest_rocks = [{0}, {0}, {0}, {0}, {0}, {0}, {0}]
rock = rocks[0].copy()

def process_all_jets(depth, height):
    global rock
    for jet in jets:
        if depth == max_depth:
            break
        if jet == '>':
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
    return depth, height

depth1, height1 = process_all_jets(0, 0)
depth2, height2 = process_all_jets(depth1, height1) # every further round would lead to the same depth and height increase
amount_rounds = (1000000000000-depth1) // (depth2 - depth1) # we can therefore calculate the amount of full rounds possible
depth3 = depth1 + amount_rounds * (depth2 - depth1) # we can compute the depth that would be reached after these rounds
height3 = height1 + amount_rounds * (height2 - height1) # we can compute the height that would be reached after these rounds
max_depth = depth2+(1000000000000-depth3) # simulate the only jet round that will not be processed fully
_, height4 = process_all_jets(depth2, height2) # since all rounds are the same, it's easier to simulate it in the 3rd round!
print(height3+(height4-height2)) # final result is height after all full rounds + height increase of 3rd round simulation!