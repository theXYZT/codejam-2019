# Codejam 2019, Qualification Round: You Can Go Your Own Way

num_cases = int(input())

for case in range(1, num_cases + 1):
    N = int(input())
    path = input()
    new_path = path.translate(str.maketrans('SE', 'ES'))
    print('Case #{}: {}'.format(case, new_path))
