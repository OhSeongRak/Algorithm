'''
무슨 데이터가 필요할까?
가장 최근에 공격한 포탑
공격한지 오래된 포탑
위에 두개들은 deque로 관리하면 될라나
맨 앞이 가장 오래된, 맨 뒤가 가장 최근인
공격과 무관했던 포탑 => 이것도 큐
'''
import sys
from collections import deque

input = sys.stdin.readline


def find_offender():
    '''
    [언제 공격했는지(1:늦게, 10:최근), 행열합, 열값, r, c]
    이 정보를 넣어서 reverse 정렬하면 공격자를 찾을 수 있음
    '''
    queue = deque() 
    infos = []
    min_value = sys.maxsize

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                continue
            min_value = min(board[i][j], min_value)

    for i in range(N):
        for j in range(M):
            if board[i][j] == min_value:
                queue.append((i, j))

    for r, c in queue:
        infos.append([time_board[r][c], r + c, c, r, c])

    infos.sort(reverse=True)
    return infos[0][3], infos[0][4]


def find_defender():
    queue = deque()
    infos = []
    max_value = 0

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0 or (i == ofr and j == ofc):
                continue
            max_value = max(board[i][j], max_value)

    for i in range(N):
        for j in range(M):
            if i == ofr and j == ofc:
                continue

            if board[i][j] == max_value:
                queue.append((i, j))

    for r, c in queue:
        infos.append([time_board[r][c], r + c, c, r, c])

    infos.sort()
    return infos[0][3], infos[0][4]


def razor():
    global attacked_list
    queue = deque()
    queue.append((ofr, ofc, []))
    visited = [[False] * M for _ in range(N)]
    visited[ofr][ofc] = True

    while queue:
        r, c, route = queue.popleft()

        if r == dfr and c == dfc:
            attacked_list = route
            for ar, ac in route[:-1]:
                board[ar][ac] -= (board[ofr][ofc] // 2)
                board[ar][ac] = max(board[ar][ac], 0)

            board[r][c] -= board[ofr][ofc]
            board[r][c] = max(board[r][c], 0)
            return True

        for i in range(4):
            nr = (r + dr[i]) % N
            nc = (c + dc[i]) % M

            if visited[nr][nc] or board[nr][nc] == 0:
                continue

            queue.append((nr, nc, route + [(nr, nc)]))
            visited[nr][nc] = True

    return False


def turret():
    global attacked_list

    attacked_list = []
    ddr = [1, 1, 1, 0, 0, -1, -1, -1]
    ddc = [1, 0, -1, 1, -1, 1, 0, -1]

    for i in range(8):
        nr = (dfr + ddr[i]) % N
        nc = (dfc + ddc[i]) % M

        if board[nr][nc] == 0 or (nr == ofr and nc == ofc):
            continue

        attacked_list.append((nr, nc))
        board[nr][nc] -= (board[ofr][ofc] // 2)
        board[nr][nc] = max(board[nr][nc], 0)

    attacked_list.append((dfr, dfc))
    board[dfr][dfc] -= board[ofr][ofc]
    board[dfr][dfc] = max(board[dfr][dfc], 0)


def attack():
    if not razor():
        turret()


def repair():
    for r in range(N):
        for c in range(M):
            if (r, c) in attacked_list or (r == ofr and c == ofc) or board[r][c] == 0:
                continue
            board[r][c] += 1


dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
N, M, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
time_board = [[0] * M for _ in range(N)]
attacked_list = []
ofr, ofc, dfr, dfc = 0, 0, 0, 0


def check_only_one():
    cnt = 0
    for r in range(N):
        for c in range(M):
            if board[r][c] == 0:
                continue
            cnt += 1

    return False if cnt > 1 else True


for time in range(K):
    ofr, ofc = find_offender()
    board[ofr][ofc] += N + M
    time_board[ofr][ofc] = time + 1
    dfr, dfc = find_defender()
    attack()
    repair()
    if check_only_one():
        break

    # print("number: ", time + 1)
    # print(*board, sep='\n')
    # print("=========================")

max_value = 0
for r in range(N):
    for c in range(M):
        max_value = max(max_value, board[r][c])

# print(*board, sep='\n')
print(max_value)
