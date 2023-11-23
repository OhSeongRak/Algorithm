import sys
from collections import deque, defaultdict
input = sys.stdin.readline


def solution(k, v):
    visited = [False] * (N + 1)
    visited[v] = True
    queue = deque([(v, sys.maxsize)])
    total = 0

    while queue:
        cur_v, cur_d = queue.popleft()

        for v, d in board[cur_v]:
            d = min(d, cur_d)
            if visited[v] or d < k:
                continue
            queue.append((v, d))
            total += 1
            visited[v] = True

    return total


N, Q = map(int, input().split())
board = defaultdict(list)
for _ in range(N-1):
    p, q, r = map(int, input().split())
    board[p].append([q, r])
    board[q].append([p, r])

for _ in range(Q):
    k ,v = map(int, input().split())
    print(solution(k, v))
