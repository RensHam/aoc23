from functools import reduce

with open('input/input', 'r') as f:
    data = f.readlines()

print(
    sum(
        [
            game['blue'] * game['red'] * game['green'] for game in
            map(
                lambda line: reduce(
                    lambda max_s, cubes:
                    {
                        'blue': max(max_s['blue'], int(cubes.split(' ')[0])) if cubes.split(' ')[1] == 'blue' else max_s['blue'],
                        'red': max(max_s['red'], int(cubes.split(' ')[0])) if cubes.split(' ')[1] == 'red' else max_s['red'],
                        'green': max(max_s['green'], int(cubes.split(' ')[0])) if cubes.split(' ')[1] == 'green' else max_s['green'],
                    },
                    line,
                    {'blue': 0, 'red': 0, 'green': 0}
                ),
                [
                    line.strip().replace(';', ',').split(': ')[1].split(', ') for line in data
                ]
            )
        ]
    )
)
