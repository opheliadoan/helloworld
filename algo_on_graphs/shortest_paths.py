# Uses python3

import sys
import queue


def check_reachable(adj, s, li):
    for t in adj[s]:
        if li[t] == 0:
            li[t] = 1
            check_reachable(adj, t, li)
    return li


def relax(u, v, i, dist, prev):
    if dist[v] > dist[u] + cost[u][i]:
        dist[v] = dist[u] + cost[u][i]
        prev[v] = u
        return 1
    return 0


def shortet_paths(adj, cost, s, distance, reachable, shortest):

    reach_ = [0 for _ in range(len(adj))]
    reach_[s] = 1
    reach_ = check_reachable(adj, s, reach_)

    for i in range(len(reachable)):
        reachable[i] = reach_[i]

    dist = distance
    prev = [-1 for i in adj]

    dist[s] = 0

    for i in range(len(adj)):
        for n, item in enumerate(adj):
            for index, t in enumerate(item):
                r = relax(n, t, index, dist, prev)
                if r == 1 and i == len(adj) - 1:
                    reach_ = [0 for _ in range(len(adj))]
                    reach_ = check_reachable(adj, n, reach_)
                    shortest_ = [1-reach_[i] for i in range(len(adj))]
                    for i in range(len(shortest)):
                        shortest[i] = shortest_[i]


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
    s = data[0]
    s -= 1
    distance = [10**19] * n
    reachable = [0] * n
    shortest = [1] * n
    shortet_paths(adj, cost, s, distance, reachable, shortest)
    for x in range(n):
        if reachable[x] == 0:
            print('*')
        elif shortest[x] == 0:
            print('-')
        else:
            print(distance[x])
