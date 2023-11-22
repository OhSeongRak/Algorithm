import sys, copy
from itertools import combinations
from collections import deque

input = sys.stdin.readline


def check_board(board):
    for i in range(N):
        for j in range(M):
            if board[i][j] != 0:
                return True

    return False


def bfs(board, C):
    dr, dc = [0, -1, 0], [-1, 0, 1]
    queue = deque()
    queue.append((N - 1, C, 1))

    while queue:
        r, c, d = queue.popleft()

        if d > D:
            return

        if board[r][c] == 1:
            kill_set.add((r, c))
            return

        for i in range(3):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= M:
                continue

            queue.append((nr, nc, d + 1))


def down_board(board):
    global kill_set
    for (r, c) in kill_set:
        board[r][c] = 0
    kill_set = set()

    for i in range(N - 1)[::-1]:
        for j in range(M):
            board[i + 1][j] = board[i][j]

    for i in range(M):
        board[0][i] = 0


def solution():
    global kill_set
    answer = 0

    for pos in list(combinations([i for i in range(0, M)], 3)):
        board = [arr[:] for arr in origin_board]
        kill_set = set()
        tmp = 0
        while check_board(board):
            for i in range(3):
                bfs(board, pos[i])
            tmp += len(kill_set)
            down_board(board)
        answer = max(answer, tmp)
        # print(*board, sep='\n')
        # print("==========================")

    return answer


N, M, D = map(int, input().split())
kill_set = set()
origin_board = [list(map(int, input().split())) for _ in range(N)]
print(solution())
