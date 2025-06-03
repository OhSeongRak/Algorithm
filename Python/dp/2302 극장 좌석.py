import sys

input = sys.stdin.readline


def solution():
    dp = [1] * 41
    for i in range(2, 41):
        dp[i] = dp[i - 1] + dp[i - 2]

    answer = 1
    for i in range(1, M + 2):
        answer *= dp[lst[i] - lst[i - 1] - 1]

    return answer


N = int(input())
M = int(input())
lst = [0] + [int(input()) for _ in range(M)] + [N + 1]
print(solution())
