import sys

from collections import defaultdict

input = sys.stdin.readline


def solution():
    dic = defaultdict(int)

    for k in lst:
        if len(k) < M:
            continue
        dic[k] += 1

    words = []
    for k in dic.keys():
        words.append([dic[k], k])

    words.sort(key=lambda x: [-x[0], (-len(x[1]), x[1])])
    for _, k in words:
        print(k)

    return


N, M = map(int, input().split())
lst = []
for _ in range(N):
    lst.append(input().strip())
solution()
