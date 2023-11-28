import sys

input = sys.stdin.readline


def solution():

    dp = board[:]

    for i in range(1, N):
        for j in range(1, M):
            if dp[i][j] == 0:
                continue
            dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])

    line = 0
    for i in range(N):
        for j in range(M):
            line = max(line, dp[i][j])

    return line * line


N, M = map(int, input().split())
board = [list(map(int, input().strip())) for _ in range(N)]
# print(*board, sep='\n')
print(solution())
