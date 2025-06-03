import sys
from collections import defaultdict

input = sys.stdin.readline

def solution():
    if 1 in dic.keys():
        dp[1][dic[1]][1] = 1
    else:
        for i in [0, 1, 2]:
            dp[1][i][1] = 1

    for day in range(2, N + 1):
        if day in dic.keys(): # 현재 날짜의 먹을 파스타가 정해져 있다면
            type = dic[day]
            # 전 날의 현재와 다른 종류 파스타 더하기 (1개 연속 & 2개 연속)
            dp[day][type][1] += dp[day - 1][(type + 1) % 3][1] + dp[day - 1][(type + 2) % 3][1]
            dp[day][type][1] += dp[day - 1][(type + 1) % 3][2] + dp[day - 1][(type + 2) % 3][2]

            # 전 날의 현재와 같은 종류 파스타 더하기 (1개 연속)
            dp[day][type][2] += dp[day - 1][type][1]
            continue

        for type in range(3):
            dp[day][type][1] += dp[day - 1][(type + 1) % 3][1] + dp[day - 1][(type + 2) % 3][1]
            dp[day][type][1] += dp[day - 1][(type + 1) % 3][2] + dp[day - 1][(type + 2) % 3][2]
            dp[day][type][2] += dp[day - 1][type][1]

    answer = 0
    for i in range(3):
        for j in range(1, 3):
            answer += dp[N][i][j]

    return answer % 10000


N, K = map(int, input().split())
dic = defaultdict(int)
for _ in range(K):
    a, b = map(int, input().split())
    dic[a] = b - 1

dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(N + 1)]
print(solution())
