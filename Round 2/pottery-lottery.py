# Codejam 2019, Round 2: Pottery Lottery

import sys


def action(V, P):
    _ = int(input())
    print('{} {}'.format(V, P), flush=True)
    if P == 0:
        N, *tokens = map(int, input().split())
        return N


def solve_case(N, V):
    for i in range(N):
        action((i % V) + 1, 1)

    inspection = [action(i + 1, 0) for i in range(20)]
    candidate = 19 - inspection[::-1].index(min(inspection[V:]))

    for i in range(99 - 20 - N):
        non_candidates = [(i, n) for i, n in enumerate(inspection)
                          if i != candidate]
        rival = min(non_candidates, key=lambda x: x[1])[0]
        action(rival + 1, 1)
        inspection[rival] += 1

    action(candidate + 1, 100)


# I/O Code
num_cases = int(input())
for _ in range(num_cases):
    solve_case(60, 14)

sys.exit()
