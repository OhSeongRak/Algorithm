import sys

input = sys.stdin.readline


def solution():
    stack = [0]
    answer = 0

    for _, h in lst:
        while h < stack[-1]:
            stack.pop()
            answer += 1

        if stack[-1] == h:
            continue

        stack.append(h)

    return answer + len(stack) - 1


N = int(input())
lst = [tuple(map(int, input().split())) for _ in range(N)]
print(solution())
