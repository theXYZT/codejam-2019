# Codejam 2019, Round 1A: Golf Gophers

import sys


def get_num_gophers(blades, remainders, M):
    """Find no. of gophers given no. of blades and remainders."""
    for i in range(1, M + 1):
        congruences = all([i % b == r for b, r in zip(blades, remainders)])
        if congruences:
            return i
    return None


# I/O Code
num_cases, N, M = map(int, input().split())

for case in range(1, num_cases + 1):
    # 7 largest coprime integers < 18
    blades = [5, 7, 9, 11, 13, 16, 17]
    remainders = []
    for b in blades:
        query = " ".join(str(b) for _ in range(18))
        print(query, flush=True)
        r = sum(map(int, input().split())) % b
        remainders.append(r)

    G = get_num_gophers(blades, remainders, M)
    print(G, flush=True)

    if int(input()) < 0:
        sys.exit()

sys.exit()
