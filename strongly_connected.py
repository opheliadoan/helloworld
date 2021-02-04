# Uses python3

import sys

counter = 1

sys.setrecursionlimit(200000)


def postorder(adj, pre, post, marked, v):
    global counter
    marked[v] = 1
    pre[v] = counter
    counter += 1
    for i in adj[v]:
        if not marked[i]:
            postorder(adj, pre, post, marked, i)
    post[v] = counter
    counter += 1


def reversed_graph(edges):
    reversed_adj = [[] for _ in range(n)]
    for (a, b) in edges:
        reversed_adj[b - 1].append(a - 1)
    return reversed_adj


def explore(adj, visited, v):
    visited[v] = 1
    for i in adj[v]:
        if not visited[i]:
            explore(adj, visited, i)


def number_of_strongly_connected_components(adj, n, edges):
    result = 0
    # write your code here
    pre = [0 for _ in range(n)]
    post = [0 for _ in range(n)]
    marked = [0 for _ in range(n)]
    visited = [0 for _ in range(n)]
    reversed_adj = reversed_graph(edges)
    for i in range(n):
        if not marked[i]:
            postorder(reversed_adj, pre, post, marked, i)
    desc_post = sorted(post, reverse=True)
    for p in desc_post:
        ind = post.index(p)
        if not visited[ind]:
            explore(adj, visited, ind)
            result += 1
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
    print(number_of_strongly_connected_components(adj, n, edges))
