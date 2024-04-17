import sys

input = sys.stdin.readline


# top-down
# def recur(index):
#     if index == N:
#         return 0
#
#     if dp[index] != -1:
#         return dp[index]
#
#     dp[index] = 0
#     for i in range(index + 1, N + 1):
#         if dp[i] == -1:
#             dp[index] = max(dp[index], recur(i) + max(lst[index:i]) - min(lst[index:i]))
#         else:
#             dp[index] = max(dp[index], dp[i] + max(lst[index:i]) - min(lst[index:i]))
#
#     return dp[index]

# bottom-up
def solution():
    for i in range(1, N):
        dp[i] = max(lst[:i + 1]) - min(lst[:i + 1])
        for j in range(0, i):
            dp[i] = max(dp[i], dp[j] + max(lst[j + 1:i + 1]) - min(lst[j + 1:i + 1]))

    return dp[-1]


N = int(input())
lst = list(map(int, input().split()))
dp = [0] * N
print(solution())
# print(recur(0))
