import sys
from collections import deque

input = sys.stdin.readline


def inRange(r, c):
    if 0 <= r < 5 and 0 <= c < 5:
        return True
    return False


def boardToOrigin():
    for r in range(5):
        for c in range(5):
            origin[r][c] = board[r][c]
    return


def originToBoard():
    for r in range(5):
        for c in range(5):
            board[r][c] = origin[r][c]
    return


def rotateBoard(r, c):
    tmp = [[0] * 3 for _ in range(3)]

    for i in range(3):
        for j in range(3):
            tmp[i][j] = board[r - j + 1][c + i - 1]

    for i in range(3):
        for j in range(3):
            board[r - 1 + i][c - 1 + j] = tmp[i][j]

    return


def bfs(r, c, visited, getList):
    visited[r][c] = True
    queue = deque()
    queue.append((r, c))
    tmpList = [[r, c]]

    while queue:
        r, c = queue.popleft()

        for dr, dc in drc:
            nr = r + dr
            nc = c + dc

            if not inRange(nr, nc) or visited[nr][nc] or board[r][c] != board[nr][nc]:
                continue

            tmpList.append([nr, nc])
            queue.append((nr, nc))
            visited[nr][nc] = True

    if len(tmpList) >= 3:
        getList.extend(tmpList)

    return


def checkBoard(r, c, rotCnt):
    global maxList, R, C, ROTCNT
    visited = [[False] * 5 for _ in range(5)]
    getList = []

    for i in range(5):
        for j in range(5):
            if visited[i][j]:
                continue
            bfs(i, j, visited, getList)

    if len(maxList) < len(getList) or (len(maxList) == len(getList) and rotCnt < ROTCNT):
        maxList = []
        for i in range(len(getList)):
            maxList.append(getList[i])
        R, C, ROTCNT = r, c, rotCnt

    return


def solution():
    global wallCnt, maxList, R, C, ROTCNT

    total = 0

    for c in range(1, 4):
        for r in range(1, 4):
            originToBoard()
            for rotCnt in range(1, 4):
                rotateBoard(r, c)
                checkBoard(r, c, rotCnt)

    originToBoard()
    while maxList:
        for i in range(ROTCNT):
            rotateBoard(R, C)

        maxList.sort(key=lambda x: (x[1], -x[0]))
        for r, c in maxList:
            board[r][c] = wallNumber[wallCnt]
            wallCnt += 1
        total += len(maxList)

        maxList = []
        R, C, ROTCNT = 0, 0, 0
        checkBoard(R, C, ROTCNT)
    boardToOrigin()

    return total


K, M = map(int, input().split())
origin = [list(map(int, input().split())) for _ in range(5)]
board = [[0] * 5 for _ in range(5)]
wallNumber = list(map(int, input().split()))
wallCnt = 0
answerList = []
maxList = []
R, C, ROTCNT = 0, 0, 0
drc = [(0, 1), (1, 0), (0, -1), (-1, 0)]

for _ in range(K):
    maxList = []
    total = solution()

    if total == 0:
        break
    answerList.append(total)

print(*answerList)

'''
우선순위
유물 획득 개수 -> 회전 각도 작은것 -> 중심 열이 작은거 -> 행이 작은거

변수
벽면 : 벽면을 deque로 해서 popleft 사용하면 편할듯
벽면cnt
오리진, 보드
획득 리스트
answerList

함수
체크 유물

진행 순서
for 1,1 ~ 4,4까지 (행을 우선 이동)
    for 90, 180, 270
        rotate(90) --> 여기 안에서 유물 획득 체크 획득 리스트와 비교
                        비교해서 더 크면 넣고 아니면 안넣음(회전 각도, 행, 열 기준으로 반복하기에)
'''
