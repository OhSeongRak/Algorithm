import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)


def recur(index, remain):
    global coins, dp

    if remain > sum(coins) // 2:
        return -10000000000

    if index == len(coins):
        return 0

    if dp[index][remain] == -1:
        dp[index][remain] = max(recur(index + 1, remain + coins[index]) + coins[index],
                                recur(index + 1, remain))

    return dp[index][remain]


def solution(lst):
    global coins, dp

    coins, dp = [], []
    for i in range(len(lst)):
        for _ in range(lst[i][1]):
            coins.append(lst[i][0])

    dp = [[-1] * (sum(coins) // 2 + 1) for _ in range(len(coins))]
    # return recur(0, 0)
    return 1 if recur(0, 0) == sum(coins) // 2 else 0


coins, dp = [], []
for _ in range(3):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    print(solution(lst))