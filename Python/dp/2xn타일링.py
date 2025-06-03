def solution():
    for i in range(3, N+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[N] % 10007

N = int(input())
dp = [1] * 1010
dp[2] = 2
print(solution())
