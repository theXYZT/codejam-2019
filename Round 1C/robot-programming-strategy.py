# Codejam 2019, Round 1C: Robot Programming Strategy

import itertools

def find_best_move(moves, robots):
    """Find best move given moves by opponent robots."""
    possible_moves = ['R', 'S', 'P']

    # Remove losing moves
    if 'R' in moves:
        possible_moves.remove('S')
    if 'S' in moves:
        possible_moves.remove('P')
    if 'P' in moves:
        possible_moves.remove('R')

    # Pick the move that wins instead of draws, eliminate losing robots
    for move in possible_moves:
        draws = [r for r, m in zip(robots, moves) if m == move]
        if len(draws) == len(robots):
            continue
        else:
            return move, draws

    return None, robots

def find_winning_strategy(A, robots):
    """Finds winning strategy defeating all robots, unless impossible."""
    strategy = ''
    while robots:
        opponent_moves = [r.__next__() for r in robots]
        move, robots = find_best_move(opponent_moves, robots)
        if move is None:
            return None
        else:
            strategy += move
    return strategy

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    A = int(input())
    robots = []
    for _ in range(A):
        robots.append(itertools.cycle(input()))

    strategy = find_winning_strategy(A, robots)
    if strategy is None:
        strategy = 'IMPOSSIBLE'
    print('Case #{}: {}'.format(case, strategy))
