import sys

from collections import deque

input = sys.stdin.readline


def in_range(r, c):
    if 0 <= r < 12 and 0 <= c < 6:
        return True
    return False


def check(r, c):
    drc = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = deque()
    queue.append((r, c))
    visited = set()
    visited.add((r, c))

    while queue:
        r, c = queue.popleft()

        for dr, dc in drc:
            nr = r + dr
            nc = c + dc
            if (not in_range(nr, nc) or board[nr][nc] != board[r][c]
                    or (nr, nc) in visited):
                continue

            visited.add((nr, nc))
            queue.append((nr, nc))

    if len(visited) >= 4:
        for r, c in visited:
            board[r][c] = '.'
        return True

    return False


def bomb():
    bombed = False

    for r in range(12):
        for c in range(6):
            if board[r][c] == '.':
                continue
            if check(r, c):
                bombed = True

    return bombed


def drop():
    for c in range(6):
        tmp = []
        for r in range(12):
            if board[r][c] != '.':
                tmp.append(board[r][c])
                board[r][c] = '.'

        r = -1
        while tmp:
            board[r][c] = tmp.pop()
            r -= 1

    return


board = [list(input().strip()) for _ in range(12)]
count = 0
while True:
    if not bomb():
        break
    count += 1
    drop()
print(count)
