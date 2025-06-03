import sys

input = sys.stdin.readline


def solution():
    stack = []

    for ch in lst:
        if ch.isalpha():
            stack.append(alpha[ord(ch) - ord('A')])
        else:
            y = stack.pop()
            x = stack.pop()
            if ch == '+':
                stack.append(x + y)
            if ch == '-':
                stack.append(x - y)
            if ch == '*':
                stack.append(x * y)
            if ch == '/':
                stack.append(x / y)

    return f"{stack[-1]:.2f}"


N = int(input())
lst = list(input().strip())
alpha = [int(input()) for _ in range(N)]
print(solution())