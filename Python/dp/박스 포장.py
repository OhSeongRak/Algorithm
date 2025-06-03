import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def recur(idx, weight):
    if idx == N:
        return 0

    if dp[idx][weight] == -1:
        if weight < boxes[idx]: # 첫째꺼 넣기
            dp[idx][weight] = max(recur(idx + 1, boxes[idx]) + 1, recur(idx + 1, weight))
            return dp[idx][weight]
        else:
            dp[idx][weight] = recur(idx + 1, weight) # 안넣기
            return dp[idx][weight]
    else:
        return dp[idx][weight]

N = int(input())
boxes = list(map(int, input().split()))
dp = [-1] * N
print(recur(0, 0))
# print(answer)
