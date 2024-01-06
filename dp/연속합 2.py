import sys

input = sys.stdin.readline


def solution():
    dp1, dp2 = [0] * N, [0] * N
    dp1[0] = dp2[0] = lst[0]

    for i in range(1, N):  # 연속합 구하기
        dp1[i] = max(dp1[i - 1] + lst[i], lst[i])

    for i in range(1, N):  # 최대 1개 제외 연속합 구하기
        dp2[i] = max(dp1[i - 1], dp2[i - 1] + lst[i])

    return max(max(dp2), max(dp1))


N = int(input())
lst = list(map(int, input().split()))
print(solution())
