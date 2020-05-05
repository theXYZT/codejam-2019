# Codejam 2019, Round 2: New Elements, Part 1

from math import gcd
import itertools


def solve(molecules):
    lines = set()
    for (c1, j1), (c2, j2) in itertools.combinations(molecules, 2):
        if (c1 < c2 and j1 > j2) or (c1 > c2 and j1 < j2):
            r, d = abs(c1 - c2), abs(j1 - j2)
            g = gcd(r, d)
            lines.add((r // g, d // g))
    return len(lines) + 1


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N = int(input())
    molecules = [tuple(map(int, input().split())) for _ in range(N)]

    num_orderings = solve(molecules)
    print('Case #{}: {}'.format(case, num_orderings))
