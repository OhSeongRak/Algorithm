import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def dfs_start(v, route):
    global s_set

    for next in graph[v]:
        if next == T:
            s_set = s_set | route
            continue

        if next in visited:
            continue

        if next != S:
            visited.append(next)
        dfs_start(next, route | {next})

        if next in visited:
            visited.remove(next)

    return


def dfs_end(v, route):
    global t_set

    for next in graph[v]:
        if next == S:
            t_set = t_set | route
            continue

        if next in visited:
            continue

        if next != T:
            visited.append(next)
        dfs_end(next, route | {next})

        if next in visited:
            visited.remove(next)

    return


N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)

S, T = map(int, input().split())
s_set, t_set = set(), set()

visited = deque()
dfs_start(S, set())
# print(s_set)

visited = deque()
dfs_end(T, set())
# print(t_set)

print(len(s_set.intersection(t_set)))
