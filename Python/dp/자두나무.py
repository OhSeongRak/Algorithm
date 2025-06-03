import sys

input = sys.stdin.readline


def solution():
    dp = [[0 for _ in range(T)] for _ in range(W + 1)]

    cnt = 0
    for i in range(T): # 움직임 횟수가 0일 경우 값 초기화
        if lst[i] == 1:
            cnt += 1
        dp[0][i] = cnt

    for m in range(1, W + 1):
        dp[m][0] = 1 # 처음은 무조건 1
        cur = m % 2 + 1  # m번 움직인 후 있는 현재 위치
        for i in range(1, T):
            dp[m][i] = max(dp[m - 1][i], dp[m][i - 1])
            if lst[i] == cur:
                dp[m][i] += 1

    return dp[-1][-1]


T, W = map(int, input().split())
lst = []
for _ in range(T):
    lst.append(int(input()))
print(solution())
