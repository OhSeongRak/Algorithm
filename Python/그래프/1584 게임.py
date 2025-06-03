import sys

from heapq import heappop, heappush

input = sys.stdin.readline


def in_range(r, c):
    if 0 <= r < 501 and 0 <= c < 501:
        return True
    return False


def solution():
    pq = [(0, 0, 0)]
    INF = sys.maxsize
    distance = [[INF] * 501 for _ in range(501)]
    distance[0][0] = 0

    while pq:
        life, r, c = heappop(pq)

        if distance[r][c] < life:
            continue

        for dr, dc in drc:
            nr = r + dr
            nc = c + dc

            if not in_range(nr, nc) or board[nr][nc] == -1:
                continue

            if life + board[nr][nc] < distance[nr][nc]:
                distance[nr][nc] = life + board[nr][nc]
                heappush(pq, (distance[nr][nc], nr, nc))

    return -1 if distance[500][500] == INF else distance[500][500]


board = [[0] * 501 for _ in range(501)]
drc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
N = int(input())
for _ in range(N):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1

    for r in range(y1, y2 + 1):
        for c in range(x1, x2 + 1):
            board[r][c] = 1

M = int(input())
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 > x2:
        x1, x2 = x2, x1
    if y1 > y2:
        y1, y2 = y2, y1
    for r in range(y1, y2 + 1):
        for c in range(x1, x2 + 1):
            board[r][c] = -1

print(solution())
