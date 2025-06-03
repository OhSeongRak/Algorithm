import sys

input = sys.stdin.readline


def solution():
    # dp[w][h]
    dp = [[0 for _ in range((N + 1))] for _ in range(N + 1)]
    dp[N][0] = 1

    for w in range(N)[::-1]:
        for h in range(N - w + 1)[::-1]:
            if h + 1 <= N:
                dp[w][h] += dp[w][h + 1]
            if w + 1 <= N and h - 1 >= 0:
                dp[w][h] += dp[w + 1][h - 1]

    return dp[0][0]


def solution2():
    # dp[h][w]
    dp = [[0 for _ in range(31)] for _ in range(31)]

    for i in range(1, 31):
        dp[0][i] = 1

    for h in range(1, 31):
        for w in range(h, 31):
            dp[h][w] += dp[h - 1][w] + dp[h][w - 1]

    return dp[N][N]

N = int(input())
while N != 0:
    print(solution2())
    N = int(input())
