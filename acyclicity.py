# Uses python3

import sys


def dfs(v, adj, visited, onStack):
    visited[v] = True
    onStack[v] = True
    for i in adj[v]:
        if not visited[i]:
            return dfs(i, adj, visited, onStack)
        elif (onStack[i]):
            return True
    onStack[v] = False
    return False


def acyclic(adj, n):
    result = 0
    visited = [False for _ in range(n)]
    onStack = [False for _ in range(n)]
    edgeTo = [0 for _ in range(n)]
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
        adj[b - 1].append(a - 1)
    print(acyclic(adj, n))
