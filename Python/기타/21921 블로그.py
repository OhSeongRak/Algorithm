import sys
from collections import defaultdict

input = sys.stdin.readline


def solution():
    max_visited = sum(lst[:X])
    cur = sum(lst[:X])
    counter = defaultdict(int)
    counter[cur] = 1

    for i in range(N - X):
        cur = cur - lst[i] + lst[i + X]
        counter[cur] += 1
        max_visited = max(max_visited, cur)

    if max_visited == 0:
        print("SAD")
    else:
        print(max_visited)
        print(counter[max_visited])

    return


N, X = map(int, input().split())
lst = list(map(int, input().split()))
solution()
