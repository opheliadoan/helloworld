# Uses python3

import sys

reachability = 0


def reach(adj, visited, x, y):
    # write your code here
    global reachability
    visited[x] = True
    if y in adj[x]:
        reachability = 1
    for t in adj[x]:
        if not visited[t]:
            reach(adj, visited, t, y)
    return reachability


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    visited = [False for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, visited, x, y))
