import sys
input = sys.stdin.readline

def solution():
    for i in range(N):
        for j in range(i):
            if boxes[j] < boxes[i] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
    
    return max(dp)

N = int(input())
boxes = list(map(int, input().split()))
dp = [1] * N
print(solution())
