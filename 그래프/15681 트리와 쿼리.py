import sys

sys.setrecursionlimit(10 ** 8)
from collections import defaultdict

input = sys.stdin.readline


def recur(v):
    visited[v] = True

    for c in graph[v]:
        if visited[c]:
            continue
        count[v] += recur(c)

    return count[v]


N, R, Q = map(int, input().split())
graph = defaultdict(list)
for _ in range(N - 1):
    U, V = map(int, input().split())
    graph[U].append(V)
    graph[V].append(U)

count = [1] * (N + 1)
visited = [False] * (N + 1)
recur(R)
for _ in range(Q):
    print(count[int(input())])
