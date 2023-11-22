import sys
input = sys.stdin.readline


def play():
    result = [0] * M

    for i in range(M):
        canGo = False
        for dir in [1, 0, -1]:
            c = i
            for r in range(N):
                if ladder[r][c] == -1:
                    c -= 1
                elif ladder[r][c] == 1:
                    c += 1
                elif ladder[r][c] == 2:
                    if c + dir < 0 or c + dir >= M:
                        break
                    result[c] = dir
                    c += dir
            else:
                if i == order[c]:
                    canGo = True
                    break

        if not canGo:
            return False

    for i in range(1, M):
        if result[i-1] == 1 and result[i] == -1:
            print("-", end='')
        else:
            print("*", end='')

    return True


def solution():
    # 알파벳 순서를 숫자로
    for i in range(M):
        order[i] = ord(order[i]) - ord('A')

    # 좌: -1, 우: 1, ?: 2
    for i in range(N):
        for j in range(M-1):
            if board[i][j] == '-':
                ladder[i][j] = 1
                ladder[i][j+1] = -1
            elif board[i][j] == '?':
                ladder[i][j] = 2
                ladder[i][j+1] = 2

    if not play():
        for _ in range(M-1):
            print("x", end='')


M = int(input())
N = int(input())
order = list(input().rstrip())
board = [list(input().rstrip()) for _ in range(N)]
ladder = [[0] * M for _ in range(N)]

solution()