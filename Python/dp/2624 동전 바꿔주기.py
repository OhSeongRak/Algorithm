import sys

input = sys.stdin.readline


def top_down(index, total):
    if total == T:
        return 1

    if total > T or index == K:
        return 0

    if dp[index][total] != -1:
        return dp[index][total]

    dp[index][total] = 0
    for i in range(coins[index][1] + 1):
        dp[index][total] += top_down(index + 1, total + coins[index][0] * i)

    return dp[index][total]


def bottom_up():
    dp = [0] * (T + 1)
    dp[0] = 1

    for n, k in coins:
        for i in range(T + 1)[::-1]:  # 뒤에서부터
            for j in range(1, k + 1):  # 동전 몇개 쓸건지
                if i - n * j < 0:
                    break
                dp[i] += dp[i - n * j]

    return dp[-1]


T = int(input())
K = int(input())
coins = [list(map(int, input().split())) for _ in range(K)]
print(bottom_up())
dp = [[-1] * (T + 1) for _ in range(1001)]
# print(top_down(0, 0))
