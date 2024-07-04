import sys
from collections import defaultdict

input = sys.stdin.readline


def solution():
    sorted_lst = sorted(list(set(lst)))
    dic = defaultdict(int)

    for i in range(len(sorted_lst)):
        dic[sorted_lst[i]] = i

    for k in lst:
        print(dic[k], end=' ')

    return


N = int(input())
lst = list(map(int, input().split()))
solution()
