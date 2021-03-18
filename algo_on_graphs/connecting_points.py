# Uses python3
import sys
import math
import collections

ids = dict()


def make_set(vertice):
    ids[vertice] = vertice


def find(vertice):
    if ids[vertice] != vertice:
        ids[vertice] = find(ids[vertice])
    return ids[vertice]


def union(v1, v2):
    ids[find(v1)] = ids[find(v2)]


def distance(s, t):
    return math.sqrt((s[0] - t[0])**2 + (s[1] - t[1])**2)


def extractMin(H, cost):
    tmp = [cost[i] for i in H]
    u_index = tmp.index(min(tmp))
    u = H[u_index]
    H.remove(u)
    return u, H


def minimum_distance(x, y):
    result = 0
    # write your code here
    # compute distance between points using 2d array
    for i in range(len(x)):
        make_set(i)
    dist = {}
    for i, s in enumerate(list(zip(x, y))):
        for j, t in enumerate(list(zip(x, y))):
            if (i, j) in dist.keys() or (j, i) in dist.keys() or i == j:
                continue
            else:
                dist[(i, j)] = distance(s, t)

    # sort the edges by weight in non-decreasing order
    dist = collections.OrderedDict(
        sorted(dist.items(), key=lambda x: x[1]))

    for e in list(dist.keys()):
        if find(e[0]) != find(e[1]):
            dist.pop(e)
            union(e[0], e[1])
            result += distance((x[e[0]], y[e[0]]), (x[e[1]], y[e[1]]))
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))
