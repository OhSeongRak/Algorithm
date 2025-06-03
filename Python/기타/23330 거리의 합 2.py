import sys

input = sys.stdin.readline


def solution():
    lst.sort()
    total = 0
    for i in range(1, N):
        total += (lst[i] - lst[i - 1]) * (N - i) * i

    return total * 2


N = int(input())
lst = list(map(int, input().split()))
print(solution())
