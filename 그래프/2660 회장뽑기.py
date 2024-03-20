import sys

from collections import deque

input = sys.stdin.readline


def bfs(v):
    visited = [False] * (N + 1)
    visited[v] = True
    queue = deque()
    queue.append((v, 0))
    answer = 0

    while queue:
        cur, d = queue.popleft()
        answer = d

        for n in graph[cur]:
            if visited[n]:
                continue
            queue.append((n, d + 1))
            visited[n] = True

    return answer


N = int(input())
graph = [[] for _ in range(N + 1)]
score_list = [0] * (N + 1)

while True:
    a, b = map(int, input().split())
    if a == b == -1:
        break
    graph[a].append(b)
    graph[b].append(a)

for v in range(1, N + 1):
    score_list[v] = bfs(v)

min_score = min(score_list[1:])
count = 0
candidate_list = []
for v in range(1, N + 1):
    if score_list[v] == min_score:
        count += 1
        candidate_list.append(v)

print(min_score, count)
for c in candidate_list:
    print(c, end=' ')
