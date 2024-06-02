import sys
from collections import deque

input = sys.stdin.readline


def in_range(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    return False


def solution():
    # 계산 편하게 하기 위해 0-1 바꿈
    for r in range(N):
        for c in range(N):
            board[r][c] = 1 - board[r][c]

    drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited = [[N * N] * N for _ in range(N)]  # r, c까지 경로의 검은 방의 최소 개수

    queue = deque()
    queue.append((0, 0, 0))
    visited[0][0] = 0

    while queue:
        r, c, k = queue.popleft()

        if r == N - 1 and c == N - 1:
            continue

        for dr, dc in drc:
            nr = r + dr
            nc = c + dc

            if not in_range(nr, nc):
                continue

            if visited[nr][nc] <= k + board[nr][nc]:
                continue

            queue.append((nr, nc, k + board[nr][nc]))
            visited[nr][nc] = k + board[nr][nc]

    return visited[-1][-1]


N = int(input())
board = [list(map(int, input().strip())) for _ in range(N)]
print(solution())
