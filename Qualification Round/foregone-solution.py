# Codejam 2019, Qualification: Foregone Solution

def split_number(N):
    A = int(str(N).replace('4', '2'))
    return A, N - A

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N = int(input())
    A, B = split_number(N)
    print('Case #{}: {} {}'.format(case, A, B))
