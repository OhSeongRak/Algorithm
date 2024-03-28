import sys

input = sys.stdin.readline

dp = [1] * 1_000_001
MOD = 1_000_000_009

for num in [2, 3]:
    for i in range(num, 1_000_001):
        dp[i] = 0
        for j in range(1, num + 1):
            dp[i] += dp[i - j]
        dp[i] %= MOD

T = int(input())
for _ in range(T):
    print(dp[int(input())])
