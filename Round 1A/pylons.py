# Codejam 2019, Round 1A: Pylons

import random


def generate_random_path(R, C):
    """Generates path randomly. Returns None if failed."""
    def valid_jump(a, b):
        """Returns True if jump from a to b is valid."""
        return (a[0] != b[0] and a[1] != b[1] and a[0] - a[1] != b[0] - b[1]
                and a[0] + a[1] != b[0] + b[1])

    # Generate randomly shuffled list of all cells
    cells = [(i, j) for i in range(1, R + 1) for j in range(1, C + 1)]
    random.shuffle(cells)

    # Pick random cells while there are valid jumps left.
    path = [
        cells.pop(),
    ]
    while cells:
        jumps = [
            i for i in range(len(cells)) if valid_jump(path[-1], cells[i])
        ]
        if jumps:
            path.append(cells.pop(random.choice(jumps)))
        else:
            return None
    return path


def find_path(R, C):
    """Find valid path on RxC grid if one exists."""
    invalid_configs = [(2, 2), (2, 3), (3, 2), (2, 4), (4, 2), (3, 3)]
    if (R, C) in invalid_configs:
        return None

    # If valid configuration, generate random paths
    # until a valid one is found, then return it.
    while True:
        path = generate_random_path(R, C)
        if path:
            return path


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    R, C = map(int, input().split())
    path = find_path(R, C)

    if path:
        print('Case #{}: POSSIBLE'.format(case))
        for c in path:
            print('{} {}'.format(c[0], c[1]))
    else:
        print('Case #{}: IMPOSSIBLE'.format(case))
