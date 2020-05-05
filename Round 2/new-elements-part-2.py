# Codejam 2019, Round 2: New Elements, Part 2

from fractions import Fraction
from itertools import zip_longest
import math


def continued_fraction(a, b):
    """Get continued fraction representation of a/b."""
    q, r = a // b, a % b
    c = [q]
    while r:
        a, b = b, r
        q, r = a // b, a % b
        c.append(q)
    return c


def get_ratio(C):
    """Get a/b representation of a continued fraction."""
    a, b = 1, 0
    for x in reversed(C):
        a, b = b + a * x, a
    return a, b


def best_rational_between(lower, upper):
    L = continued_fraction(lower.numerator, lower.denominator)
    U = continued_fraction(upper.numerator, upper.denominator)

    for A in [L, L[:-1] + [L[-1] - 1, 1]]:
        for B in [U, U[:-1] + [U[-1] - 1, 1]]:
            R = []
            for a, b in zip_longest(A, B, fillvalue=math.inf):
                if a == b:
                    R.append(a)
                else:
                    R.append(min(a, b) + 1)
                    break

            m = Fraction(*get_ratio(R))
            if lower < m < upper:
                return m


def solve(molecules):
    lower, upper = Fraction(0), Fraction(10**9)
    for (c1, j1), (c2, j2) in zip(molecules, molecules[1:]):
        if c1 < c2 and j1 > j2:
            upper = min(upper, Fraction(c1 - c2, j2 - j1))
        elif c1 > c2 and j1 < j2:
            lower = max(lower, Fraction(c1 - c2, j2 - j1))
        elif c1 >= c2 and j1 >= j2:
            return 'IMPOSSIBLE'

    if lower >= upper:
        return 'IMPOSSIBLE'

    M = best_rational_between(lower, upper)
    wj, wc = M.numerator, M.denominator

    return "{} {}".format(wc, wj)


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N = int(input())
    molecules = [tuple(map(int, input().split())) for _ in range(N)]

    print('Case #{}: {}'.format(case, solve(molecules)))
