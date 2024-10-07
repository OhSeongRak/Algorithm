import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline


def fillEmptyList():
    for r in range(R):
        for c in range(C):
            if original[r][c] == 0:
                emptyList.append((r, c))

    return


def copy_board():
    for r in range(R):
        for c in range(C):
            board[r][c] = original[r][c]


def in_range(r, c):
    if 0 <= r < R and 0 <= c < C:
        return True
    return False


def bfs(r, c):
    drc = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True

    while queue:
        r, c = queue.popleft()

        for dr, dc in drc:
            nr = r + dr
            nc = c + dc

            if not in_range(nr, nc) or visited[nr][nc] or board[nr][nc] == 1:
                continue

            queue.append((nr, nc))
            board[nr][nc] = 2
            visited[nr][nc] = True

    return


R, C = map(int, input().split())
original = [list(map(int, input().split())) for _ in range(R)]
emptyList, board = [], [[0] * C for _ in range(R)]
visited = [[False] * C for _ in range(R)]
answer = 0

fillEmptyList()
for wallList in list(combinations(emptyList, 3)):
    copy_board()
    visited = [[False] * C for _ in range(R)]

    for r, c in wallList:
        board[r][c] = 1

    for r in range(R):
        for c in range(C):
            if board[r][c] == 2 and not visited[r][c]:
                bfs(r, c)
                # print(*board, sep='\n')
                # print("=========================")

    cnt = 0
    for r in range(R):
        for c in range(C):
            if board[r][c] == 0:
                cnt += 1

    answer = max(answer, cnt)

print(answer)
