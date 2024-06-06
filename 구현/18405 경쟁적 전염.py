import sys

from collections import deque

input = sys.stdin.readline


def sort_by_number():
    lst = []
    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                continue
            lst.append((board[r][c], r, c, 0))

    return sorted(lst)


def in_range(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    return False


def solution():
    queue = deque(sort_by_number())

    while queue:
        number, r, c, count = queue.popleft()

        if count == S:
            break

        for i in range(4):
            nr = r + d[i]
            nc = c + d[i - 1]

            if not in_range(nr, nc) or board[nr][nc] != 0:
                continue

            queue.append((number, nr, nc, count + 1))
            board[nr][nc] = number

    return board[X - 1][Y - 1]


d = [1, 0, -1, 0]
N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())
print(solution())
