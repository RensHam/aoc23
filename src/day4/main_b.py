import itertools
from functools import reduce

# 9425061

with open('input/input', 'r') as f:
    data = f.readlines()

cards = list(itertools.repeat(1, len(data)))

wins = [
    len(
        set(line.replace('  ', ' ').strip().split(':')[1].split(' | ')[0].split(' '))
        .intersection(set(line.replace('  ', ' ').strip().split(':')[1].split(' | ')[1].split(' ')))
    ) for line in data
]

for idx, win in enumerate(wins):
    for i in range(idx + 1, idx+win+1):
        cards[i] += cards[idx]

print(sum(cards))