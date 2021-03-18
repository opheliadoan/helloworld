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


def clusterCount(x):
    return len(set([find(p) for p in range(len(x))]))


def extractMin(H, cost):
    tmp = [cost[i] for i in H]
    u_index = tmp.index(min(tmp))
    u = H[u_index]
    H.remove(u)
    return u, H


def clustering(x, y, k):
    # write your code here
    # disjoint set for each point
    for i in range(len(x)):
        make_set(i)

    dist = {}

    # compute distance between points and store in list of dict
    for i, s in enumerate(list(zip(x, y))):
        for j, t in enumerate(list(zip(x, y))):
            if (i, j) in dist.keys() or (j, i) in dist.keys() or i == j:
                continue
            else:
                dist[(i, j)] = distance(s, t)

    # sort the edges by weight in non-decreasing order
    dist = collections.OrderedDict(sorted(dist.items(), key=lambda x: x[1]))

    for e in list(dist.keys()):
        if find(e[0]) != find(e[1]):
            if clusterCount(x) > k:
                dist.pop(e)
                union(e[0], e[1])
        else:
            dist.pop(e)
    return (list(dist.items())[0][1])


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    data = data[1:]
    x = data[0:2 * n:2]
    y = data[1:2 * n:2]
    data = data[2 * n:]
    k = data[0]
    print("{0:.9f}".format(clustering(x, y, k)))
