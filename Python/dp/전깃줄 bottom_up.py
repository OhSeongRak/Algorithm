import sys
input = sys.stdin.readline

def solution():
    for i in range(1, 501):
        for j in range(1, 501):
            dp[i][j] = max(dp[i][j-1] + dp[i][j], dp[i-1][j]) 

    return N - dp[500][500]

N = int(input())
dp = [[0] * (501) for _ in range(501)]
for _ in range(N):
    a, b = map(int, input().split())
    dp[a][b] += 1

print(solution())