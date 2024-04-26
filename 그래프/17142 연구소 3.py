import sys

from itertools import combinations
from collections import deque

input = sys.stdin.readline


def copy_board():
    board = [[origin[r][c] for c in range(N)] for r in range(N)]

    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                board[r][c] = '-'  # 빈 공간
            elif board[r][c] == 1:
                board[r][c] = -1  # 벽
            elif board[r][c] == 2:
                board[r][c] = '*'  # 비활성 바이러스
    return board


def in_range(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    return False


def bfs(activate, board):
    drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque()
    count = 0

    for r, c in activate:
        queue.append((r, c, 0))

    while queue:
        r, c, d = queue.popleft()

        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc) or (board[nr][nc] != '-' and board[nr][nc] != '*'):
                continue
            queue.append((nr, nc, d + 1))
            if board[nr][nc] == '-':  # 해당 칸이 벽일 때만 시간 체크
                count = max(count, d + 1)
            board[nr][nc] = d + 1

    for r in range(N):
        for c in range(N):
            if board[r][c] == '-':
                return MAX_SIZE

    return count


def solution():
    answer = MAX_SIZE

    for activate in list(combinations(virus, M)):
        board = copy_board()
        for r, c in activate:
            board[r][c] = 0

        count = bfs(activate, board)
        answer = min(answer, count)

    return answer if answer != MAX_SIZE else -1


N, M = map(int, input().split())
MAX_SIZE = N * N
origin = [list(map(int, input().split())) for _ in range(N)]
virus = []
for r in range(N):
    for c in range(N):
        if origin[r][c] == 2:
            virus.append((r, c))

print(solution())
