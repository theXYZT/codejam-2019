# Codejam 2019, Round 1C: Bacterial Tactics

import itertools
from functools import lru_cache


def mex(s):
    for i in itertools.count():
        if i not in s:
            return i


@lru_cache(maxsize=None)
def nimber(state):
    s = set()
    for a, b in itertools.chain.from_iterable(legal_moves(state)):
        s.add(nimber(a) ^ nimber(b))
    return mex(s)


def legal_moves(state):
    h_moves, v_moves = [], []

    if len(state) == 0 or len(state[0]) == 0:
        return h_moves, v_moves

    R, C = len(state), len(state[0])

    move_rows = [r for r in range(R) if all(state[r])]
    move_cols = [c for c in range(C) if all([r[c] for r in state])]

    for h in move_rows:
        a = state[:h]
        b = state[h + 1:]
        h_moves.append([a, b])

    for v in move_cols:
        a = tuple(r[:v] for r in state)
        b = tuple(r[v + 1:] for r in state)
        v_moves.append([a, b])

    return h_moves, v_moves


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    R, C = map(int, input().split())
    board = tuple(tuple(c == '.' for c in input()) for i in range(R))

    winning_moves = 0
    h_moves, v_moves = legal_moves(board)
    for a, b in h_moves:
        if nimber(a) ^ nimber(b) == 0:
            winning_moves += C

    for a, b in v_moves:
        if nimber(a) ^ nimber(b) == 0:
            winning_moves += R

    print('Case #{}: {}'.format(case, winning_moves))
