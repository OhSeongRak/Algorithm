import sys

input = sys.stdin.readline


def move_fireballs():
    for i in range(len(fireballs)):
        r, c, _, s, d = fireballs[i]
        r = (N + r + s * dr[d]) % N
        c = (N + c + s * dc[d]) % N
        fireballs[i][0], fireballs[i][1] = r, c

    return


def set_fireballs_to_board():
    global board

    board = [[[] for _ in range(N)] for _ in range(N)]
    for r, c, m, s, d in fireballs:
        board[r][c].append([m, s, d])

    return


def divide_fireballs():
    global fireballs

    fireballs = []
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) == 0:
                continue
            if len(board[i][j]) == 1:
                fireballs.append([i, j] + board[i][j][0])
                continue

            m_sum, s_sum, dir = 0, 0, 0
            for m, s, d in board[i][j]:
                m_sum += m
                s_sum += s
                if d % 2 != board[i][j][0][2] % 2:  # 첫번째 파이어볼의 방향과 다를 경우
                    dir = 1

            m, s = m_sum // 5, s_sum // len(board[i][j])

            if m == 0:
                continue

            for k in range(4):
                d = k * 2 + dir
                fireballs.append([i, j, m, s, d])

    return


N, M, K = map(int, input().split())
fireballs = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())  # r, c, 질량, 방향, 속력
    fireballs.append([r - 1, c - 1, m, s, d])

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]

board = [[[] for _ in range(N)] for _ in range(N)]

for _ in range(K):
    move_fireballs()
    set_fireballs_to_board()
    divide_fireballs()

total = 0
for fireball in fireballs:
    total += fireball[2]

print(total)
