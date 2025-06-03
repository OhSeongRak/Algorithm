import sys

input = sys.stdin.readline


def in_range(r, c):
    if r < 0 or r >= N or c < 0 or c >= N or board[r][c] == 1:
        return False
    return True


def solution():
    dp = [[[0 for _ in range(N)] for _ in range(N)] for _ in range(3)]
    dp[0][0][1] = 1

    for r in range(N):
        for c in range(N):
            if board[r][c] == 1:
                continue
            for type in range(3):
                if type == 0:
                    if not in_range(r, c - 1):
                        continue
                    dp[type][r][c] += dp[0][r][c - 1] + dp[2][r][c - 1]

                if type == 1:
                    if not in_range(r - 1, c):
                        continue
                    dp[type][r][c] += dp[1][r - 1][c] + dp[2][r - 1][c]

                if type == 2:
                    if not in_range(r - 1, c) or not in_range(r, c - 1) or not in_range(r - 1, c - 1):
                        continue
                    dp[type][r][c] += dp[0][r - 1][c - 1] + dp[1][r - 1][c - 1] + dp[2][r - 1][c - 1]


    return dp[0][-1][-1] + dp[1][-1][-1] + dp[2][-1][-1]


dr = [[0, 1], [1, 1], [0, 1, 1]]
dc = [[1, 1], [0, 1], [1, 0, 1]]
# dr = [[0, -1], [-1, -1], [0, -1, -1]]
# dc = [[-1, -1], [0, -1], [-1, 0, -1]]
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
# print(*board, sep='\n')
print(solution())
