# Codejam 2019, Round 1B: Draupnir

import sys

def get_initial_rings():
    """Find no. of initial rings using two hand-crafted queries."""
    Rs = [0, 0, 0, 0, 0, 0]

    print(200, flush=True)
    num_rings = int(input())
    Rs[5] = (num_rings % 2**40) // 2**33
    num_rings -= Rs[5] * (2**33)
    Rs[4] = (num_rings % 2**50) // 2**40
    num_rings -= Rs[4] * (2**40)
    Rs[3] = num_rings // 2**50

    print(56, flush=True)
    num_rings = int(input())
    num_rings -= Rs[3]*2**14 + Rs[4]*2**11 + Rs[5]*2**9
    Rs[2] = (num_rings % 2**28) // 2**18
    num_rings -= Rs[2] * (2**18)
    Rs[1] = (num_rings % 2**56) // 2**28
    num_rings -= Rs[1] * (2**28)
    Rs[0] = num_rings // 2**56

    return Rs

# I/O Code
num_cases, W = map(int, input().split())

for case in range(1, num_cases + 1):
    Rs = get_initial_rings()
    print(" ".join(map(str, Rs)), flush=True)

    if int(input()) < 0:
        sys.exit()

sys.exit()
