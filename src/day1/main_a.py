import re


def get_numbers(line):
    digits = re.findall(r'\d', line)
    return int(''.join([digits[0], digits[-1]]))


with open('input/input', 'r') as f:
    print(sum([get_numbers(line) for line in f.readlines()]))
