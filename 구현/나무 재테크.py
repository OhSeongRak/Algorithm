import sys
input = sys.stdin.readline


def spring():
    return


def summer():
    return


def autumn():
    return


def winter():
    return


def solution():

    return


# K년후 찾기
# A는 양분
N, M, K = map(int, input().split())
board = [[5] * N for _ in range(N)]
A = [list(map(int, input().split())) for _ in range(N)]
trees = []
for _ in range(M):
    r, c, age = map(int, input().split())
    trees.append([r-1, c-1, age])

solution()
# print(*A, sep='\n')
# print(*board, sep='\n')
# print(*trees, sep='\n')
