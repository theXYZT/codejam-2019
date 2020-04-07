# Codejam 2019, Qualification Round: Foregone Solution

num_cases = int(input())

for case in range(1, num_cases + 1):
    N = int(input())
    A = int(str(N).replace('4', '2'))
    print('Case #{}: {} {}'.format(case, A, N - A))
