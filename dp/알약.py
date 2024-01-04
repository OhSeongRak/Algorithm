import sys

input = sys.stdin.readline


def solution():
    dp = [[0 for _ in range((N + 1))] for _ in range(N + 1)]
    dp[N][0] = 1

    for w in range(N)[::-1]:
        for h in range(N - w + 1)[::-1]:
            if h + 1 <= N:
                dp[w][h] += dp[w][h + 1]
            if w + 1 <= N and h - 1 >= 0:
                dp[w][h] += dp[w + 1][h - 1]

    return dp[0][0]


N = int(input())
while N != 0:
    print(solution())
    N = int(input())
