import sys

input = sys.stdin.readline


def solution():
    lst = [i for i in range(101)]

    for i in range(7, 101):
        for j in range(3, i - 2):
            lst[i] = max(lst[i], lst[j] * (i - j - 1))

    return lst[N]


N = int(input())
print(solution())
