import sys

input = sys.stdin.readline


def LIS4():
    dp = [[-1, 1] for _ in range(N)] # [내 이전 인덱스, 나를 포함한 가장 긴 길이]

    for me in range(N):
        for cur in range(me):
            if lst[cur] < lst[me] and dp[me][1] < dp[cur][1] + 1:
                dp[me][1] = dp[cur][1] + 1
                dp[me][0] = cur

    answer = 0
    index = 0
    for i in range(N):
        if answer < dp[i][1]:
            answer = dp[i][1]
            index = i

    print(answer)
    tmp = []

    while True:
        tmp.append(lst[index])
        if dp[index][0] == -1:
            break
        index = dp[index][0]


    for k in tmp[::-1]:
        print(k, end=' ')

    return


N = int(input())
lst = list(map(int, input().split()))
LIS4()

