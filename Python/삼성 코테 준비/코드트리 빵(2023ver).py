import sys
from collections import deque

input = sys.stdin.readline

'''
1. 가까운 베이스캠프를 찾을 때의 경로를 저장해둠 => 실패 (갑자기 막혀버리는 상황이 생김)
2. 처음에 모든 인원의 베이스챔프를 정해둠
그냥 queue에 추가하는 느낌으로 가보자
ps. 0번째부터 시작할거임!
'''


def find_basecamp(pos):
    r, c = pos[0], pos[1]
    queue = deque()
    visited = [[False] * N for _ in range(N)]

    visited[r][c] = True
    queue.append((r, c))
    while queue:
        r, c = queue.popleft()
        if board[r][c] == 1:
            board[r][c] = -1
            camps.append((r, c))
            return

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if nr < 0 or nr >= N or nc < 0 or nc >= N or visited[nr][nc] or board[nr][nc] == -1:
                continue

            queue.append((nr, nc))
            visited[nr][nc] = True

    return


def solution():
    for i in range(M):
        find_basecamp(stores[i]) # 시작 위치 정하기

    # print("stores: ", stores)
    queue = deque()
    visited = [[[False] * N for _ in range(N)] for _ in range(M)]

    r, c = camps[0][0], camps[0][1]
    queue.append((r, c, 0, 0))
    visited[0][r][c] = True
    arrived = [False] * M
    person_in = [False] * M
    person_in[0] = True
    cnt = 0
    while True:
        r, c, time, number = queue.popleft()

        if time < M and not person_in[time]: # 새로운 사람 베이스 캠프에 위치
            queue.append((camps[time][0], camps[time][1], time, time))
            person_in[time] = True

        if arrived[number]:
            continue


        if r == stores[number][0] and c == stores[number][1]:
            # print("r, c, time, number: ", r, c, time, number)
            board[r][c] = -1
            arrived[number] = True
            for arrive in arrived:
                if not arrive:
                    break
            else:
                return time + 1

        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if (nr < 0 or nr >= N or nc < 0 or nc >= N
                    or visited[number][nr][nc] or board[nr][nc] == -1):
                continue

            queue.append((nr, nc, time + 1, number))
            visited[number][nr][nc] = True




# a = [(1, 2)]
# b = a + [(2, 3)]
# print(b)
# exit()
dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]
N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
camps = []
stores = []
for _ in range(M):
    r, c = map(int, input().split())
    stores.append((r - 1, c - 1))

print(solution())
#
# print(*board, sep='\n')
# print(*stores, sep='\n')
