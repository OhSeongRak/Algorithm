import sys

from collections import defaultdict

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    clothes = defaultdict(list)
    for _ in range(N):
        name, type = input().split()
        clothes[type].append(name)

    answer = 1
    for cloth in clothes.keys():
        answer *= (len(clothes[cloth]) + 1)
    print(answer - 1)
