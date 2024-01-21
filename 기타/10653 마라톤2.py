import sys
from itertools import combinations

input = sys.stdin.readline


def get_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def solution():
    dp = [[0 for _ in range(N)] for _ in range(K + 1)]
    dis = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            dis[i][j] = get_distance(lst[i][0], lst[i][1], lst[j][0], lst[j][1])

    for i in range(1, N):
        dp[0][i] = dp[0][i - 1] + dis[i - 1][i]

    for k in range(1, K + 1):
        dp[k][k + 1] = dis[0][k + 1]  # k칸 뛰고, k+1칸까지 가는 거리는 0~k+1칸까지의 거리
        for n in range(k + 2, N):
            dp[k][n] = sys.maxsize
            for i in range(k + 1):
                dp[k][n] = min(dp[k][n], dp[k - i][n - i - 1] + dis[n - i - 1][n])

    return dp[-1][-1]


N, K = map(int, input().split())
lst = [tuple(map(int, input().split())) for _ in range(N)]
print(solution())
