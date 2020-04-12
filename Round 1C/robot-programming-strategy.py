# Codejam 2019, Round 1C: Robot Programming Strategy

import itertools

BEST_MOVE = {
    frozenset({'R'}): 'P',
    frozenset({'P'}): 'S',
    frozenset({'S'}): 'R',
    frozenset({'R', 'P'}): 'P',
    frozenset({'P', 'S'}): 'S',
    frozenset({'S', 'R'}): 'R',
    frozenset({'R', 'P', 'S'}): None,
}


def find_winning_strategy(robots):
    strategy = ''
    while robots:
        robot_moves = list(r.__next__() for r in robots)
        move = BEST_MOVE[frozenset(robot_moves)]
        if move is None:
            return None
        else:
            strategy += move
            robots = [r for r, m in zip(robots, robot_moves) if m == move]
    return strategy


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    A = int(input())
    robots = []
    for _ in range(A):
        robots.append(itertools.cycle(input()))

    strategy = find_winning_strategy(robots)
    if strategy is None:
        strategy = 'IMPOSSIBLE'
    print('Case #{}: {}'.format(case, strategy))
