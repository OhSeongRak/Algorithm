import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def in_range(r, c):
    if 0 <= r < R and 0 <= c < C:
        return True
    return False


def solution():
    pq = []
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    visited = [[False] * C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if i == 0 or j == 0 or i == R - 1 or j == C - 1:
                heappush(pq, (-board[i][j], i, j))
                visited[i][j] = True

    count = 0
    while count < K:
        count += 1
        cost, r, c = heappop(pq)
        print(r + 1, c + 1)

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if in_range(nr, nc) and not visited[nr][nc]:
                heappush(pq, (-board[nr][nc], nr, nc))
                visited[nr][nc] = True

    return


R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
K = int(input())
solution()
