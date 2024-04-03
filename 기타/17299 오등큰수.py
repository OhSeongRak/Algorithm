import sys
from collections import defaultdict

input = sys.stdin.readline


def solution():
    F = defaultdict(int)

    for k in lst:
        F[k] += 1

    stack = []
    answer = [-1] * N

    for i in range(N):
        while stack and F[lst[stack[-1]]] < F[lst[i]]:
            answer[stack.pop()] = lst[i]

        stack.append(i)

    return answer


N = int(input())
lst = list(map(int, input().split()))
print(*solution())
