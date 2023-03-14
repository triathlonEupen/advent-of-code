sensors = []
beacons = []
blanks = set()
for line in open('input15.txt'):
    line = line.strip().split()
    sensors.append([int(line[2].split('=')[1].split(',')[0]), int(line[3].split('=')[1].split(':')[0])])
    beacons.append([int(line[8].split('=')[1].split(',')[0]), int(line[9].split('=')[1])])
for k,sensor in enumerate(sensors):
    d = abs(sensor[0]-beacons[k][0]) + abs(sensor[1]-beacons[k][1])
    d2 = d-abs(sensor[1]-2000000)
    for i in range(1,d2+1):
        blanks.add(sensor[0]-i)
        blanks.add(sensor[0]+i)

blanks.discard(-432198) # beacon x=-432198 y=2000000 should'nt be in the blank list
print(len(blanks))