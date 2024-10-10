import sys

input = sys.stdin.readline


def in_range(r, c):
    if 0 <= r < N and 0 <= c < N:
        return True
    return False


def solution(student):
    fCnt, eCnt = -1, -1
    pos = [0, 0]

    for r in range(N):
        for c in range(N):
            if board[r][c] != 0:
                continue

            fTmp, eTmp = 0, 0
            for dr, dc in drc:
                nr = r + dr
                nc = c + dc
                if in_range(nr, nc):
                    if board[nr][nc] in student:
                        fTmp += 1
                    if board[nr][nc] == 0:
                        eTmp += 1

            if fTmp > fCnt or (fTmp == fCnt and eTmp > eCnt):
                fCnt, eCnt = fTmp, eTmp
                pos[0], pos[1] = r, c

    board[pos[0]][pos[1]] = student[0]
    return


N = int(input())
drc = [(0, 1), (1, 0), (-1, 0), (0, -1)]
students = [list(map(int, input().split())) for _ in range(N * N)]
board = [[0] * N for _ in range(N)]
answer = 0
score = [0, 1, 10, 100, 1000]

for student in students:
    solution(student)

# print(*board, sep='\n')

students.sort(key=lambda x: x[0])

for r in range(N):
    for c in range(N):
        cnt = 0
        for dr, dc in drc:
            nr = r + dr
            nc = c + dc
            if in_range(nr, nc) and board[nr][nc] in students[board[r][c] - 1]:
                cnt += 1

        answer += score[cnt]

print(answer)