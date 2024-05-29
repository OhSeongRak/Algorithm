import sys

input = sys.stdin.readline


def top_down(cur, hp):
    if hp <= 0:
        return -999999999

    if cur == N:
        return 0

    if dp[cur][hp] != -1:
        return dp[cur][hp]

    dp[cur][hp] = max(top_down(cur + 1, hp),
                      top_down(cur + 1, hp - hello[cur]) + happy[cur])

    return dp[cur][hp]


def bottom_up():
    dp = [[0] * 101 for _ in range(20)]

    for i in range(1, 101):
        if i > hello[0]:
            dp[0][i] = happy[0]

    for i in range(1, N):
        for hp in range(1, 101):
            if hello[i] < hp:
                dp[i][hp] = max(dp[i - 1][hp], dp[i - 1][hp - hello[i]] + happy[i])
            else:
                dp[i][hp] = dp[i - 1][hp]

    return dp[N - 1][100]


N = int(input())
dp = [[-1] * 101 for _ in range(20)]
hello = list(map(int, input().split()))
happy = list(map(int, input().split()))
# print(top_down(0, 100))
print(bottom_up())
