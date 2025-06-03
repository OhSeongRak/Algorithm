import sys
from collections import defaultdict, deque

input = sys.stdin.readline
'''
P에서 시작해서 가장 가까운 지지대 2개를 고름.
전체 얼음 - (2개의 지지대까지 거리 + P 얼음)
'''


def solution():
    distance = [-1] * (N + 1)
    distance[P] = 0
    queue = deque([(P, 0)])

    while queue:
        cur, d = queue.popleft()

        for v in graph[cur]:
            if distance[v] != -1:
                continue
            queue.append((v, d + 1))
            distance[v] = d + 1

    support = sorted(distance[1:S + 1])

    return N - support[0] - support[1] - 1


N, S, P = map(int, input().split())
graph = defaultdict(list)
for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

print(solution())
