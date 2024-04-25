import sys

input = sys.stdin.readline


def solution():
    stack = []
    answer = 0

    for k in lst:
        while stack and k >= stack[-1]:
            stack.pop()
        answer += len(stack)
        stack.append(k)

    return answer


N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
print(solution())
