import sys

input = sys.stdin.readline


def recur(cur, door1, door2):
    if cur == size:
        return 0

    if dp[cur][door1][door2] != -1:
        return dp[cur][door1][door2]

    dp[cur][door1][door2] = min(recur(cur + 1, use[cur], door2) + abs(use[cur] - door1),
                                recur(cur + 1, door1, use[cur]) + abs(use[cur] - door2))

    return dp[cur][door1][door2]


N = int(input())
door1, door2 = map(int, input().split())
size = int(input())
use = []
for _ in range(size):
    use.append(int(input()))

dp = [[[-1] * (N + 1) for _ in range(N + 1)] for _ in range(size)]
print(recur(0, door1, door2))
