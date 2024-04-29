import sys, math

input = sys.stdin.readline


def bottom_up():
    dp = [[0] * (K + 1) for _ in range(N + 1)]  # i개 종류의 색 사용, j개의 색 선택 가능한 경우의 수

    for i in range(N + 1):
        for j in range(K + 1):
            if j == 0:
                dp[i][j] = 1
            elif j == 1:
                dp[i][j] = i
            else:
                dp[i][j] += dp[i - 1][j] + dp[i - 2][j - 1]
                dp[i][j] %= MOD

    # 처음과 끝이 만나면 안되니까
    # N번째 선택 안하고 K개 뽑는 경우 : dp[N - 1][K]
    # N번째 하고 K-1개 뽑는 경우(N-3개에서 K-1개 뽑는 경우) : dp[N - 3][K - 1]
    return (dp[N - 1][K] + dp[N - 3][K - 1]) % MOD


MOD = 1_000_000_003
N = int(input())
K = int(input())
print(bottom_up())
