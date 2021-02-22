# Uses python3

import sys
import queue


def setColor(adj, coloredGraph, s, c):
    coloredGraph[s] = c
    for i in adj[s]:
        if coloredGraph[i] == -1:
            setColor(adj, coloredGraph, i, 1 - c)
        else:
            if coloredGraph[i] == c:
                return 0
    return 1


def bipartite(adj):
    # write your code here
    # 0 for white, 1 for black
    coloredGraph = [-1 for _ in range(len(adj))]
    for i in range(len(adj)):
        if coloredGraph[i] == -1:
            if not setColor(adj, coloredGraph, i, 0):
                return 0
    return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(bipartite(adj))
