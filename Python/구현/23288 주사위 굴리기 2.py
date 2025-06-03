import sys

from collections import deque

input = sys.stdin.readline


def in_range(r, c):
    if 0 <= r < R and 0 <= c < C:
        return True
    return False


def bfs(r, c):
    d = [1, 0, -1, 0]
    queue = deque()
    queue.append((r, c))
    visited = [(r, c)]

    while queue:
        r, c = queue.popleft()

        for i in range(4):
            nr = r + d[i]
            nc = c + d[i - 1]

            if not in_range(nr, nc) or board[nr][nc] != board[r][c] or (nr, nc) in visited:
                continue

            queue.append((nr, nc))
            visited.append((nr, nc))

    total = len(visited)
    for r, c in visited:
        score[r][c] = total

    return


def calculate_score():
    for r in range(R):
        for c in range(C):
            if score[r][c] == 0:
                bfs(r, c)


def move_dice(d):
    if d == 0:
        tmp = dice[1]
        dice[1] = dice[4]
        dice[4] = dice[6]
        dice[6] = dice[3]
        dice[3] = tmp

    if d == 1:
        tmp = dice[1]
        dice[1] = dice[2]
        dice[2] = dice[6]
        dice[6] = dice[5]
        dice[5] = tmp

    if d == 2:
        tmp = dice[1]
        dice[1] = dice[3]
        dice[3] = dice[6]
        dice[6] = dice[4]
        dice[4] = tmp

    if d == 3:
        tmp = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[6]
        dice[6] = dice[2]
        dice[2] = tmp


def solution():
    return


R, C, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
score = [[0] * C for _ in range(R)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
dice = [0, 1, 2, 3, 4, 5, 6]  # (0), 위, 북, 동, 서, 남, 아래

calculate_score()
d, r, c, answer = 0, 0, 0, 0
for _ in range(K):
    if not in_range(r + dr[d], c + dc[d]):
        d = (d + 2) % 4

    move_dice(d)
    r += dr[d]
    c += dc[d]
    answer += score[r][c] * board[r][c]

    if dice[6] > board[r][c]:
        d = (d + 1) % 4
    if dice[6] < board[r][c]:
        d = (d + 3) % 4

print(answer)
