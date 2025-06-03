import sys

input = sys.stdin.readline

T = int(input())
MOD = 1000000007

dp = [0] * 5001
dp[0], dp[2] = 1, 1

for i in range(4, 5001, 2):
    for j in range(0, i, 2):
        dp[i] += dp[j] * dp[i - j - 2]
        dp[i] %= MOD

for _ in range(T):
    print(dp[int(input())])
