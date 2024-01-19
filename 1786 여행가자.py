import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    queue = deque()
    queue.append(start)
    visited[start] = True

    while queue:
        v = queue.popleft()
        for i in range(N):
            if graph[v][i] == 0 or visited[i]:
                continue
            visited[i] = True
            queue.append(i)

    return


def solution():
    bfs(plan[0] - 1)

    for p in plan:
        if not visited[p - 1]:
            return "NO"

    return "YES"


N = int(input())
M = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
visited = [False] * N
plan = list(map(int, input().split()))
print(solution())
