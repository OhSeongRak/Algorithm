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


T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    K = int(input())
    print(solution())
