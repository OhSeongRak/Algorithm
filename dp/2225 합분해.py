import sys

input = sys.stdin.readline


# top-down
def recur(index, total):
    if total > N:
        return 0

    if index == K:
        if total == N:
            return 1
        return 0

    if dp[index][total] != -1:
        return dp[index][total]

    dp[index][total] = 0
    for i in range(N + 1):
        dp[index][total] += recur(index + 1, total + i)

    dp[index][total] %= 1_000_000_000
    return dp[index][total]


# bottom-up
def solution():
    dp = [[1] * (N + 1) for _ in range(K + 1)]

    for k in range(2, K + 1):
        for n in range(N + 1):
            tmp = 0
            for i in range(n + 1):
                tmp += dp[k - 1][i]
            dp[k][n] = tmp

    return dp[-1][-1] % 1_000_000_000


N, K = map(int, input().split())
dp = [[-1] * 201 for _ in range(201)]
# print(recur(0, 0))
print(solution())
