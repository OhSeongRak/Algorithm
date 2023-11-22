import sys

input = sys.stdin.readline


def solution():
    stack = []

    for k in lst:
        stack.append(k)
        while len(stack) >= 4 and stack[-1] == 'P':
            if "".join(stack[-4:]) == 'PPAP':
                for _ in range(3):
                    stack.pop()
            else:
                break

    if len(stack) == 1 and stack[0] == 'P':
        return 'PPAP'
    return 'NP'


lst = list(input().strip())
print(solution())
# 일단 하나씩 집어넣음
# while stack[-1] == p 고 길이가 4 이상이면 체크
# 시초 나올 수도 있음