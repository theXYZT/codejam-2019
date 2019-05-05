# Codejam 2019, Qualification Round: You Can Go Your Own Way

def get_new_path(path):
	"""Returns diagonally flipped path."""
    return path.replace('S', 'e').replace('E', 's').swapcase()

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N = int(input())
    path = input()
    new_path = get_new_path(path)
    print('Case #{}: {}'.format(case, new_path))
