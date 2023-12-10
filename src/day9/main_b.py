import numpy

print(
    sum([
        round(
            numpy.polynomial.Polynomial.fit(
                list(range(len(numbers.split()))),
                list(map(int, numbers.split())),
                len(numbers.split()) - 1)(-1)
        )
        for numbers in open('input/input', 'r').readlines()
    ])
)
