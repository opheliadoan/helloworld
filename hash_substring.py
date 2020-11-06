# python3
import random


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def PolyHash(S, p, x):
    hash = 0
    for i in reversed(S):
        hash = (hash * x + ord(i)) % p
    return hash


def get_occurrences(pattern, text):
    _prime = 1000000007
    x = random.randint(1, _prime - 1)
    result = []
    pHash = PolyHash(pattern, _prime, x)
    for i in range(len(text) - len(pattern) + 1):
        tHash = PolyHash(text[i: i + len(pattern)], _prime, x)
        if pHash != tHash:
            continue
        if text[i:i + len(pattern)] == pattern:
            result.append(i)
    return result


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
