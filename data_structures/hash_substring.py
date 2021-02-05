# python3
import random


def read_input():
    return (input().rstrip(), input().rstrip())


def print_occurrences(output):
    print(' '.join(map(str, output)))


def PolyHash(S, p, x):
    hash = 0
    for i in reversed(S):
        hash = ((hash * x + ord(i)) % p + p) % p
    return hash


def precompute_hash(pattern, text, p, x):
    result = [None] * (len(text) - len(pattern) + 1)
    S = text[(len(text) - len(pattern)):len(text)]
    result[len(text) - len(pattern)] = PolyHash(S, p, x)

    y = 1
    for i in range(1, len(pattern) + 1):
        y = (y * x) % p
    for i in range(len(text) - len(pattern) - 1, -1, -1):
        result[i] = (x * result[i+1] + ord(text[i]) -
                     y * ord(text[i + len(pattern)])) % p

    return result


def get_occurrences(pattern, text):
    _prime = 1000000007
    x = random.randint(1, _prime - 1)
    result = []
    pHash = PolyHash(pattern, _prime, x)
    hashes = precompute_hash(pattern, text, _prime, x)
    for i in range(len(text) - len(pattern) + 1):

        if pHash != hashes[i]:
            continue
        if text[i:i + len(pattern)] == pattern:
            result.append(i)
    return result


if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
