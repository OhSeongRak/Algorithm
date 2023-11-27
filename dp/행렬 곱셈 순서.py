import sys

input = sys.stdin.readline

'''
dp[i][j] = i~j 범위의 최소 연산 수
'''


def solution():
    MAX_VALUE = sys.maxsize
    dp = [[MAX_VALUE for _ in range(N)] for _ in range(N)]
    for i in range(N):
        dp[i][i] = 0

    for size in range(1, N):
        for start in range(N):
            if start + size == N:
                break
            for k in range(start, start + size):
                dp[start][start + size] = min(dp[start][start + size],
                                              dp[start][k] + dp[k + 1][start + size] + matrix[start][0] * matrix[k][1] *
                                              matrix[start + size][1])

    # print(*dp, sep='\n')
    return dp[0][N - 1]


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
print(solution())
