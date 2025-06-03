import sys
from itertools import combinations

input = sys.stdin.readline

answer = sys.maxsize
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
lst = [k for k in range(N)]

for numbers in list(combinations(lst, N // 2)):
    s_sum, l_sum = 0, 0
    for i in range(N):
        for j in range(N):
            if i == j:
                continue

            if i in numbers and j in numbers:
                s_sum += board[i][j]
            elif not i in numbers and j not in numbers:
                l_sum += board[i][j]

    answer = min(answer, abs(s_sum - l_sum))

print(answer)
