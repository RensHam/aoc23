import re

with open('input/input', 'r') as f:
    data = f.readlines()

mapping = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}
gnippam = {
    'eno': '1',
    'owt': '2',
    'eerht': '3',
    'ruof': '4',
    'evif': '5',
    'xis': '6',
    'neves': '7',
    'thgie': '8',
    'enin': '9',
}

def get_numbers(line):
    chars = len(line)
    number = ''
    for i in range(chars):
        if line[i].isdigit():
            number = line[i]
        else:
            for match, digit in mapping.items():
                if line[i::].startswith(match):
                    number = digit
        if len(number):
            break
    line = line[::-1]
    for i in range(chars):
        if line[i].isdigit():
            number += line[i]
        else:
            for match, digit in gnippam.items():
                if line[i::].startswith(match):
                    number += digit
        if len(number) > 1:
            break
    return int(number)

print(sum([
    get_numbers(line)
    for line in data
]))