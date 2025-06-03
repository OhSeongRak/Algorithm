import sys

input = sys.stdin.readline


def solution():
    njh = [[0 for c in range(C + 1)] for r in range(R + 1)]

    # 가로
    for r in range(R):
        for c in range(C):
            njh[r + 1][c + 1] += board[r][c] + njh[r + 1][c]

    # 세로
    for c in range(C):
        for r in range(R):
            njh[r + 1][c + 1] += njh[r][c + 1]

    for r1, c1, r2, c2 in pos:
        total = njh[r2][c2] - njh[r2][c1 - 1] - njh[r1 - 1][c2] + njh[r1 - 1][c1 - 1]
        total //= ((r2 - r1 + 1) * (c2 - c1 + 1))
        print(total)

    # print(*njh, sep='\n')
    return


R, C, Q = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
pos = []
for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    pos.append([r1, c1, r2, c2])
solution()
