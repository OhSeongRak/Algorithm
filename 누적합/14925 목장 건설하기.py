import sys

input = sys.stdin.readline


def solution():
    dp = [[0] * C for _ in range(R)]

    for r in range(R):
        if board[r][0] == 0:
            dp[r][0] = 1
    for c in range(C):
        if board[0][c] == 0:
            dp[0][c] = 1

    for r in range(1, R):
        for c in range(1, C):
            if board[r][c] != 0:
                continue
            dp[r][c] = 1 + min(dp[r - 1][c], dp[r][c - 1], dp[r - 1][c - 1])

    answer = 0
    for r in range(R):
        answer = max(answer, max(dp[r]))

    return answer


R, C = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]
# print(solution())
