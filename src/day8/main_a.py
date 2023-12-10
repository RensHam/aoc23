with open('input/input', 'r') as f:
    directions = list(map(int, list(f.readline().strip().replace('R', '1').replace('L', '0'))))
    f.readline()
    mapping = {
        line.split(' = ')[0]: line.split(' = ')[1].strip().strip('()').split(', ')
        for line in f.readlines()
    }

loc = 'AAA'
i = 0
while loc != 'ZZZ':
    loc = mapping[loc][directions[i % len(directions)]]
    i += 1
print(i)