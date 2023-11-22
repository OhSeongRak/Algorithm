import sys
input = sys.stdin.readline

def solution(lst):

    coins, dp = [], []
    for i in range(len(lst)):
        for _ in range(lst[i][1]):
            coins.append(lst[i][0])

    for i in range(2, sum(coins) // 2 + 1):
        dp[i] 

    dp = [[-1] * (sum(coins) // 2 + 1) for _ in range(len(coins))]
    # return 


for _ in range(3):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    print(solution(lst))