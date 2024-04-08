import sys

from collections import deque

input = sys.stdin.readline

'''
1. 이동 했을 때, 벽이 있는지 확인. => 이동한 위치에 기사는 몇 명인지 확인 => 계속 반복
2. 이상 없이 다 이동할 수 있다? => 이동한 knigts 배열의 위치 정보를 갱신 
3. 덫 배열을 통해 기사 체력 갱신 but 이미 죽은 기사는 제외 (총 대미지 추가)
4. 체력이 0 이상인 기사들만 기사 보드에 초기화
'''


def reset_k_board():
    for r in range(L):
        for c in range(L):
            k_board[r][c] = 0

    number = 0

    for r, c, h, w, k in knights[1:]:
        number += 1
        if k == 0:
            continue
        for i in range(r, r + h):
            for j in range(c, c + w):
                k_board[i][j] = number

    return


def in_range(r, c):
    if 0 <= r < L and 0 <= c < L:
        return True
    return False


def can_move(number, d):
    queue = deque()
    queue.append(number)

    while queue:
        number = queue.popleft()
        r, c, h, w, _ = knights[number]

        if d == 0:  # 위
            for i in range(c, c + w):
                if not in_range(r - 1, i) or board[r - 1][i] == 2:  # 보드 밖이거나, 벽이면
                    return False

                if k_board[r - 1][i] != 0 and k_board[r - 1][i] not in pushed:  # 기사가 있다면
                    queue.append(k_board[r - 1][i])
                    pushed.append(k_board[r - 1][i])

        if d == 1:  # 오른
            for i in range(r, r + h):
                if not in_range(i, c + w) or board[i][c + w] == 2:  # 보드 밖이거나, 벽이면
                    return False

                if k_board[i][c + w] != 0 and k_board[i][c + w] not in pushed:  # 기사가 있다면
                    queue.append(k_board[i][c + w])
                    pushed.append(k_board[i][c + w])

        if d == 2:  # 아래
            for i in range(c, c + w):
                if not in_range(r + h, i) or board[r + h][i] == 2:  # 보드 밖이거나, 벽이면
                    return False

                if k_board[r + h][i] != 0 and k_board[r + h][i] not in pushed:  # 기사가 있다면
                    queue.append(k_board[r + h][i])
                    pushed.append(k_board[r + h][i])

        if d == 3:  # 왼
            for i in range(r, r + h):
                if not in_range(i, c - 1) or board[i][c - 1] == 2:  # 보드 밖이거나, 벽이면
                    return False

                if k_board[i][c - 1] != 0 and k_board[i][c - 1] not in pushed:  # 기사가 있다면
                    queue.append(k_board[i][c - 1])
                    pushed.append(k_board[i][c - 1])

    return True


def damage_hp(number):
    r, c, h, w, k = knights[number]
    d = 0

    for i in range(r, r + h):
        for j in range(c, c + w):
            if board[i][j] == 1:
                d += 1

    return d


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
L, N, Q = map(int, input().split())  # 크기, 기사, 명령
board = [list(map(int, input().split())) for _ in range(L)]
knights = [[]]
hps = []
for _ in range(N):
    r, c, h, w, k = map(int, input().split())
    knights.append([r - 1, c - 1, h, w, k])
    hps.append(k)

orders = []
for _ in range(Q):
    i, d = map(int, input().split())
    orders.append([i, d])

k_board = [[0] * L for _ in range(L)]

# solution
for number, d in orders:
    reset_k_board()
    # print(*k_board, sep='\n')
    # print("================")

    pushed = []
    if knights[number][4] == 0:
        continue

    if can_move(number, d):
        knights[number][0] += dr[d]
        knights[number][1] += dc[d]

        pushed = list(set(pushed))
        while pushed:
            p_number = pushed.pop()  # 밀린 기사 번호
            knights[p_number][0] += dr[d]
            knights[p_number][1] += dc[d]

            damaged = damage_hp(p_number)  # 덫 개수
            knights[p_number][4] = max(0, knights[p_number][4] - damaged)

answer = 0
for i in range(N):
    if knights[i + 1][4] == 0:
        continue
    answer += hps[i] - knights[i + 1][4]

print(answer)
