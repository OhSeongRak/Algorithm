import sys
from collections import deque

input = sys.stdin.readline


def in_range(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    return False


def bfs(r, c):
    visited = [[False] * N for _ in range(N)]
    visited[r][c] = True
    queue = deque()
    queue.append((r, c))
    number = board[r][c]
    group = [(r, c)]
    rainbow_count = 0

    while queue:
        r, c = queue.popleft()

        for dr, dc in drc:
            nr = r + dr
            nc = c + dc

            if not in_range(nr, nc) or visited[nr][nc] or board[nr][nc] not in [0, number]:
                continue

            visited[nr][nc] = True
            group.append((nr, nc))
            queue.append((nr, nc))
            if board[nr][nc] == 0:
                rainbow_count += 1

    if len(group) > 1:
        group_list.append(group + [rainbow_count])

    return


def not_checked(r, c):
    for group in group_list:
        if (r, c) in group:
            return False
    return True


def check_block_group():
    for r in range(N):
        for c in range(N):
            if not_checked(r, c) and board[r][c] > 0:
                bfs(r, c)

    group_list.sort(key=lambda x: (len(x), x[-1], x[0][0], x[0][1]), reverse=True)
    return


def remove_block():
    global score, group_list

    remove_group = group_list[0][:-1]
    size = len(remove_group)
    score += size * size

    for r, c in remove_group:
        board[r][c] = -2

    group_list = []

    return


def gravity():
    under_area = deque()

    for c in range(N):
        for r in range(N)[::-1]:
            if board[r][c] == -2:
                under_area.append((r, c))
            elif board[r][c] == -1:
                under_area = deque()
            else:
                if under_area:
                    er, ec = under_area.popleft()
                    board[er][ec], board[r][c] = board[r][c], -2
                    under_area.append((r, c))

        under_area = deque()

    return


def rotate_reverse_90():
    global board
    tmp = [[board[r][c] for c in range(N)] for r in range(N)]

    for c in range(N):
        for r in range(N):
            board[r][c] = tmp[c][N - r - 1]

    return


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
group_list = []
drc = [(0, 1), (1, 0), (-1, 0), (0, -1)]
score = 0

while True:
    check_block_group()

    if not group_list:
        break

    remove_block()
    gravity()
    rotate_reverse_90()
    gravity()

print(score)
