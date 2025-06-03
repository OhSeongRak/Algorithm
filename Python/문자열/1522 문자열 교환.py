import sys

input = sys.stdin.readline


def solution():
    global lst

    total = lst.count('a')
    answer = len(lst)
    lst = lst + lst

    for i in range(len(lst) - total + 1):
        answer = min(answer, total - lst[i:i + total].count('a'))

    return answer


lst = list(input().strip())
print(solution())
