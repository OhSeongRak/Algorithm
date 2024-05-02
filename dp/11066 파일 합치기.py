import sys

from heapq import heappush, heappop, heapify

input = sys.stdin.readline


def solution():
    # dp[i][j] : j번째부터 뒤로 i개의 파일을 합치는데에 드는 최소 비용
    dp = [[0] * N for _ in range(N + 1)]

    for i in range(2, N + 1):
        for j in range(N + 1 - i):
            tmp = sys.maxsize
            for k in range(1, i):
                tmp = min(tmp, dp[k][j] + dp[i - k][j + k])
            dp[i][j] = tmp + sum(lst[j:j + i])

    return dp[N][0]


T = int(input())
for _ in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    print(solution())
