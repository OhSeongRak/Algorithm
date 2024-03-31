import sys

input = sys.stdin.readline


def recur(cur, total):
    if T < total:
        return -9999999999

    if cur == N:
        return 0

    if dp[cur][total] != -1:
        return dp[cur][total]

    dp[cur][total] = max(recur(cur + 1, total + K[cur]) + S[cur]
                         , recur(cur + 1, total))

    return dp[cur][total]


N, T = map(int, input().split())
K, S = [], []
for _ in range(N):
    k, s = map(int, input().split())
    K.append(k)
    S.append(s)

dp = [[-1] * 10001 for _ in range(N)]
print(recur(0, 0))
