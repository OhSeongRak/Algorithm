import sys

input = sys.stdin.readline


def solution():
    stack = []
    nge = [-1] * N

    for i in range(N):
        if not stack:
            stack.append(i)

        while stack:
            if lst[stack[-1]] >= lst[i]:
                break
            nge[stack.pop()] = lst[i]

        stack.append(i)

    return nge


N = int(input())
lst = list(map(int, input().split()))
print(*solution())
