with open('input/input', 'r') as f:
    data = f.readlines()

print(
    sum(map(lambda x: 2**(x-1) if x else 0, [
        len(
            set(line.strip().split(':')[1].split(' | ')[0].split())
            .intersection(set(line.strip().split(':')[1].split(' | ')[1].split()))
        ) for line in data
    ]))
)