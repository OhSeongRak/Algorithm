import sys

from collections import deque

input = sys.stdin.readline


def in_range(r, c):
    if 0 <= r < R and 0 <= c < C:
        return True
    return False


def solution():
    queue = deque()
    visited = [[False] * C for _ in range(R)]

    for r in range(R):
        for c in range(C):
            if board[r][c] == '*':
                queue.append((r, c, -1))

    for r in range(R):
        for c in range(C):
            if board[r][c] == '@':
                queue.append((r, c, 0))
                visited[r][c] = True

    while queue:
        r, c, d = queue.popleft()

        if d == -1:  # 불일 때
            for dr, dc in drc:
                nr = r + dr
                nc = c + dc

                if not in_range(nr, nc) or board[nr][nc] == '#' or board[nr][nc] == '*':
                    continue
                board[nr][nc] = '*'
                queue.append((nr, nc, -1))

        else:
            for dr, dc in drc:
                nr = r + dr
                nc = c + dc

                if not in_range(nr, nc):
                    return d + 1
                if visited[nr][nc] or board[nr][nc] == '#' or board[nr][nc] == '*':
                    continue
                queue.append((nr, nc, d + 1))
                visited[nr][nc] = True

    return "IMPOSSIBLE"


drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
T = int(input())
for _ in range(T):
    C, R = map(int, input().split())
    board = [list(input().strip()) for _ in range(R)]
    print(solution())
