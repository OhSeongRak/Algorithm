import sys
from collections import defaultdict
from heapq import heappop, heappush

input = sys.stdin.readline


def dijkstra():
    INF = sys.maxsize
    distance = [INF] * (N + 1)
    queue = [(0, 1)]

    while queue:
        d, cur = heappop(queue)

        if distance[cur] < d:
            continue

        for next_d, next in graph[cur]:
            if d + next_d < distance[next]:
                distance[next] = d + next_d
                heappush(queue, (d + next_d, next))

    return distance[-1]


N, M = map(int, input().split())
graph = defaultdict(list)
for _ in range(M):
    x, y, w = map(int, input().split())
    graph[x].append((w, y))
    graph[y].append((w, x))

print(dijkstra())
