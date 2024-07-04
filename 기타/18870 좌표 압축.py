import sys
from collections import defaultdict

input = sys.stdin.readline


def solution():
    global lst

    sorted_lst = list(set(lst))
    sorted_lst.sort()
    dic, ret = defaultdict(int), [0] * N

    for i in range(len(sorted_lst)):
        dic[sorted_lst[i]] = i

    for i in range(N):
        ret[i] = dic[lst[i]]

    for k in ret:
        print(k, end=' ')

    return


N = int(input())
lst = list(map(int, input().split()))
solution()
