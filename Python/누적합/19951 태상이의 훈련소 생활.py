import sys

input = sys.stdin.readline


def solution():
    pre = [0] * (N + 1)

    for a, b, k in order:
        pre[a - 1] += k
        pre[b] -= k

    for i in range(1, N + 1):
        pre[i] += pre[i - 1]

    for i in range(N):
        print(lst[i] + pre[i], end=' ')

    return


N, M = map(int, input().split())
lst = list(map(int, input().split()))
order = [list(map(int, input().split())) for _ in range(M)]
solution()
