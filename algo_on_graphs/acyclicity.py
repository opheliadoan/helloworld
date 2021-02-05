# Uses python3

import sys


def dfs(v, adj, visited, onStack):
    visited[v] = 1
    onStack[v] = 1
    for i in adj[v]:
        if not visited[i] and dfs(i, adj, visited, onStack):
            return 1
        elif onStack[i]:
            return 1
    onStack[v] = 0
    return 0


def acyclic(adj):
    visited = [0 for _ in range(len(adj))]
    onStack = [0 for _ in range(len(adj))]
    for i in range(len(adj)):
        if not visited[i]:
            if dfs(i, adj, visited, onStack,):
                return 1
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
