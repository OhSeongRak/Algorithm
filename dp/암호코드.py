import sys

input = sys.stdin.readline


def solution():
    N = len(lst)
    dp = [0] * N
    dp[0], dp[1] = 1, 1

    if lst[1] == 0:
        return 0

    for i in range(2, N):
        if lst[i] != 0:  # lst[i]로만 숫자를 만들 수 있으므로 dp[i-1]만큼 가능
            dp[i] += dp[i - 1]
        if 10 <= 10 * lst[i - 1] + lst[i] <= 26:  # lst[i-1] lst[i]로 숫자를 만들 수 있으므로 dp[i-2]만큼 가능
            dp[i] += dp[i - 2]

    # return dp
    return dp[-1] % 1000000


lst = [-1] + list(map(int, input().strip()))
print(solution())