from datetime import datetime
start_time = datetime.now()

tunnels = {}
tvalves = ['AA']
trates = {}
for line in open('input16.txt'):
    line = line.strip()
    valve = line.split()[1]
    rate = int(line.split('=')[1].split(';')[0])
    tunnels[valve] = line.split("to ")[1].split(" ", 1)[1].split(", ")
    if rate>0:
        tvalves.append(valve)
        trates[valve]=rate

def find_dist(i, j): # breath-first search
    visited={i}
    queue = [(0,i)]
    while queue:
        m = queue.pop(0)
        for n in tunnels[m[1]]:
            if n == j: return m[0]+1
            elif n not in visited:
                visited.add(n)
                queue.append((m[0]+1,n))
dist = {}
for i in tvalves:
    for j in tvalves:
        if i != j: dist[(i, j)] = find_dist(i, j)

def dfs(): # depth-first search
    answer = 0
    queue = [(0, ['AA'], 0)]
    while queue:
        depth, path, pressure = queue.pop(0)
        for n in tvalves:
            if n not in path:
                current_dist = depth + dist[(path[-1],n)]
                if current_dist >= 29:
                    if pressure>answer: answer = pressure
                else: queue.insert(0,(current_dist+1, path+[n], pressure + trates[n] * (29-current_dist)))
    return answer

print(dfs(), 'Duration: {}'.format(datetime.now() - start_time))