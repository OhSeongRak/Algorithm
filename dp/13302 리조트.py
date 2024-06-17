import sys

input = sys.stdin.readline


def recur(cur, coupon):
    if cur > N:
        return 0

    if cur in lst:
        return recur(cur + 1, coupon)

    if dp[cur][coupon] != -1:
        return dp[cur][coupon]

    dp[cur][coupon] = min(recur(cur + 1, coupon) + 10000,
                          recur(cur + 3, coupon + 1) + 25000,
                          recur(cur + 5, coupon + 2) + 37000)

    if coupon >= 3:
        dp[cur][coupon] = min(recur(cur + 1, coupon - 3), dp[cur][coupon])

    return dp[cur][coupon]


N, M = map(int, input().split())
lst = list(map(int, input().split()))
dp = [[-1] * (N + 1) for _ in range(N + 1)]
print(recur(1, 0))
