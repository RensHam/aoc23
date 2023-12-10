import math

with open('input/input', 'r') as f:
    print(math.prod([
        1 + math.floor(-0.01 + 0.5 * (match[0] + pow((match[0] ** 2) - (4 * match[1]), 0.5))) - math.ceil(0.01 + 0.5 * (match[0] - pow((match[0] ** 2) - (4 * match[1]), 0.5)))
        for match in zip(*[map(int, line.strip().split(':')[1].split()) for line in f.readlines()])
    ]))