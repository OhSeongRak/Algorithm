import sys

input = sys.stdin.readline


def solution():
    answer, cur = 0, 0
    stack = []
    for k in lst:
        if not stack:
            stack.append(k)
            cur += 1
            continue

        if stack[-1] == k:
            stack.append(k)
            cur += 1
        else:
            stack.pop()
            answer = max(answer, cur)
            cur -= 1

    if stack:
        return -1

    return answer


N = int(input())
lst = list(input().strip())
print(solution())
