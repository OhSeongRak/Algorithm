import sys

input = sys.stdin.readline

'''
터질폭탄 -1, 설치폭탄 1, 빈공간 0
'''


def in_range(r, c):
    if 0 <= r < R and 0 <= c < C:
        return True
    return False


def solution():
    for i in range(R):
        for j in range(C):
            if board[i][j] == '.':
                board[i][j] = 0
            else:
                board[i][j] = -1

    for count in range(N - 1):
        if count % 2 == 0:
            # 설치
            for r in range(R):
                for c in range(C):
                    if board[r][c] == 0:
                        board[r][c] = 1
        else:
            # 폭발
            tmp = [[board[r][c] for c in range(C)] for r in range(R)]
            for r in range(R):
                for c in range(C):
                    if board[r][c] != -1:
                        continue

                    tmp[r][c] = 0
                    if in_range(r - 1, c):
                        tmp[r - 1][c] = 0
                    if in_range(r, c - 1):
                        tmp[r][c - 1] = 0
                    if in_range(r + 1, c):
                        tmp[r + 1][c] = 0
                    if in_range(r, c + 1):
                        tmp[r][c + 1] = 0

            for r in range(R):
                for c in range(C):
                    board[r][c] = -tmp[r][c]

    for r in range(R):
        for c in range(C):
            if board[r][c] == 1 or board[r][c] == -1:
                print('O', end="")
            else:
                print('.', end="")
        print()


R, C, N = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
solution()
