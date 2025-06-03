import sys
from collections import deque

input = sys.stdin.readline


def bfs(start):
    queue = deque([(start, -1)])
    visited = dict()
    visited[(start, -1)] = True

    while queue:
        m, c = queue.popleft()

        if m == 0:
            return 'Y'

        if c == C - 1:
            continue

        if (m, c + 1) not in visited.keys():
            visited[(m, c + 1)] = True
            queue.append((m, c + 1))

        if (m - chu[c + 1], c + 1) not in visited.keys():
            visited[(m - chu[c + 1], c + 1)] = True
            queue.append((m - chu[c + 1], c + 1))

        if (m + chu[c + 1], c + 1) not in visited.keys():
            visited[(m + chu[c + 1], c + 1)] = True
            queue.append((m + chu[c + 1], c + 1))

    return 'N'


C = int(input())
chu = list(map(int, input().split()))
M = int(input())
marble = list(map(int, input().split()))
for m in marble:
    print(bfs(m), end=" ")
