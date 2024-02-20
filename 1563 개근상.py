import sys

input = sys.stdin.readline


def recur(size, late, absent):
    if late >= 2:
        return 0

    if absent == 3:
        return 0

    if size == N:
        return 1

    if dp[size][late][absent] != -1:
        return dp[size][late][absent]

    dp[size][late][absent] = recur(size + 1, late, 0) + recur(size + 1, late + 1, 0) + recur(size + 1, late, absent + 1)

    return dp[size][late][absent]


N = int(input())
dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(N)]
print(recur(0, 0, 0) % 1000000)
