# Codejam 2019, Round 1A: Alien Rhyme

from collections import defaultdict, Counter


def largest_subset_size(N, words):
    word_dict = defaultdict(Counter)
    for word in words:
        word_dict[len(word)][word] += 1

    max_length = max(len(word) for word in words)

    result = 0
    for length in range(max_length, 0, -1):
        for (suffix, count) in word_dict[length].items():
            if count >= 2:
                result += 2
                count -= 2
            if count:
                word_dict[length - 1][suffix[1:]] += count
    return result


# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    num_words = int(input())
    words = [input() for _ in range(num_words)]
    largest = largest_subset_size(num_words, words)
    print('Case #{}: {}'.format(case, largest))
