import sys
input = sys.stdin.readline

def solution(N, k):
    # dp[k][N][e]
    # k: 인접한 비트의 개수가 k인 개수
    # N: 비트의 길이
    # e: 0 or 1. 로 끝나는 비트의 개수
    dp = [[[0] * 2 for _ in range(N+1)] for _ in range(k+1)]

    # dp[0][1][0]: 인접비트 0개, 비트 길이 1, 마지막 비트 = 0
    # dp[0][1][1]: 인접비트 0개, 비트 길이 1, 마지막 비트 = 1
    dp[0][1][0], dp[0][1][1] = 1, 1

    # 인접 비트 0개인 경우
    # dp[0][i][0] : 마지막 비트와 상관없이 길이가 i-1인 비트에 0을 붙이면 됨
    # dp[0][i][1] : 마지막 비트가 0인 길이가 i-1인 비트에 1을 붙이면 됨
    for i in range(2, N+1):
        dp[0][i][0] = dp[0][i-1][0] + dp[0][i-1][1]
        dp[0][i][1] = dp[0][i-1][0]

    # dp[r][c][0]: 인접 비트가 r개이고, 길이가 c-1인 비트에 0을 붙이면 됨
    # dp[r][c][1]: 인접 비트가 r개, 길이가 c-1인 비트, 마지막 비트가 0인 비트에 1을 붙이기 + 
    # 인접 비트가 r-1개, 길이가 c-1인 비트, 마지막 비트가 1인 비트에 1을 붙이기 (인접 비트가 1개 증가함) 
    for r in range(1, k+1):
        for c in range(r+1, N+1):
            dp[r][c][0] = dp[r][c-1][0] + dp[r][c-1][1]
            dp[r][c][1] = dp[r][c-1][0] + dp[r-1][c-1][1]

    # 인접 비트: k, 길이: N, 마지막 비트: 0 and 1 인 비트의 개수
    return dp[k][N][0] + dp[k][N][1]

T = int(input())
for _ in range(T):
    N, k = map(int, input().split())
    print(solution(N, k))