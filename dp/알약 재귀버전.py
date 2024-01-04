import sys

sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

'''
완탐인 경우
- recur(반알 개수, 한알 개수):
'''


def recur(whole, half):
    if half < 0 or half > N or whole < 0 or whole > N:
        return 0

    if dp[half][whole] != 0:
        return dp[whole][half]

    dp[whole][half] = recur(whole, half + 1) + recur(whole + 1, half - 1)
    return dp[whole][half]


N = int(input())
while N != 0:
    total = 0
    dp = [[0 for _ in range((N + 1))] for _ in range(N + 1)]
    dp[N][0], dp[0][N] = 1, 1
    recur(0, 0)
    print(*dp, sep='\n')
    N = int(input())
