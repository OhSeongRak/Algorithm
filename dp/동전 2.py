import sys

input = sys.stdin.readline


def solution():
    MAX_SIZE = 10001
    dp = [MAX_SIZE] * (K + 1)

    for coin in coins:
        if coin > K:
            continue
        dp[coin] = 1
        for i in range(K + 1 - coin):
            dp[i + coin] = min(dp[i] + 1, dp[i + coin])

    return dp[K] if dp[K] != MAX_SIZE else -1


N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
print(solution())
