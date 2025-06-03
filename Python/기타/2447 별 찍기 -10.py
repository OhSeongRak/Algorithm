import sys

input = sys.stdin.readline


def recur(size, r, c):
    if size == 3:
        for i in range(3):
            for j in range(3):
                if i == j == 1:
                    continue
                board[r + i][c + j] = '*'
        return

    for i in range(9):
        if i == 4:
            continue
        recur(size // 3, r + (i // 3) * size // 3, c + (i * size // 3) % size)

    return


N = int(input())
board = [[' '] * N for _ in range(N)]
recur(N, 0, 0)
for r in range(N):
    for c in range(N):
        print(board[r][c], end='')
    print()
