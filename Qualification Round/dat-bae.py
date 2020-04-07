# Codejam 2019, Qualification Round: Dat Bae

import sys

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N, B, F = map(int, input().split())
    F = B.bit_length() + 1

    # Silly way to generate worker queries
    worker_inputs = [
        format(i % 2**F, '#0{}b'.format(F + 2))[2:] for i in range(N)
    ]
    queries = ["".join([s[i] for s in worker_inputs]) for i in range(F)]

    # Save responses
    responses = []
    for q in queries:
        print(q, flush=True)
        responses.append(input())
    worker_outputs = ["".join([r[i] for r in responses]) for i in range(N - B)]

    # Iterate through responses in order to find broken workers
    broken = []
    for i, w in enumerate(worker_inputs):
        if worker_outputs and w == worker_outputs[0]:
            worker_outputs.pop(0)
        else:
            broken.append(i)
    print(*broken, flush=True)

    if int(input()) < 0:
        sys.exit()

sys.exit()
