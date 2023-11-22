import sys

input = sys.stdin.readline
'''
플레이어 정보를 따로 모아둘까
player[0] = [1, 3, 2, 3, 0] : r, c, d, s, gun
'''


def print_board():
    print(*board, sep='\n')
    print("========================")


def print_player():
    print(*player, sep='\n')


N, M, K = map(int, input().split())
board = [[[] for _ in range(N)] for _ in range(N)]
for i in range(N):
    tmp = list(map(int, input().split()))
    for j in range(N):
        board[i][j].append(tmp[j])

player = []
for _ in range(M):
    player.append(list(map(int, input().split())) + [0])
    player[-1][0] -= 1
    player[-1][1] -= 1

point = [0] * M
# 상부터 시계방향
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]


def is_player(r, c):
    for i in range(M):
        if r == player[i][0] and c == player[i][1]:
            return i

    return -1


def select_gun(me, r, c):
    board[r][c].append(player[me][4])
    # 최대값 플레이어에게 주고, 총 리스트에서 지우기
    player[me][4] = max(board[r][c])
    board[r][c].remove(player[me][4])

    player[me][0], player[me][1] = r, c


def can_go(nr, nc):
    if 0 <= nr < N and 0 <= nc < N and is_player(nr, nc) == -1:
        return True
    return False


def result(winner, loser, r, c):
    if player[loser][4] != 0:
        board[r][c].append(player[loser][4])
        player[loser][4] = 0

    d = player[loser][2]
    nr = r + dr[d]
    nc = c + dc[d]
    while not can_go(nr, nc):
        d = (d + 1) % 4
        nr = r + dr[d]
        nc = c + dc[d]

    select_gun(loser, nr, nc)
    select_gun(winner, r, c)
    player[loser][0], player[loser][1], player[loser][2] = nr, nc, d


def fight(me, op, r, c):
    me_hab = player[me][3] + player[me][4]
    op_hab = player[op][3] + player[op][4]
    # 상대방이 더 세다면
    if me_hab < op_hab or (me_hab == op_hab and player[me][3] < player[op][3]):
        point[op] += (op_hab - me_hab)
        result(op, me, r, c)
    else:
        point[me] += (me_hab - op_hab)
        result(me, op, r, c)

    return


def move(me):
    r, c, d, s, g = player[me]

    nr = r + dr[d]
    nc = c + dc[d]
    if nr < 0 or nr >= N:
        nr = r - dr[d]
        d = (d + 2) % 4
    if nc < 0 or nc >= N:
        nc = c - dc[d]
        d = (d + 2) % 4

    player[me][2] = d
    op = is_player(nr, nc)
    if op == -1:
        select_gun(me, nr, nc)
    else:
        fight(me, op, nr, nc)


for _ in range(K):
    for i in range(M):
        move(i)
    print_player()
    print_board()
    print(point)
# r c d s
