import sys

from collections import defaultdict

input = sys.stdin.readline

'''
4 6 8 8 10 10 12 12 12 14 14 14 
'''


def solution():
    if dic[N]:
        return dic[N]

    grid = 2
    k = 0
    cnt = 1
    while k < N:
        k += cnt
        grid += 2
        if k >= N:
            break
        k += cnt
        grid += 2
        cnt += 1

    dic[N] = grid
    return grid


T = int(input())
dic = defaultdict(int)
for _ in range(T):
    N = int(input())
    print(solution())
