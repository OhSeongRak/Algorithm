import sys

input = sys.stdin.readline


def recur(l, r):
    if l + r == 3 * N:
        return 0

    if dp[l][r] != -1:
        return dp[l][r]

    count = l + r
    if pill[count % 3] == lst[l] and pill[count % 3] == lst[-r - 1]:
        dp[l][r] = max(recur(l + 1, r), recur(l, r + 1)) + 1
    elif pill[count % 3] == lst[l]:
        dp[l][r] = recur(l + 1, r) + 1
    elif pill[count % 3] == lst[-r - 1]:
        dp[l][r] = recur(l, r + 1) + 1
    else:
        dp[l][r] = 0

    return dp[l][r]


pill = ['B', 'L', 'D']
N = int(input())
lst = list(input().strip())
dp = [[-1 for _ in range(3 * N)] for _ in range(3 * N)]
recur(0, 0)
print(dp[0][0])
