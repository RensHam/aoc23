import re

with open('input/input', 'r') as f:
    data = f.readlines()

parts_idx = [
    [char_idx for char_idx, char in enumerate(line.strip()) if not char.isdigit() and char != '.'] for line in data
]

print(
    sum(
        sum(
            [
                [
                    int(m.group()) for m in re.finditer(r'\d+', data[numbers_line_idx]) if (set(range(m.start(), m.end())).intersection(set(partial_numbers_idx)))
                ] for numbers_line_idx, partial_numbers_idx in enumerate([
                    [
                        char_idx for char_idx in numbers_in_line if (
                            {char_idx - 1, char_idx, char_idx + 1}.intersection(set(parts_idx[max(0, numbers_line_idx - 1)])) or
                            {char_idx - 1, char_idx, char_idx + 1}.intersection(set(parts_idx[min(len(parts_idx) - 1, numbers_line_idx + 1)])) or
                            {char_idx - 1, char_idx, char_idx + 1}.intersection(set(parts_idx[numbers_line_idx]))
                    )
                    ] for numbers_line_idx, numbers_in_line in enumerate([
                        [char_idx for char_idx, char in enumerate(line.strip()) if char.isdigit()] for line in data
                    ])
                ])
            ],
            []
        )
    )
)
