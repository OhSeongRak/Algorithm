import sys

from collections import deque

input = sys.stdin.readline
'''
고려할 것
0. 편의점에 도착하거나, 베이스캠프 도달 시 -1 처리
1. 최단 경로에 있는 베이스캠프 or CU가 X가 되는 경우
 - 신경쓰지 말고, 이동할 때는 항상 BFS로 찾기
2. 모두 이동 후 X가 됨
3. 이동 후 베이스캠프에 배치
4. 사람 이동 : 상 좌 우 하 / 베이스캠프 찾기 : 행이 작은 -> 열이 작은
5. 그래서 사람 이동은?
 - board에 쓰기 / 리스트 하나 만들기 => 리스트를 만들어야 같은 위치 판단 가능.
6. 도착 판단 : people과 board가 같으면 continue
'''


def all_arrived():
    for i in range(M):
        if cu[i][0] != people[i][0] or cu[i][1] != people[i][1]:
            return False
    return True


def set_people(number):
    queue = deque()
    queue.append((cu[number][0], cu[number][1], 0))
    visited = [[False] * N for _ in range(N)]
    candidate = []  # 베이스캠프 후보

    while queue:
        r, c, d = queue.popleft()

        if board[r][c] == 1:
            candidate.append((d, r, c))

        for i in range(4):
            nr = r + drc[i][0]
            nc = c + drc[i][1]

            if not in_range(nr, nc) or visited[nr][nc] or board[nr][nc] == -1:
                continue

            queue.append((nr, nc, d + 1))
            visited[nr][nc] = True

    candidate.sort(key=lambda x: (x[0], x[1], x[2]))  # 거리, 행, 열 순으로 오름차순 정렬
    r, c = candidate[0][1], candidate[0][2]
    people[number][0], people[number][1] = r, c
    board[r][c] = -1

    return


def in_range(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    return False


def make_route(number, r, c):
    global route

    queue = deque()
    queue.append((r, c, []))
    visited = [[False] * N for _ in range(N)]

    while queue:
        r, c, lst = queue.popleft()

        if r == cu[number][0] and c == cu[number][1]:
            route[number] = lst
            break

        for i in range(4):  # 상, 좌, 우, 하 순
            nr = r + drc[i][0]
            nc = c + drc[i][1]

            if not in_range(nr, nc) or visited[nr][nc] or board[nr][nc] == -1:
                continue

            queue.append((nr, nc, lst + [(nr, nc)]))
            visited[nr][nc] = True

    return


def move_people():
    for i in range(M):
        r, c = people[i][0], people[i][1]
        # 아직 출발 안했거나, 편의점에 도착한 친구면 놔둠
        if (r == -1 and c == -1) or (r == cu[i][0] and c == cu[i][1]):
            continue

        if not route[i]:  # 아직 경로가 정해지지 않은 친구면 정해줌
            make_route(i, r, c)
        else:
            for rr, rc in route[i]:
                if board[rr][rc] == -1:  # 만약 원래의 경로가 막혔다면
                    make_route(i, r, c)  # 다시 경로를 생성
                    break

        # 경로 지정이 다 끝났다면, 경로대로 움직임
        people[i][0] = route[i][0][0]
        people[i][1] = route[i][0][1]
        route[i] = route[i][1:]

    for i in range(M):
        r, c = people[i][0], people[i][1]

        if r == -1 and c == -1:
            break
        if cu[i][0] == r and cu[i][1] == c:  # 편의점에 도착했다면, -1 처리
            board[r][c] = -1

    return


N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
people, cu = [], []
for _ in range(M):
    r, c = map(int, input().split())
    cu.append((r - 1, c - 1))
    people.append([-1, -1])

route = [[] for _ in range(M)]
drc = [(-1, 0), (0, -1), (0, 1), (1, 0)]
time = 0
while not all_arrived():
    move_people()  # 격자에 있는 사람 모두 움직임
    if time < M:  # 베이스캠프에 사람 놓기
        set_people(time)
    time += 1

print(time)
