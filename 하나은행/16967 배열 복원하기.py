import sys

input = sys.stdin.readline


def solution():
    A = [[B[r][c] for c in range(C)] for r in range(R)]

    for r in range(X, R):
        for c in range(Y, C):
            A[r][c] -= A[r - X][c - Y]

    for r in range(R):
        for c in range(C):
            print(A[r][c], end=" ")
        print()

    return


R, C, X, Y = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(R + X)]
solution()
