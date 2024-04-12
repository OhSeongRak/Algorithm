import sys

from collections import deque

input = sys.stdin.readline


def rotate(r, c, K):
    tmp = [[board[r + i][c + j] for j in range(K)] for i in range(K)]
    tmp = list(zip(*tmp[::-1]))

    for i in range(K):
        for j in range(K):
            board[r + i][c + j] = tmp[i][j]

    return


def magic():
    K = 2 ** L
    for r in range(0, N, K):
        for c in range(0, N, K):
            rotate(r, c, K)

    return


def in_range(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    return False


def reduce_ice():
    melt = []

    for r in range(N):
        for c in range(N):
            if board[r][c] == 0:
                continue

            count = 0
            for dr, dc in drc:
                nr, nc = r + dr, c + dc
                if not in_range(nr, nc):
                    continue
                if board[nr][nc] > 0:
                    count += 1

            if count < 3:
                melt.append((r, c))

    for r, c in melt:
        board[r][c] -= 1

    return


def area_size(r, c):
    visited[r][c] = True
    size, total = 1, board[r][c]

    queue = deque()
    queue.append((r, c))

    while queue:
        r, c = queue.popleft()

        for dr, dc in drc:
            nr, nc = r + dr, c + dc
            if not in_range(nr, nc) or board[nr][nc] == 0 or visited[nr][nc]:
                continue

            queue.append((nr, nc))
            visited[nr][nc] = True
            size += 1
            total += board[nr][nc]

    return size, total


N, Q = map(int, input().split())
N = 2 ** N
board = [list(map(int, input().split())) for _ in range(N)]
L_list = list(map(int, input().split()))
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for L in L_list:
    magic()
    reduce_ice()

total = 0
max_size = 0
visited = [[False] * N for _ in range(N)]
for r in range(N):
    for c in range(N):
        if board[r][c] != 0 and not visited[r][c]:
            size, ice = area_size(r, c)
            total += ice
            max_size = max(max_size, size)

# print(*board, sep='\n')
print(total)
print(max_size)
