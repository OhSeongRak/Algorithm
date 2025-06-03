import sys

input = sys.stdin.readline


def solution():
    # dp = [[0 for _ in range(3)] for _ in range(N)]
    # for i in range(3):
    #     dp[0][i] = lst[0][i]

    dp_max, dp_min = lst[0][:], lst[0][:]
    max_result, min_result = lst[0][:], lst[0][:]

    for i in range(1, N):
        max_result[0] = lst[i][0] + max(dp_max[0], dp_max[1])
        max_result[1] = lst[i][1] + max(dp_max[0], dp_max[1], dp_max[2])
        max_result[2] = lst[i][2] + max(dp_max[1], dp_max[2])
        dp_max = max_result[:]

        min_result[0] = lst[i][0] + min(dp_min[0], dp_min[1])
        min_result[1] = lst[i][1] + min(dp_min[0], dp_min[1], dp_min[2])
        min_result[2] = lst[i][2] + min(dp_min[1], dp_min[2])
        dp_min = min_result[:]

    print(max(max_result), end=" ")
    print(min(min_result))
    return

N = int(input())
lst = []
for _ in range(N):
    lst.append(list(map(int, input().split())))

solution()
