import sys

from collections import deque

input = sys.stdin.readline


def in_range(r, c):
    if 0 <= r < R and 0 <= c < C:
        return True
    return False


def solution():
    queue = deque()

    # 불을 먼저 큐에 넣어야 지훈이 불타는 경우가 나옴
    for r in range(R):
        for c in range(C):
            if board[r][c] == 'F':
                queue.append((r, c, 'F', -1))  # 불의 거리는 의미 없음

    for r in range(R):
        for c in range(C):
            if board[r][c] == 'J':
                queue.append((r, c, 'J', 0))

    while queue:
        r, c, o, d = queue.popleft()

        for dr, dc in drc:
            nr = r + dr
            nc = c + dc

            if o == 'J':
                if not in_range(nr, nc):  # 범위 밖이면 탈출
                    return d + 1
                if board[nr][nc] != '.':
                    continue
                queue.append((nr, nc, 'J', d + 1))
                board[nr][nc] = 'J'

            if o == 'F':
                if not in_range(nr, nc) or board[nr][nc] == '#' or board[nr][nc] == 'F':
                    continue
                queue.append((nr, nc, 'F', -1))
                board[nr][nc] = 'F'

    return "IMPOSSIBLE"


drc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
print(solution())
