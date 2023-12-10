import numpy

scoring = {
    'A': 'C', 'K': 'B', 'Q': 'A', 'T': '9', '9': '8', '8': '7', '7': '6', '6': '5', '5': '4', '4': '3', '3': '2', '2': '1', 'J': '0'
}

with open('input/input', 'r') as f:
    matches = [[line.split()[0], int(line.split()[1].strip())] for line in f.readlines()]

def get_match(match: str) -> int:
    m, c = numpy.unique(list(match), return_counts=True)
    if max(c) == 5:  # five of a kind
        return 0x600000
    i = 0
    count_sort_ind = numpy.argsort(-c)
    m = m[count_sort_ind]
    while 'J' in match:
        match = match.replace('J', m[i])
        i += 1
    c = numpy.unique(list(match), return_counts=True)[1]
    if max(c) == 5:  # five of a kind
        return 0x600000
    if max(c) == 4:  # four of a kind
        return 0x500000
    if max(c) == 3 and min(c) == 2:  # full house
        return 0x400000
    if max(c) == 3:
        return 0x300000
    if len(set(match)) == 4:  # One pair
        return 0x100000
    if max(c) == 1:  # High card
        return 0
    return 0x200000

print(sum([
    (rank+1) * match[1] for rank, match in enumerate(sorted(matches, key=lambda match: get_match(match[0]) + int(''.join(map(lambda m: scoring[m], match[0])), 16)))
]))
