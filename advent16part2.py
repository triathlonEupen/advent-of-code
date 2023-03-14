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

def add_all(a, ls):
    res = []
    for elem in ls:
        res.append([elem[0]+[a],elem[1]])
        res.append([elem[0],elem[1]+[a]])
    return res

def find_combi(ls):
    if len(ls) == 1:
        return [[[ls[0]],[]]]
    else:
        rec = find_combi(ls[1:])
        return add_all(ls[0], rec)
mysplit = find_combi(tvalves[1:])
        
def dfs(ls): # depth-first search
    answer = 0
    queue = [(0, ['AA'], 0)]
    while queue:
        depth, path, pressure = queue.pop(0)
        for n in ls:
            if n not in path:
                current_dist = depth + dist[(path[-1],n)]
                if current_dist >= 25:
                    if pressure>answer: answer = pressure
                else: queue.insert(0,(current_dist+1, path+[n], pressure + trates[n] * (25-current_dist)))
    return answer

result = 0
for elem in mysplit:
    if len(elem[0])>6 and len(elem[1])>6:
        total = dfs(elem[0]) + dfs(elem[1])
        if total>result: result = total
    
print(result, 'Duration: {}'.format(datetime.now() - start_time))