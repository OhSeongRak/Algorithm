import sys

from itertools import permutations

input = sys.stdin.readline


def recur(i, j, k):
    if dp[i][j][k] != -1:
        return dp[i][j][k]

    dp[i][j][k] = sys.maxsize
    for attack in permutations([1, 3, 9], 3):
        f, s, t = max(0, i - attack[0]), max(0, j - attack[1]), max(0, k - attack[2])
        dp[i][j][k] = min(dp[i][j][k], recur(f, s, t) + 1)

    return dp[i][j][k]


dp = [[[-1] * 61 for _ in range(61)] for _ in range(61)]
dp[0][0][0] = 0
N = int(input())
SCV = list(map(int, input().split()))
SCV.extend([0, 0])
recur(SCV[0], SCV[1], SCV[2])
print(dp[SCV[0]][SCV[1]][SCV[2]])
