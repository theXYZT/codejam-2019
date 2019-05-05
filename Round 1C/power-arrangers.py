# Codejam 2019, Round 1B: Power Arrangers

import sys
from collections import defaultdict

# I/O Code
num_cases, F = map(int, input().split())

for case in range(1, num_cases + 1):
    answer = ''
    indices = list(range(119))

    for position, num_sets in zip([1, 2, 3], [23, 5, 1]):
        memory = defaultdict(list)
        for i in indices:
            print(5*i + position, flush=True)
            memory[input()].append(i)
        for c in memory:
            if len(memory[c]) == num_sets:
                answer += c
                indices = memory[c][:]

    print(5*indices[0] + 4, flush=True)
    last_char = input()
    answer += (set('ABCDE') - set(answer + last_char)).pop()
    answer += last_char
    print(answer, flush=True)

    if input() == 'N':
        sys.exit()

sys.exit()
