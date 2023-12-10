import math

with open('input/input', 'r') as f:
    directions = list(map(int, list(f.readline().strip().replace('R', '1').replace('L', '0'))))
    f.readline()
    mapping = {
        line.split(' = ')[0]: line.split(' = ')[1].strip().strip('()').split(', ')
        for line in f.readlines()
    }

locs = [loc for loc in list(mapping.keys()) if loc[2] == 'A']
distance = []
for loc in locs:
    i = 0
    while loc[2] != 'Z':
        loc = mapping[loc][directions[i % len(directions)]]
        i += 1
    distance.append(i)
print(math.lcm(*distance))