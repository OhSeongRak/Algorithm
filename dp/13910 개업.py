import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


def recur(cur):
    if cur > N:
        return 100000

    if cur == N:
        return 0

    if dp[cur] != -1:
        return dp[cur]

    dp[cur] = 100000
    for i in range(M):
        dp[cur] = min(recur(cur + S[i]) + 1, dp[cur])
        for j in range(i + 1, M):
            dp[cur] = min(recur(cur + S[i] + S[j]) + 1, dp[cur])

    return dp[cur]


N, M = map(int, input().split())
S = list(map(int, input().split()))
dp = [-1] * N
recur(0)
print(-1) if dp[0] == 100000 else print(dp[0])
