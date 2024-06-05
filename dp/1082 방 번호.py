import sys

input = sys.stdin.readline


# 재귀 완전 탐색 ver
def recur(cur, total):
    global answer

    if total <= M:
        answer = max(answer, cur)
    else:
        return

    for i in range(N)[::-1]:
        recur(cur * 10 + i, total + cost[i])

    return


def solution():
    dp = [0] * (M + 1)

    for i in range(1, M + 1):
        for room_number in range(N):
            if cost[room_number] <= i:
                dp[i] = max(dp[i], dp[i - cost[room_number]] * 10 + room_number)

    return max(dp)


N = int(input())
cost = list(map(int, input().split()))
M = int(input())
print(solution())
