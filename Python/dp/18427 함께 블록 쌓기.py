import sys

input = sys.stdin.readline


def recur(index, height):
    if height == H:
        return 1

    if index == N:
        return 0

    if height > H:
        return 0

    if dp[index][height] == -1:
        dp[index][height] = recur(index + 1, height)
        for h in lst[index]:
            dp[index][height] += recur(index + 1, height + h)

    return dp[index][height] % 10007


N, M, H = map(int, input().split())
lst = [sorted(list(map(int, input().split()))) for _ in range(N)]
dp = [[-1 for _ in range(H + 1)] for _ in range(N)]
print(recur(0, 0))
