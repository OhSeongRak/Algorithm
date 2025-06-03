import sys

input = sys.stdin.readline


def LIS():
    dp = [1] * N

    for end in range(N):
        for cur in range(end + 1):
            if lst[cur] < lst[end]:
                dp[end] = max(dp[cur] + 1, dp[end])

    return N - max(dp)


N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
print(LIS())
