# Codejam 2019, Qualification Round: Cryptopangrams

from math import gcd
import string

def single_pass(primes, cipher):
    """Goes through cipher solving for primes from left to right."""
    for i, p in enumerate(primes):
        if not p:
            if i == 0 and primes[i+1]:
                primes[i] = cipher[i+1] // primes[i+1]
            elif i == L - 2 and primes[i-1]:
                primes[i] = cipher[i] // primes[i-1]
            elif 0 < i < L - 2 and primes[i-1]:
                if primes[i-1]:
                    primes[i] = cipher[i] // primes[i-1]
    return primes

def decipher(cipher, N, L):
    """Deciphers given ciphertext."""
    primes = []
    found = False
    for a, b in zip(cipher, cipher[1:]):
        if a != b and not found:
            primes.append(gcd(a, b))
            found = True
        else:
            primes.append(None)

    # Forward pass if some primes are unsolved
    if None in primes:
        primes = single_pass(primes[:], cipher)

    # Backward pass if some primes are unsolved
    if None in primes:
        primes = single_pass(primes[::-1], cipher[::-1])[::-1]

    # Add in first and last primes
    primes.insert(0, cipher[0] // primes[0])
    primes.append(cipher[-1] // primes[-1])

    # Generate dictionary and return deciphered text
    dictionary = dict(zip(sorted(set(primes)), string.ascii_uppercase))
    return "".join([dictionary[i] for i in primes])

# I/O Code
num_cases = int(input())

for case in range(1, num_cases + 1):
    N, L = map(int, input().split())
    ciphertext = list(map(int, input().split()))
    plaintext = decipher(ciphertext, N, L)
    print('Case #{}: {}'.format(case, plaintext))
