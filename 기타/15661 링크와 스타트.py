import math
import sys

from itertools import combinations

input = sys.stdin.readline


def solution():
    for i in range(2, math.floor(N // 2) + 1):
        for lst in combinations(range(N), i):
            for k in range(N):
                1
    return


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
answer = sys.maxsize
print(solution())
