import sys

input = sys.stdin.readline


def recur(index, cur, type):
    if index == len(lst):
        return 1

    if cur == len(bridge[0]):
        return 0

    if dp[index][cur][type] != -1:
        return dp[index][cur][type]

    dp[index][cur][type] = 0
    if lst[index] == bridge[type][cur]:
        dp[index][cur][type] += recur(index + 1, cur + 1, 1 - type)

    dp[index][cur][type] += recur(index, cur + 1, type)
    return dp[index][cur][type]


lst = list(input().strip())
bridge = []
bridge.append(list(input().strip()))
bridge.append(list(input().strip()))
dp = [[[-1] * 2 for _ in range(101)] for _ in range(101)]
print(recur(0, 0, 0) + recur(0, 0, 1))
