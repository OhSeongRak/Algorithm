import sys

input = sys.stdin.readline


def solution():
    for c in range(M):
        board[0][c] += grow[c + M - 1]
    for r in range(1, M)[::-1]:
        board[r][0] += grow[M - 1 - r]

    for r in range(1, M):
        for c in range(1, M):
            board[r][c] = board[r - 1][c]

    for r in range(M):
        for c in range(M):
            print(board[r][c], end=' ')
        print()

    return


M, N = map(int, input().split())
board = [[1] * M for _ in range(M)]
grow = [0] * (2 * M - 1)
for _ in range(N):
    z, o, t = map(int, input().split())
    index = z
    for _ in range(o):
        grow[index] += 1
        index += 1
    for _ in range(t):
        grow[index] += 2
        index += 1

solution()
