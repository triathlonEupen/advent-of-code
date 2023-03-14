sensors = []
beacons = []
dists = []
for line in open('input15.txt'):
    line = line.strip().split()
    sensors.append([int(line[2].split('=')[1].split(',')[0]), int(line[3].split('=')[1].split(':')[0])])
    beacons.append([int(line[8].split('=')[1].split(',')[0]), int(line[9].split('=')[1])])
for k,sensor in enumerate(sensors):
    dists.append(abs(sensor[0]-beacons[k][0]) + abs(sensor[1]-beacons[k][1]))

# since there is only one solution, it must be exactly at distance d+1 of at least one sensor
for k,sensor in enumerate(sensors):
    for i in range(-dists[k]-1,dists[k]+2):
        if 0 <= sensor[0]+i <= 4000000:
            d2 = dists[k]+1-abs(i)
            for j in (-d2, d2):
                if (0 <= sensor[1]+j <= 4000000
                    and all(abs(sensor[0]+i-sensors[a][0]) + abs(sensor[1]+j-sensors[a][1]) > dists[a] for a in range(len(dists)))):
                    print((sensor[0]+i)*4000000+sensor[1]+j)
                    exit(0)