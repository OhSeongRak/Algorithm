import sys

input = sys.stdin.readline


def count(r, c, size):
    ret = 0
    for i in range(r, r + size):
        for j in range(c, c + size):
            ret += board[i][j]

    return ret


def divide(r, c, size):
    global white, blue

    total = count(r, c, size)
    if total == 0:
        white += 1
        return

    if total == size * size:
        blue += 1
        return

    divide(r, c, size // 2)
    divide(r + size // 2, c, size // 2)
    divide(r, c + size // 2, size // 2)
    divide(r + size // 2, c + size // 2, size // 2)

    return


N = int(input())
white, blue = 0, 0
board = [list(map(int, input().split())) for _ in range(N)]
divide(0, 0, N)
print(white)
print(blue)
