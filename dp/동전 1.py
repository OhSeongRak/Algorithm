import sys

input = sys.stdin.readline


def solution():
    dp = [0] * (K + 1)

    for coin in coins:
        if coin > K:
            continue
        dp[coin] += 1
        for i in range(K + 1 - coin):
            dp[i + coin] += dp[i]

    return dp[K]


N, K = map(int, input().split())
coins = []
for _ in range(N):
    coins.append(int(input()))
print(solution())
