import re

with open('input/input', 'r') as f:
    data = f.readlines()

parts_idx = [
    [char_idx for char_idx, char in enumerate(line.strip()) if char == '*'] for line in data
]

numbers_idx = [
    [char_idx for char_idx, char in enumerate(line.strip()) if char.isdigit()] for line in data
]

matching_gears = [
    [
        char_idx for char_idx in parts_in_line if (
            (
                (
                    {char_idx - 1}.intersection(set(numbers_idx[max(0, parts_line_idx - 1)]))
                ) and (
                    {char_idx + 1}.intersection(set(numbers_idx[max(0, parts_line_idx - 1)])) or
                    {char_idx - 1, char_idx, char_idx + 1}.intersection(set(numbers_idx[min(len(parts_idx) - 1, parts_line_idx + 1)])) or
                    {char_idx - 1, char_idx, char_idx + 1}.intersection(set(numbers_idx[parts_line_idx]))
                )
            )
            or
            (
                (
                    {char_idx}.intersection(set(numbers_idx[max(0, parts_line_idx - 1)]))
                ) and (
                    {char_idx - 1, char_idx, char_idx + 1}.intersection(set(numbers_idx[min(len(parts_idx) - 1, parts_line_idx + 1)])) or
                    {char_idx - 1, char_idx, char_idx + 1}.intersection(set(numbers_idx[parts_line_idx]))
                )
            )
            or
            (
                (
                    {char_idx + 1}.intersection(set(numbers_idx[max(0, parts_line_idx - 1)]))
                ) and (
                    {char_idx - 1}.intersection(set(numbers_idx[max(0, parts_line_idx - 1)])) or
                    {char_idx - 1, char_idx, char_idx + 1}.intersection(set(numbers_idx[min(len(parts_idx) - 1, parts_line_idx + 1)])) or
                    {char_idx - 1, char_idx, char_idx + 1}.intersection(set(numbers_idx[parts_line_idx]))
                )
            )
            or
            (
                (
                    {char_idx - 1}.intersection(set(numbers_idx[parts_line_idx]))
                ) and (
                    {char_idx + 1}.intersection(set(numbers_idx[parts_line_idx])) or
                    {char_idx - 1, char_idx, char_idx + 1}.intersection(set(numbers_idx[max(0, parts_line_idx - 1)])) or
                    {char_idx - 1, char_idx, char_idx + 1}.intersection(set(numbers_idx[min(len(parts_idx) - 1, parts_line_idx + 1)]))
                )
            )
            or
            (
                (
                    {char_idx + 1}.intersection(set(numbers_idx[parts_line_idx]))
                ) and (
                    {char_idx - 1}.intersection(set(numbers_idx[parts_line_idx])) or
                    {char_idx - 1, char_idx, char_idx + 1}.intersection(set(numbers_idx[max(0, parts_line_idx - 1)])) or
                    {char_idx - 1, char_idx, char_idx + 1}.intersection(set(numbers_idx[min(len(parts_idx) - 1, parts_line_idx + 1)]))
                )
            )
            or
            (
                (
                    {char_idx - 1}.intersection(set(numbers_idx[min(len(parts_idx) - 1, parts_line_idx + 1)]))
                ) and (
                    {char_idx + 1}.intersection(set(numbers_idx[min(len(parts_idx) - 1, parts_line_idx + 1)])) or
                    {char_idx - 1, char_idx, char_idx + 1}.intersection(set(numbers_idx[max(0, parts_line_idx - 1)])) or
                    {char_idx - 1, char_idx, char_idx + 1}.intersection(set(numbers_idx[parts_line_idx]))
                )
            )
            or
            (
                (
                    {char_idx}.intersection(set(numbers_idx[min(len(parts_idx) - 1, parts_line_idx + 1)]))
                ) and (
                    {char_idx - 1, char_idx, char_idx + 1}.intersection(set(numbers_idx[max(0, parts_line_idx - 1)])) or
                    {char_idx - 1, char_idx, char_idx + 1}.intersection(set(numbers_idx[parts_line_idx]))
                )
            )
            or
            (
                (
                    {char_idx + 1}.intersection(set(numbers_idx[min(len(parts_idx) - 1, parts_line_idx + 1)]))
                ) and (
                    {char_idx - 1}.intersection(set(numbers_idx[min(len(parts_idx) - 1, parts_line_idx + 1)])) or
                    {char_idx - 1, char_idx, char_idx + 1}.intersection(set(numbers_idx[max(0, parts_line_idx - 1)])) or
                    {char_idx - 1, char_idx, char_idx + 1}.intersection(set(numbers_idx[parts_line_idx]))
                )
            )
        )
    ] for parts_line_idx, parts_in_line in enumerate(parts_idx)
]

parts_partial_number = filter(None, [
    list(filter(None, [
        list(filter(None, [
            [
                [gear_line_idx, idx] for idx in [max(gear_idx - 1, 0), gear_idx, min(gear_idx+1, len(data) - 1)] if data[gear_line_idx][idx].isdigit()
            ] for gear_idx in gears_in_line
            for gear_line_idx in [max(gear_center_line_idx - 1, 0), gear_center_line_idx, min(gear_center_line_idx + 1, len(data) - 1)]
        ]))
    ])) for gear_center_line_idx, gears_in_line in enumerate(matching_gears)
])

parts_partial_number = list(parts_partial_number)

print(parts_partial_number)

numbers = []
for groups in parts_partial_number:
    for group in groups:
        print(group)
        for e in group:
            n = set()
            print(e)
            for g in e:
                print(g)
                n.add(next(int(m.group()) for m in re.finditer(r'\d+', data[g[0]]) if g[1] in range(m.start(), m.end())))
            print('n')
            print(n)
            numbers.append(n.pop() * n.pop())

print(sum(numbers))

