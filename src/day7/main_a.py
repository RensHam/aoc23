import numpy

scoring = {
    'A': 'C', 'K': 'B', 'Q': 'A', 'J': '9', 'T': '8', '9': '7', '8': '6', '7': '5', '6': '4', '5': '3', '4': '2', '3': '1', '2': '0'
}

with open('input/input', 'r') as f:
    matches = [[line.split()[0], int(line.split()[1].strip())] for line in f.readlines()]


def get_match(match: str) -> int:
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
    (rank+1) * match[1] for rank, match in enumerate(sorted(
        matches,
        key=lambda match: get_match(match[0]) + int(''.join(map(lambda m: scoring[m], match[0])), 16)
    ))
]))
