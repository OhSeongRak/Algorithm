import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def recur(cur, jump):
    if cur > N or jump == 0 or cur in small:
        return 10010

    if cur == N:
        return 0

    if dp[cur][jump] != 10010:
        return dp[cur][jump]

    dp[cur][jump] = min(dp[cur][jump], recur(cur + jump - 1, jump - 1) + 1)
    dp[cur][jump] = min(dp[cur][jump], recur(cur + jump, jump) + 1)
    dp[cur][jump] = min(dp[cur][jump], recur(cur + jump + 1, jump + 1) + 1)

    return dp[cur][jump]


N, M = map(int, input().split())
dp = [[10010] * 200 for _ in range(N + 1)]
small = [int(input()) for _ in range(M)]
print(recur(2, 1) + 1)
