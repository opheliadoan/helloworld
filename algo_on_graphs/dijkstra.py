# Uses python3

import sys
import queue


def extractMin(H):
    min_pair = H.get()
    return min_pair[1]


def distance(adj, cost, s, t):
    # write your code here
    result = -1
    dist = [(sys.maxsize * 2 + 1) for _ in range(len(adj))]
    prev = [-1 for _ in range(len(adj))]
    dist[s] = 0
    H = queue.PriorityQueue(len(adj))
    for i in range(len(adj)):
        H.put((dist[i], i))
    while not H.empty():
        u = extractMin(H)
        j = 0
        for v in adj[u]:
            if dist[v] > dist[u] + cost[u][j]:
                dist[v] = dist[u] + cost[u][j]
                prev[v] = u
            j += 1
    if dist[t] != sys.maxsize * 2 + 1:
        result = dist[t]
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(
        zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))
    # distance(adj, cost, s, t)
