# Uses python3

import sys
import queue


def color(adj):
    coloredGraph = [-1 for _ in range(len(adj))]
    coloredGraph[0] = 0
    Q = [0]
    while (len(Q) > 0):
        u = Q.pop(0)
        for v in adj[u]:
            if coloredGraph[v] == -1:
                coloredGraph[v] = 1 if coloredGraph[u] == 0 else 0
                Q.append(v)
    return coloredGraph


def bipartite(adj, edges):
    # write your code here
    # 0 for white, 1 for black
    coloredGraph = color(adj)
    for (a, b) in edges:
        if coloredGraph[a - 1] == coloredGraph[b - 1]:
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
    print(bipartite(adj, edges))
