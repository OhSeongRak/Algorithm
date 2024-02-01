import sys

input = sys.stdin.readline


def solution():
    answer = 0
    dp = [[0 for _ in range(len(lst2) + 1)] for _ in range(len(lst1) + 1)]

    for i in range(1, len(lst1) + 1):
        for j in range(1, len(lst2) + 1):
            if lst1[i - 1] == lst2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            answer = max(answer, dp[i][j])

    return answer


lst1 = list(input().strip())
lst2 = list(input().strip())
print(solution())