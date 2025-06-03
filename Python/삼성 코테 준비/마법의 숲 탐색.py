from collections import deque


def in_range(r, c):
    if 0 <= r < R and 0 <= c < C:
        return True
    return False


def can_go(r, c, d):
    if d != 0:
        if in_range(r - 1, c - d) and board[r - 1][c - d] != 0:
            return False

    if c < 0 or c >= C:
        return False

    if in_range(r, c) and board[r][c] != 0:
        return False

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]

        if nc < 0 or nc >= C:
            return False

        if in_range(nr, nc) and board[nr][nc] != 0:
            return False

    return True


def drop_spaceship(c, exit):
    for r in range(R):
        if can_go(r - 1, c, 0):
            continue
        elif can_go(r - 1, c - 1, 1):
            c -= 1
            exit -= 1
            exit = (exit + 4) % 4

        elif can_go(r - 1, c + 1, -1):
            c += 1
            exit = (exit + 1) % 4

        else:
            spaceship.append([r - 2, c, exit])
            return

    spaceship.append([r - 1, c, exit])

    return


def check_spaceship():
    r, c, d = spaceship[-1]

    if not in_range(r, c):
        return False

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if not in_range(nr, nc):
            return False

    return True


def fill_board():
    r, c, d = spaceship[-1]
    n = len(spaceship) - 1
    board[r][c] = n
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        board[nr][nc] = n


def check_score():
    r, c, d = spaceship[-1]
    score = r + 1
    n = len(spaceship) - 1
    visited = set()
    visited.add(n)
    queue = deque()
    queue.append([r, c, d])

    while queue:
        r, c, d = queue.popleft()
        score = max(score, r + 1)
        r += dr[d]
        c += dc[d]

        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]

            if not in_range(nr, nc) or board[nr][nc] == 0 or board[nr][nc] in visited:
                continue

            queue.append(spaceship[board[nr][nc]])
            visited.add(board[nr][nc])

    return score


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
R, C, K = map(int, input().split())
order = []
for _ in range(K):
    r, d = map(int, input().split())
    order.append([r - 1, d])
spaceship = [[]]
board = [[0] * C for _ in range(R)]
answer = 0

for start, dir in order:
    drop_spaceship(start, dir)

    if check_spaceship():
        fill_board()
        answer += check_score() + 1
    else:
        spaceship = [[]]
        board = [[0] * C for _ in range(R)]

print(answer)
