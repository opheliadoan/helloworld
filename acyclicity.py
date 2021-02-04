# Uses python3

import sys


def dfs(v, adj, visited, onStack):
    visited[v] = 1
    onStack.append(v)
    for i in adj[v]:
        if not visited[i]:
            return dfs(i, adj, visited, onStack)
        elif (i in onStack):
            return 1
    onStack.clear()
    return 0


def acyclic(adj, n):
    result = 0
    visited = [0 for _ in range(n)]
    onStack = []
    for i in range(n):
        if not visited[i] and result == 0:
            if dfs(i, adj, visited, onStack):
                result = 1
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj, n))
