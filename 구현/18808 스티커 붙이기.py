import sys

input = sys.stdin.readline


def fit(stiker, r, c):
    R, C = len(stiker), len(stiker[0])

    for i in range(R):
        for j in range(C):
            if board[i + r][j + c] == stiker[i][j] == 1:
                return False

    for i in range(R):
        for j in range(C):
            if stiker[i][j] == 1:
                board[i + r][j + c] = 1

    return True


def find(stiker):
    R, C = len(stiker), len(stiker[0])

    for r in range(N - R + 1):
        for c in range(M - C + 1):
            if fit(stiker, r, c):
                return True

    return False


def rotate(stiker):
    return list(zip(*stiker[::-1]))


def solution():
    for stiker in stikers:
        for _ in range(4):
            if find(stiker):
                break
            stiker = rotate(stiker)

    answer = 0
    for i in range(N):
        for j in range(M):
            if board[i][j] == 1:
                answer += 1
    return answer


N, M, K = map(int, input().split())
board = [[0] * M for _ in range(N)]
stikers = []
for _ in range(K):
    R, C = map(int, input().split())
    stikers.append([list(map(int, input().split())) for _ in range(R)])

print(solution())
