# Codejam 2019, Round 1B: Manhattan Crepe Cart

from collections import namedtuple
import numpy as np

Person = namedtuple("Person", ["x", "y", "D"])


def find_cart(P, Q, persons):
    """Find crepe cart given a list of people."""
    xs = np.zeros(Q + 1)
    ys = np.zeros(Q + 1)

    for p in persons:
        if p.D == 'N':
            ys[p.y + 1:] += 1
        if p.D == 'S':
            ys[:p.y] += 1
        if p.D == 'W':
            xs[:p.x] += 1
        if p.D == 'E':
            xs[p.x + 1:] += 1

    return (np.argmax(xs), np.argmax(ys))


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    P, Q = map(int, input().split())

    persons = []
    for _ in range(P):
        x, y, D = input().split()
        persons.append(Person(int(x), int(y), D))

    cart = find_cart(P, Q, persons)
    print('Case #{}: {} {}'.format(case, *cart))
