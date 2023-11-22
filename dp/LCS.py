import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline


def solution():

    for i in range(1, R):
        for j in range(1, C):
            if lst1[j] == lst2[i]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    ans = ""
    end = C-1
    for i in range(1, R)[::-1]:
        for j in range(1, end)[::-1]:
            if dp[i-1][j] < dp[i][j] and dp[i][j-1] < dp[i][j]:
                ans = lst1[j] + ans
                end = j
                break


    return ans

lst1 = [0] + list(input().rstrip())
lst2 = [0] + list(input().rstrip())
R, C = len(lst2), len(lst1)
dp = [[0] * C for _ in range(R)]
print(solution())
