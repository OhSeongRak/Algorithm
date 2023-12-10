import sys

input = sys.stdin.readline


def solution():
    dp = [[0 for _ in range(21)] for _ in range(N - 1)]
    dp[0][lst[0]] = 1

    for i in range(1, N - 1):
        for j in range(21):
            if dp[i - 1][j] == 0:
                continue

            plus = j + lst[i]
            minus = j - lst[i]

            if plus <= 20:
                dp[i][plus] += dp[i - 1][j]

            if minus >= 0:
                dp[i][minus] += dp[i - 1][j]

    return dp[-1][lst[-1]]


N = int(input())
lst = list(map(int, input().split()))
print(solution())

'''
11
8 3 2   4    8   7   2   4   0   8   8

11  9   5
        13
    13  9
        17
5   3   -
        7
    7   3
        11
        
        
dp[i][j] = i번째 수까지 계산하고 값이 j인 수
합 또는 차가 0보다 크고 20보다 작아야하니 계산하기 쉬워짐
'''
