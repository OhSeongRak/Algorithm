import sys

input = sys.stdin.readline


# def solution(info, N, M):
#     MAX_VALUE = 100000
#     dp = [[MAX_VALUE for _ in range(M + 1)] for _ in range(41)]
#
#     def recur(cur, m):
#         if m >= M:
#             return MAX_VALUE
#
#         if cur == len(info):
#             return 0
#
#         if dp[cur][m] != MAX_VALUE:
#             return dp[cur][m]
#
#         dp[cur][m] = min(recur(cur + 1, m) + info[cur][0], recur(cur + 1, m + info[cur][1]))
#
#         if dp[cur][m] >= N:
#             dp[cur][m] = MAX_VALUE
#             return MAX_VALUE
#
#         return dp[cur][m]
#
#     recur(0, 0)
#     if dp[0][0] == MAX_VALUE:
#         dp[0][0] = -1
#
#     return dp[0][0]


def solution(info, N, M):
    MAX_VALUE = 100000
    R = len(info)
    dp = [[MAX_VALUE for _ in range(M)] for _ in range(R)]

    dp[0][0] = info[0][0]
    if info[0][1] < M:
        dp[0][info[0][1]] = 0

    for r in range(1, R):
        for m in range(M - info[r][1]):  # m을 선택한 경우
            dp[r][m + info[r][1]] = dp[r - 1][m]

        for m in range(M):  # n을 선택한 경우z`
            dp[r][m] = min(dp[r][m], dp[r - 1][m] + info[r][0])

    # print(*dp, sep='\n')
    answer = min(dp[R - 1])
    if answer >= N:
        answer = -1
    return answer


if __name__ == "__main__":
    # N = int(input())
    # M = int(input())
    # info = list(map(int, input().split()))
    info = [[1, 2], [2, 3], [2, 1]]
    N, M = 4, 4

    solution(info, N, M)
